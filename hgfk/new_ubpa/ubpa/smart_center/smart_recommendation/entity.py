# CI-FLAG-NOT-COMPILE

from typing import Dict, Optional, Union

from pydantic import BaseModel


class JSONRPCRequest(BaseModel):
    jsonrpc: str = "2.0"
    method: str
    params: Dict = None
    id: Optional[Union[int, str]] = None
