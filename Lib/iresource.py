# coding: utf8
"""
资源库
"""

from typing import Any

import pandas as pd

# 元素与对象库
from ubpa.iobject import (base, browser, controller, device, office, system,
                          vision)
from ubpa.iobject.element import (Action as _Action, Element as _Element,
                                  PickType as _PickType)
from ubpa.iobject.resource import By as _By, Resource as _Resource

Action = _Action
Element = _Element
Resource = _Resource


class iSElement(Element):
    """元素库"""

    def __init__(self, metadata: dict = None):
        super(iSElement, self).__init__(metadata)

    @property
    def _property(self) -> dict:
        """元素元属性字典"""
        return super()._property

    def get_property(self, name: str, default: Any = None) -> Any:
        """
        获取元属性值

        :param name: 属性名称，
        :param default: 默认值
        :return: 结果属性值
        """
        return super().get_property(name, default)

    def set_property(self, name: str, value: Any) -> bool:
        """
        设置元属性值

        :param name: 属性名称，
        :param value: 新的属性值
        :return: 是否设置成功
        """
        return super().set_property(name, value)

    class PickType:
        """拾取类型枚举"""
        # 浏览器拾取
        IE = _PickType.ie
        Chrome = _PickType.chrome
        Firefox = _PickType.firefox
        Edge = _PickType.edge
        Qihoo = _PickType.qihoo
        # 客户端拾取
        CS = _PickType.cs
        UIA = _PickType.uia
        Java = _PickType.java
        SAP = _PickType.sap
        # 图片拾取
        Image = _PickType.image

    class Property:
        """元素属性名枚举"""

        class Base:
            """基础属性"""
            Name = _Element.Property.Name
            PickType = _Element.Property.PickType
            ProjectPath = _Element.Property.ProjectPath

        class IE:
            """IE浏览器属性"""
            Control = _Element.Property.Selector
            Title = _Element.Property.TopTitle
            Url = _Element.Property.Url

        class _Webkit:
            """类Webkit内核浏览器属性"""
            Control = _Element.Property.AttrMap
            Title = _Element.Property.Title
            Url = _Element.Property.Url

        Chrome = Firefox = Edge = Qihoo = _Webkit

        class _Win32:
            Title = _Element.Property.WindowTitle
            Class = _Element.Property.WindowClass

        class UIA(_Win32):
            """UIA窗口属性"""
            Control = _Element.Property.Selector

        class CS(_Win32):
            """CS窗口属性"""
            Control = _Element.Property.ControlAdvanced

        class Java:
            """Java窗口属性"""
            Control = _Element.Property.Hierarchy
            Title = _Element.Property.Title
            ClassName = _Element.Property.ClassName
            Program = _Element.Property.Program
            JvmTitle = _Element.Property.JvmTitle
            JvmClassName = _Element.Property.JvmClassName
            JvmProgram = _Element.Property.JvmProgram

        class SAP:
            """SAP窗口属性"""
            Control = _Element.Property.SapId
            Title = _Element.Property.WinTitle
            CellColumn = _Element.Property.SapCellColumn
            CellRow = _Element.Property.SapCellRow
            ExtractData = _Element.Property.ExtractData
            MaxRow = _Element.Property.MaxRow

        class Image:
            """图片拾取属性"""
            Control = _Element.Property.Target
            Title = _Element.Property.WinTitle
            Path = _Element.Property.SnapshotPreview

        class CV:
            """智能拾取属性
            其他拾取类型下设置cv属性，则转变为智能拾取类型"""
            Control = _Element.Property.CV

    @property
    def id(self) -> str:
        """元素唯一号"""
        return super().id

    @property
    def name(self) -> str:
        """元素名称"""
        return super().name

    @property
    def code(self) -> str:
        """元素编号"""
        return super().code

    @property
    def desc(self) -> str:
        """元素描述"""
        return super().desc

    @property
    def type(self) -> str:
        """元素类型"""
        return super().type

    @property
    def pick_type(self) -> str:
        """元素拾取类型"""
        return super().pick_type

    @property
    def process_name(self) -> str:
        """元素所属程序进程名称"""
        return super().process_name

    @property
    def window_title(self) -> str:
        """元素所属窗口标题"""
        return super().window_title

    @property
    def url(self) -> str:
        """Web元素url地址"""
        return super().url

    @property
    def path(self) -> str:
        """元素所在窗体控件路径"""
        return super().path

    @property
    def snapshot(self) -> str:
        """元素截图"""
        return super().snapshot

    @property
    def project_path(self) -> str:
        """项目文件夹路径"""
        return super().project_path

    def properties(self) -> list:
        """返回所有元素对象属性"""
        return super().properties()

    def actions(self) -> list:
        """返回所有动作方法"""
        return super().actions()

    def help(self, name="actions") -> str:
        """
        查看元素对象动作方法帮助，传递方法名即可打印出帮助内容。

        :param name: 方法名，默认"actions"
        :return: None
        """
        return super().help(name)

    def action_doc(self, name="actions", logging=False) -> str:
        """
        元素对象方法使用文档

        :param name: 方法名称，默认"actions"
        :param logging: 是否日志打印，默认否
        :return: 使用方法文档
        """
        return super().action_doc(name, logging)

    def click(self, horizontal_offset=0, vertical_offset=0,
              wait_seconds=Action.WaitSeconds) -> Element:
        """
        鼠标点击元素

        :param horizontal_offset: 水平x轴偏移，正数向右，负数向左，默认0
        :param vertical_offset: 垂直y轴偏移，正数向下，负数向上，默认0
        :param wait_seconds: 等待时间秒数，默认3秒
        :return: 动作的返回，或者报错返回False
        """
        return super().click(
            horizontal_offset, vertical_offset, wait_seconds)

    def double_click(self, horizontal_offset=0, vertical_offset=0,
                     wait_seconds=Action.WaitSeconds) -> Element:
        """
        鼠标双击元素

        :param horizontal_offset: 水平x轴偏移，正数向右，负数向左，默认0
        :param vertical_offset: 垂直y轴偏移，正数向下，负数向上，默认0
        :param wait_seconds: 等待时间秒数，默认3秒
        :return: True / False
        """
        return super().double_click(
            horizontal_offset, vertical_offset, wait_seconds)

    def mouse_over(self, horizontal_offset=0, vertical_offset=0,
                   wait_seconds=Action.WaitSeconds) -> Element:
        """
        鼠标移动至元素

        :param horizontal_offset: 水平x轴偏移，正数向右，负数向左，默认0
        :param vertical_offset: 垂直y轴偏移，正数向下，负数向上，默认0
        :param wait_seconds: 等待时间秒数，默认3秒
        :return: True / False
        """
        return super().mouse_over(
            horizontal_offset, vertical_offset, wait_seconds)

    def position(self, point: (str, int) = "lt",
                 horizontal_offset=0, vertical_offset=0,
                 wait_seconds=Action.WaitSeconds) -> [tuple, bool, None]:
        """
        获取元素矩形区域左上角（默认）所在屏幕坐标位置和宽高像素值

        :param point: 区域内参照点位，0中心c、1左上lt（默认）、2右上rt、3右下rb、4左下lb
        :param horizontal_offset: 水平x轴偏移，正数向右，负数向左，默认0
        :param vertical_offset: 垂直y轴偏移，正数向下，负数向上，默认0
        :param wait_seconds: 等待时间秒数，默认3秒
        :return: （x, y, width, height） / False
        """
        return super().position(
            point, horizontal_offset, vertical_offset, wait_seconds)

    def existed(self, wait_seconds=Action.WaitSeconds) -> [bool, None]:
        """
        元素是否存在

        :param wait_seconds: 等待时间秒数，默认3秒
        :return: True / False
        """
        return super().existed(wait_seconds)

    def get_text(self, wait_seconds=Action.WaitSeconds) -> [str, bool, None]:
        """
        获取元素文本

        :param wait_seconds: 等待时间秒数，默认3秒
        :return: 文本内容字符串 / False
        """
        return super().get_text(wait_seconds)

    def set_text(self, value="", wait_seconds=Action.WaitSeconds) -> Element:
        """
        设置元素文本

        :param value:文本内容，默认""空字符
        :param wait_seconds: 等待时间秒数，默认3秒
        :return: True / False
        """
        return super().set_text(value, wait_seconds)

    def match_text(self, value, wait_seconds=Action.WaitSeconds
                   ) -> [bool, None]:
        """
        匹配元素文本是否含有该值

        :param value: 匹配的文本，默认""空字符
        :param wait_seconds: 等待时间秒数，默认3秒
        :return: True / False
        """
        return super().match_text(value, wait_seconds)

    def options(self, wait_seconds=Action.WaitSeconds) -> [list, bool, None]:
        """
        获取全部下拉选择项

        :param wait_seconds: 等待时间秒数，默认3秒
        :return: 所有下拉项列表 / False
        """
        return super().options(wait_seconds)

    def get_option(self, wait_seconds=Action.WaitSeconds) -> [str, bool, None]:
        """
        获取下拉选择项

        :param wait_seconds: 等待时间秒数，默认3秒
        :return: 下拉项值 / False
        """
        return super().get_option(wait_seconds)

    def set_option(self, option="", wait_seconds=Action.WaitSeconds) -> Element:
        """
        设置下拉选择项

        :param option: 选项内容，默认""空字符
        :param wait_seconds: 等待时间秒数，默认3秒
        :return: True / False
        """
        return super().set_option(option, wait_seconds)

    def check(self, checked=1, sync=0, wait_seconds=Action.WaitSeconds
              ) -> Element:
        """
        设置Checkbox勾选状态

        :param checked: 勾选状态 1（勾选）/0（不勾选），默认1
        :param sync: 是否异步执行 1（异步）/0（同步），默认0
        :param wait_seconds: 等待时间秒数，默认3秒
        :return: True / False
        """
        return super().check(checked, sync, wait_seconds)

    def checked(self, wait_seconds=Action.WaitSeconds) -> [bool, None]:
        """
        检查Checkbox是否被勾选

        :param wait_seconds: 等待时间秒数，默认3秒
        :return: True / False
        """
        return super().checked(wait_seconds)

    def capture(self, wait_seconds=Action.WaitSeconds) -> [str, bool, None]:
        """
        元素截图

        :param wait_seconds: 等待时间秒数，默认3秒
        :return: 图片路径字符串 / False
        """
        return super().capture(wait_seconds)

    def get_table(self, wait_seconds=Action.WaitSeconds
                  ) -> [pd.DataFrame, bool, None]:
        """
        获取表格元素数据

        :param wait_seconds: 等待时间秒数，默认3秒
        :return: 返回pandas的DataFrame结构数据 / False
        """
        return super().get_table(wait_seconds)

    def get_html(self, wait_seconds=Action.WaitSeconds) -> [str, bool, None]:
        """
        获取元素Html源码

        :param wait_seconds: 等待时间秒数，默认3秒
        :return: html源码字符串 / False
        """
        return super().get_html(wait_seconds)


