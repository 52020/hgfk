# CI-FLAG-NOT-COMPILE

from typing import List, Optional

from pydantic import BaseModel


class Output:
    def __init__(self, *args, **kwargs):
        super(Output, self).__init__()
        # self.id = id
        self.labelName = kwargs.get("labelName")
        self.confidence = kwargs.get("confidence")
        self.box = kwargs.get("box")
        self.order = kwargs.get("order")
        self.text = kwargs.get("text")
        self.part = kwargs.get("part")
        self.row = kwargs.get("row")
        self.col = kwargs.get("col")

    def __str__(self):
        return f"[{self.order}, {self.labelName}, {self.confidence}, {self.box}, {self.text}]"

    def __repr__(self):
        return f"[{self.order}, {self.labelName}, {self.confidence}, {self.box}, {self.text}]"


class ClientRole:
    Capture1 = "pickup_get_index"
    Capture2 = "pickup_get_ocr_res"
    Capture3 = "pickup_get_rect_ocr_res"
    Replay = "real_play_back"


class Data(BaseModel):
    image: str
    type: str


class Info(BaseModel):
    hashCode: str
    machineNo: str
    timestamp: str


class Recognition(BaseModel):
    info: Info
    version: str  # Refers to "version mark"


class AlgRequest(BaseModel):
    resId: Optional[str]
    data: Data
    fun_type: str
    recognition: Recognition
    boxes: Optional[List[List[int]]]
