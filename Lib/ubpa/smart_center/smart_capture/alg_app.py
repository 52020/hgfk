"""
    FastAPI App of the Algorithm
"""
# CI-FLAG-NOT-COMPILE

import os
import time
from threading import Thread

import psutil
from fastapi import FastAPI

import config
from ubpa.smart_center.lib_smart_capture import pipelines
from ubpa.pub.pubfun import cv_imread
from ubpa.smart_center.smart_capture.entity import AlgRequest
from ubpa.smart_center.smart_capture.utils import UtilSet

# Create a logging object
logger = config.get_logger("AlgServer.log")

# Get model info from environment variables
REC_MODEL_PATH = os.environ["rec_model_path"]
DET_MODEL_PATH = os.environ["det_model_path"]
CHAR_DICT_PATH = os.environ["char_dict_path"]
CLASSES_PATH = os.environ["classes_path"]
MAIN_PROCESS_PID = os.environ["main_process_pid"]

# Instantiate the algorithm object
PIPELINE = pipelines.SmartCapturePipeline(
    det_model_path=DET_MODEL_PATH,
    rec_model_path=REC_MODEL_PATH,
    char_dict_path=CHAR_DICT_PATH,
    classes_path=CLASSES_PATH
)

# Create a web application
app = FastAPI()


def main_process_watcher():
    logger.info("主进程watcher已启动...")
    my_p = psutil.Process(os.getpid())

    while True:
        if psutil.pid_exists(int(MAIN_PROCESS_PID)) is False:
            logger.error("检测到主进程退出,强制退出本进程")
            my_p.terminate()

        # print(f"{MAIN_PROCESS_PID}存在")

        time.sleep(1)


# Start process watcher
Thread(target=main_process_watcher).start()


@app.post("/boxes")
async def get_boxes(req: AlgRequest):
    ts_str = req.recognition.info.timestamp
    machine_no = req.recognition.info.machineNo
    hash_code = req.recognition.info.hashCode
    img_path = req.data.image

    try:
        bgr_img = cv_imread(img_path)
    except Exception:
        logger.error(f"读取图片{img_path}出错", exc_info=True)
        return UtilSet.make_response(code=-2, msg=f"读取图片{img_path}出错")

    ts_detection = time.time()
    box_results = PIPELINE.get_boxes(bgr_img=bgr_img, ts_str=ts_str, machine_no=machine_no, hash_code=hash_code)
    logger.debug(f"元素检测算法花费{(time.time() - ts_detection) * 1000}毫秒")

    try:
        box_ret = UtilSet.assemble_dict_results(req, box_results)
    except Exception as e:
        logger.error(f"组装处理结果出错,{e}", exc_info=True)
        return UtilSet.make_response(code=-4, msg="组装处理结果出错")

    return box_ret


@app.post("/ocr")
async def get_ocr_results(req: AlgRequest):
    ts_str = req.recognition.info.timestamp
    machine_no = req.recognition.info.machineNo
    hash_code = req.recognition.info.hashCode
    img_path = req.data.image
    boxes = req.boxes

    try:
        bgr_img = cv_imread(img_path)
    except Exception:
        logger.error(f"读取图片{img_path}出错", exc_info=True)
        return UtilSet.make_response(code=-2, msg=f"读取图片{img_path}出错")

    ts_detection = time.time()
    try:
        ocr_results = PIPELINE.get_ocr_results(bgr_img=bgr_img, boxes=boxes, ts_str=ts_str, machine_no=machine_no,
                                               hash_code=hash_code)
    except Exception:
        logger.error(f"获得OCR结果出错", exc_info=True)
        return UtilSet.make_response(code=-2, msg=f"获得OCR结果出错")
    logger.debug(f"OCR算法处理花费{(time.time() - ts_detection) * 1000}毫秒")
    return ocr_results


@app.post("/predict")
async def predict(req: AlgRequest):
    # Validate the signature
    ts_str = req.recognition.info.timestamp
    machine_no = req.recognition.info.machineNo
    hash_code = req.recognition.info.hashCode
    img_path = req.data.image

    try:
        bgr_img = cv_imread(img_path)
    except Exception:
        logger.error(f"读取图片{img_path}出错", exc_info=True)
        return UtilSet.make_response(code=-2, msg=f"读取图片{img_path}出错")

    # [idx, class_id, confidence, box, text_result]
    ts_detection = time.time()

    try:
        pipeline_results = PIPELINE.detect(bgr_img, ts_str=ts_str, machine_no=machine_no, hash_code=hash_code)
    except Exception as e:
        logger.error("获得结果出错", exc_info=True)
        return UtilSet.make_response(code=-3, msg=str(e))
    logger.debug(f"元素检测+OCR算法总共花费{(time.time() - ts_detection) * 1000}毫秒")

    try:
        pipeline_ret = UtilSet.assemble_dict_results(req, pipeline_results)
    except Exception as e:
        logger.error(f"组装处理结果出错,{e}", exc_info=True)
        return UtilSet.make_response(code=-4, msg="组装处理结果出错")

    return pipeline_ret


# Check if the server has been started
@app.get("/check")
async def check():
    logger.debug("收到一条测试接口请求")
    return {"msg": "OK"}


if __name__ == "__main__":
    pass
