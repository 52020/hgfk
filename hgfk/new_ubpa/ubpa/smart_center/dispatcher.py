# CI-FLAG-NOT-COMPILE

"""
智能中心调度器
"""
import os
from threading import Thread

import uvicorn.server
from fastapi import FastAPI

from ubpa.pub.pubfun import get_logger_for_independent, terminate_process
from ubpa.smart_center import pub_utils
from ubpa.smart_center.smart_capture.smart_cap import SmartCapture
from ubpa.smart_center.smart_recommendation.smart_rec import (
    sub_recommendation_app)

logger = get_logger_for_independent("SmartCenterDispatcher.log", __name__)

# # ROUTERS DEFINITION BEGIN

# Register routers
app = FastAPI()

# sub routers registration
app.mount("/recommendation", sub_recommendation_app)


# main router registration
@app.get("/check")
async def check():
    logger.debug("收到一条测试接口请求")
    return {"msg": "OK"}


# # ROUTERS DEFINITION END


def write_free_port():
    try:
        free_port = pub_utils.get_free_port()
        logger.info(f"获得一个空闲端口号: {free_port}")

        config_path = pub_utils.write_port(free_port)
        logger.info(f"写入空闲端口号「{free_port}」到文件「{config_path}」成功")

        return int(free_port)
    except Exception:
        logger.error(f"获取空闲端口号失败", exc_info=True)
        raise GetFreePortError("获取空闲端口号失败")


def start_smart_capture_udp_server(_uvicorn_server):
    logger.info(f"即将启动智能CV UDP服务...")
    try:
        # 启动socket循环监听，异常或设计器关闭时，返回结果
        capture = SmartCapture()
        ret = capture.listen()
        if ret is None:
            cur_pid = os.getpid()
            _uvicorn_server.shutdown()
            logger.debug(f"uvicorn_server shutdown [{cur_pid}]")

            # 使用进程id关闭进程，未成功则使用进程名
            closed = terminate_process(pid=cur_pid)
            if not closed:
                terminate_process("pythoncv.exe")
    except Exception as e:
        logger.error(f"start_smart_capture_udp_server error: {e}")
        raise e


def start_modules(_uvicorn_server):
    logger.info(f"开启Smart Center子模块...")
    Thread(target=start_smart_capture_udp_server, args=(_uvicorn_server,)).start()


# 自定义异常
class GetFreePortError(Exception):
    pass


if __name__ == '__main__':
    free_port = write_free_port()
    uvicorn_server = uvicorn.Server(
        uvicorn.Config(app, host="127.0.0.1", port=free_port))
    start_modules(uvicorn_server)
    logger.debug(f"uvicorn_server started [{os.getpid()}]")
    uvicorn_server.run()
