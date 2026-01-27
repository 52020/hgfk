# coding: utf8
"""
Python模块脚本
"""

import os

# 项目路径、资源库元素文件（建议其他元素库文件路径在此处声明）
ProjectPath = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
CodePath = os.path.join(ProjectPath, "codes")
ModulePath = os.path.join(CodePath, "modules")
ElementFile = os.path.join(ModulePath, "resources", "elements.json")