class By:
    """查找元素时所需依据"""

    ID = _By.ID
    CODE = _By.CODE
    NAME = _By.NAME


class iSResource(Resource):
    """资源库"""

    # 资源库
    Resource = None

    def __init__(self, script_path=None, json_file=None):
        """
        资源库初始化
        可通过脚本查找项目目录下的resources/elements.json文件；
        若在自定义脚本中使用元素库，可直接指定elements.json文件路径，
        二选一，优先以‘元素库json文件路径’初始化。

        :param script_path: Python模块脚本路径
        :param json_file: 元素库json文件路径
        """
        super(iSResource, self).__init__(script_path, json_file)

    def get_global_var(self, name="gv_1") -> Any:
        """根据名称获取全局变量"""
        return super().get_global_var(name=name)

    def set_global_var(self, name="gv_1", value=None):
        """根据名称设置全局变量值"""
        super().set_global_var(name=name, value=value)

    def get_flow_var(self, name="lv_1") -> Any:
        """根据名称获取流程变量（参数）"""
        return super().get_flow_var(name=name)

    def set_flow_var(self, name="lv_1", value=None):
        """根据名称设置流程变量（参数）值"""
        super().set_flow_var(name=name, value=value)

    def all_global_var(self) -> list:
        """所有全局变量"""
        return super().all_global_var()

    def all_flow_var(self) -> list:
        """所有流程变量和参数"""
        return super().all_flow_var()

    def get_element(self, by=By.ID, value=None) -> iSElement:
        """查找元素对象"""
        return super().get_element(by=by, value=value)

    def get_element_by_id(self, value=None) -> iSElement:
        """按id查找元素对象"""
        return super().get_element_by_id(value=value)

    def get_element_by_code(self, value=None) -> iSElement:
        """按code查找元素对象"""
        return super().get_element_by_code(value=value)

    def get_element_by_name(self, value=None) -> iSElement:
        """按name查找元素对象"""
        return super().get_element_by_name(value=value)

    def set_action_wait_seconds(self, value: int = 5):
        """
        全局设置动作方法执行的等待时间秒数，动作方法报错时每秒会重试1次。

        :param value: 秒数值
        :return:
        """
        return super().set_action_wait_seconds(value=value)

    def all(self) -> dict:
        """全部资源
        元素、项目、流程"""
        return super().all()

    def elements(self) -> list:
        """全部元素"""
        return super().elements()


class iSObject:
    """对象库"""

    # 基础对象
    DialogBox = base.DialogBox  # 对话框窗口，消息框、输入框等

    # 浏览器对象
    Browser = browser.Browser  # 浏览器，打开网址、进入网址等

    # 控制台对象
    Server = controller.Server  # 服务器，设置变量、获取变量等

    # 外设对象
    Keyboard = device.Keyboard  # 键盘，模拟按键、控件输入等
    Mouse = device.Mouse  # 鼠标，点击位置、拖拽、滚动滚轮等

    # Office办公对象
    Excel = office.Excel  # Excel表格，单元格写入等
    Email = Mail = office.Email  # Mail邮件类，发送邮件等

    # 系统对象
    Clipboard = system.Clipboard  # 剪贴板，拷贝到剪贴板、从剪贴板获取等
    Executor = system.Executor  # 执行器，运行应用、打开文件(目录)等
    Window = system.Window  # 窗口类，激活、最大化、最小化等

    # 视觉对象
    Image = vision.Image  # 图像类，截图等
    OCR = vision.OCR  # OCR类，OCR文本识别、验证码等
