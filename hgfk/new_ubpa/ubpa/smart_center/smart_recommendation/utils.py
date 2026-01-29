from typing import Dict


def make_response(req_id, result=None, error=None) -> Dict:
    """
    组装为jsonrpc2.0的返回格式

    @param req_id: 请求传过来的id
    @param result: 成功时返回的对象
    @param error: 失败时返回的错误对象

    @return: Dict
    """

    response = {
        "jsonrpc": "2.0",
        "id": req_id,
    }

    # 根据JSON-RPC 2.0协议，有两种返回格式
    # https://www.jsonrpc.org/specification
    if result is not None:
        response.update({"result": result})
    else:
        response.update({"error": error})

    return response
