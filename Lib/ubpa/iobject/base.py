# coding: utf8
"""
基础类对象，消息框、加解密、日志、错误类、常量类等
"""
from ubpa import ibox


class DialogBox:
    """消息对话框"""

    def __init__(self, title="", duration_time=3, width=300, height=150):
        """
        初始化
        示例：
            DialogBox("消息框", 10)    # 实例化一个10秒后关闭的消息框
        :param title: 对话框窗口标题
        :param duration_time: 对话框持续时长秒数，时长耗尽窗口自动关闭
        """
        self.title = title
        self.duration_time = duration_time
        self.width = width
        self.height = height

    def show_message(self, *messages):
        """
        显示消息框窗口
        示例：
            DialogBox("消息框", 10).show_message("消息内容")
        :param messages: 消息内容，接受多个消息内容
        :return:
        """
        return ibox.msgs_box(
            *messages,
            title=self.title,
            timeout=self.duration_time
        )

    def show_input(self, prompt="请输入", default="", cipher_char="*"):
        """
        显示输入框窗口
        示例：
            DialogBox("输入框", 10).show_input()
        :param prompt: 输入框提示语
        :param default: 输入框默认值
        :param cipher_char: 密文字符，输入框的每个字符，都将被替换为该字符，默认*号
        :return:
        """
        self.title = "InputBox"  # 输入框暂无法修改标题
        return ibox.input_box(
            text=prompt,
            default=default,
            password=cipher_char,
            width=self.width,
            height=self.height,
            timeout=self.duration_time
        )
