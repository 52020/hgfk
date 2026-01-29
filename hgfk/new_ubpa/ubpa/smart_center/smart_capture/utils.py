# CI-FLAG-NOT-COMPILE

import configparser
import os
import functools
from pathlib import Path
from socket import socket
from typing import List, Dict
from uuid import uuid4

from ubpa.smart_center.smart_capture import config
from ubpa.pub import pub_path
from ubpa.smart_center.smart_capture.entity import Output, AlgRequest


class UtilSet:

    @staticmethod
    def get_uuid() -> str:
        return str(uuid4()).replace("-", "")

    @staticmethod
    def get_config_path(is_dynamic=False) -> str:
        if pub_path.LinuxOS:
            p_root_path = Path(pub_path.UserDocumentPath) / "RPA"
        else:
            p_root_path = Path(pub_path.PLUGIN_PATH) / config.PLUGIN_NAME

        if is_dynamic is False:
            p_plugin_path = p_root_path / config.STATIC_CONFIG_NAME
        else:
            p_plugin_path = p_root_path / config.DYNAMIC_CONFIG_NAME
        return p_plugin_path.as_posix()

    @staticmethod
    def get_config_parser(is_dynamic=False) -> configparser.ConfigParser:
        conf_path = UtilSet.get_config_path(is_dynamic)
        if is_dynamic is False and os.path.exists(conf_path) is False:
            raise Exception(f"配置文件{conf_path}不存在!")

        _config = configparser.ConfigParser()
        _config.read(conf_path)
        return _config

    # 在配置文件中写入端口号
    @staticmethod
    def write_port(port):
        _conf_path = UtilSet.get_config_path(is_dynamic=True)
        _config = configparser.ConfigParser()
        _config.read(_conf_path, encoding="utf-8")

        # update port
        if not _config.has_section("Server"):
            _config.add_section("Server")
        _config.set("Server", "Port", str(port))

        # write
        with open(_conf_path, "w", encoding="utf-8") as f:
            _config.write(f, space_around_delimiters=False)

    # 获得当前运行环境的版本号
    @staticmethod
    def get_current_version():
        _config = UtilSet.get_config_parser()
        version = _config.get("Models", "Version", fallback="1.0.0")
        return version

    @staticmethod
    def get_default_model_version():
        _config = UtilSet.get_config_parser()
        model_version = _config.get("Models", "Version", fallback="1.0.0")
        return model_version

    # 获得模型基础路径
    @staticmethod
    def get_models_base_path() -> Path:
        parser = UtilSet.get_config_parser()
        res_name = parser.get("Models", "BaseDir", fallback="res")
        p_full_path = Path(pub_path.PLUGIN_PATH) / config.PLUGIN_NAME / res_name / UtilSet.get_current_version()
        return p_full_path

    @staticmethod
    def get_free_port():
        with socket() as s:
            s.bind(('', 0))
            return s.getsockname()[1]

    @staticmethod
    def _cmp(left: Output, right: Output):
        if left.labelName < right.labelName:
            return -1
        if left.labelName > right.labelName:
            return 1
        # left, top, width, height = box
        if left.box[1] < right.box[1]:
            return -1
        if left.box[1] > right.box[1]:
            return 1
        if left.box[0] < right.box[0]:
            return -1
        return 1

    @staticmethod
    def sort_results(results: List[Output]):
        results = sorted(results, key=functools.cmp_to_key(UtilSet._cmp))
        new_results = []

        index = 1
        label_name = ""
        for output in results:
            if label_name != output.labelName:
                label_name = output.labelName
                index = 1
            output.order = index

            new_results.append(output)
            index += 1
        return new_results

    @staticmethod
    def make_response(code=200, msg="OK"):
        return {"code": code, "msg": msg}

    @staticmethod
    def assemble_dict_results(req: AlgRequest, pipeline_results) -> Dict:
        results: List[Output] = []
        for pipeline_result in pipeline_results:
            idx, class_id, label, confidence, box, text_result = pipeline_result
            output = Output(order=idx, labelName=label, confidence=confidence, box=box, text=text_result)
            results.append(output)

        # Sort results
        sorted_results = UtilSet.sort_results(results)

        # Assemble the final result
        js_root = {}

        ai_ret = []

        image_indies = []
        icon_indies = []
        text_indies = []
        doc_indies = []

        for idx, result in enumerate(sorted_results):
            label_name = result.labelName.lower()
            if label_name == "doc":
                doc_indies.append(idx)
            elif label_name == "image":
                image_indies.append(idx)
            elif label_name == "icon":
                icon_indies.append(idx)
            elif label_name == "text":
                text_indies.append(idx)

            ret = {"type": result.labelName.lower(), "text": result.text[0] if result.text else "",
                   "index": result.order,
                   "confidence": float(result.confidence), "rect": {}}
            ret["rect"]["x"] = int(result.box[0])
            ret["rect"]["y"] = int(result.box[1])
            ret["rect"]["w"] = int(result.box[2])
            ret["rect"]["h"] = int(result.box[3])
            ai_ret.append(ret)

        ai_ret.append({"image": image_indies, "icon": icon_indies, "text": text_indies, "doc": doc_indies})

        js_root["result"] = ai_ret
        js_root["retCode"] = 1
        js_root["version"] = req.recognition.version
        return js_root
