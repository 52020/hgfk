# coding: utf8
"""
操作系统类对象，窗口、剪贴板、文件管理、资源情况等
"""

from typing import Any

from ubpa import iclipboard, ics
from ubpa import iwin
from ubpa.iobject.element import Action


class Clipboard:
    """剪贴板"""

    @classmethod
    def set(cls, value: Any):
        """
        设置剪贴板内容，（拷贝到剪贴板）
        :param value:
        :return:
        """
        return iclipboard.set_clipboard(text=value)

    @classmethod
    def get(cls, strip=True) -> str:
        """
        从剪贴板获取内容
        :param strip: 是否去除收尾空格，默认去除
        :return:
        """
        value: str = iclipboard.get_clipboard()
        return value.strip() if strip else value


class Executor:
    """执行器"""

    @staticmethod
    def run(path: str, cwd=None):
        """
        运行可执行exe应用程序
        :param path: 应用程序文件路径，例如：r"C:/cms/cms.exe"
        :param cwd: 需要切换到的工作目录，例如：cwd=r"C:/cms" 等同于 "cd C:/cms"
        :return:
        """
        return ics.run_app(path=path, work_path=cwd)

    @staticmethod
    def open(path: str):
        """
        打开文件或目录
        例如，word文档文件，由系统判断文件类型，并使用支持的应用（office或wps）打开。
        :param path: 文件或目录路径，例如：r"C:/work.docx" 或 r"C:/work"
        :return:
        """
        return ics.run_shellexecute(path=path)


class Window(object):
    """窗口"""

    def __init__(self, win_title: str = "",
                 win_class: [str, None] = None,
                 win_text: [str, None] = None):
        """
        实例化
        示例：
            Window("无标题 - 记事本")  # 记事本新建窗口
            Window(element.window_title)  # 用元素属性实例化
        :param win_title: 窗口标题名称，可使用元素对象的window_title属性传递
        """
        self.win_title = win_title
        self.win_class = win_class
        self.win_text = win_text

    def activate(self, wait_seconds: int = Action.WaitSeconds):
        """
        窗口激活
        示例：
            # 不输入等待时长，则使用默认的Action.WaitSeconds参数（3秒）
            Window().activate()

            # 指定等待时长为1秒
            Window().activate(wait_seconds=1000)
        :param wait_seconds：等待时长，默认3秒
        """
        return iwin.do_win_activate(
            win_title=self.win_title,
            win_class=self.win_class,
            win_text=self.win_text,
            waitfor=wait_seconds
        )

    def maximize(self, wait_seconds: int = Action.WaitSeconds):
        """
        窗口最大化
        示例：
            # 不输入等待时长，则使用默认的Action.WaitSeconds参数（3秒）
            Window().maximize()

            # 指定等待时长为1秒
            Window().maximize(wait_seconds=1000)
        :param wait_seconds：等待时长，默认3秒
        """
        return iwin.do_win_maximize(
            win_title=self.win_title,
            win_text=self.win_text,
            waitfor=wait_seconds
        )

    def minimize(self, wait_seconds: int = Action.WaitSeconds):
        """
        窗口最小化
        示例：
            # 不输入等待时长，则使用默认的Action.WaitSeconds参数（3秒）
            Window().minimize()

            # 指定等待时长为1秒
            Window().minimize(wait_seconds=1000)
        :param wait_seconds：等待时长，默认3秒
        """
        return iwin.do_win_minimize(
            win_title=self.win_title,
            win_text=self.win_text,
            waitfor=wait_seconds
        )

    def close(self, force=False, wait_seconds: int = Action.WaitSeconds):
        """
        关闭窗口
        示例：
            # 使用默认的Action.WaitSeconds参数（3秒）关闭窗口
            Window().close()

            # 指定等待时长为1秒
            Window().close(wait_seconds=1000)

            # 指定强行关闭窗口
            Window().close(force=True)
        :param force: 布尔类型，True为强行关闭窗口，默认值为False
        :param wait_seconds：等待时长，默认3秒
        """
        close_window = iwin.do_win_kill if force else iwin.do_win_close
        return close_window(
            win_title=self.win_title,
            win_text=self.win_text,
            waitfor=wait_seconds
        )
