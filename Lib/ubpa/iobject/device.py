# coding: utf8
"""
外设类对象，包含：键盘、鼠标、USB设备、屏幕、喇叭、麦克风、等
"""

import re

from ubpa import ics, ikeyboard
from ubpa.iobject.element import Action
from ubpa.pub.pubenum import MouseButton, MouseScroll


class Keyboard:
    """键盘"""

    class HotKeys:
        """热键"""
        _hot_keys = tuple("^+!#")
        _letter_keys = tuple("abcdefghijklmnopqrstuvwxyz")
        CTRL, SHIFT, ALT, WIN = _hot_keys
        (A, B, C, D, E, F, G, H, I, J, K, L, M, N,
         O, P, Q, R, S, T, U, V, W, X, Y, Z) = _letter_keys

        @classmethod
        def CombinationOf(cls, *hotkeys, letter=""):
            """
            组合热键
            :param hotkeys: 热键，接受多个热键
            :param letter: 单个字母键
            :return:
            """
            _hotkeys = "".join(set(hotkeys) & set(cls._hot_keys))
            letter = "".join({str(letter).lower()} & set(cls._letter_keys))
            if (letter == "" and hotkeys != ""
                    and hotkeys[-1] in cls._letter_keys):
                letter = hotkeys[-1]
            return _hotkeys + letter

        Plus = Put = Group = CombinationOf

    class Keys:
        """键值，排列顺序：从上到下，从左到右"""
        # 第一排：退出，F区
        ESC = "{ESC}"
        F1, F2, F3, F4, F5, F6, F7, F8, F9, F10, F11, F12 = (
            "{F1}", "{F2}", "{F3}", "{F4}", "{F5}", "{F6}",
            "{F7}", "{F8}", "{F9}", "{F10}", "{F11}", "{F12}")
        # 第二排：叹号，加号，反号，井号，删除键
        TAB = "{TAB}"
        BANG, PLUS, CARET, SHARP = "{!}", "{+}", "{^}", "{#}"
        BACKSPACE, DELETE = "{BACKSPACE}", "{DEL}"
        # 第三排：回车，翻页区
        ENTER = "{ENTER}"
        HOME, END, PGUP, PGDN = "{HOME}", "{END}", "{PGUP}", "{PGDN}"
        # 第四排：左右Ctrl、Shift、Win，以及Alt、空格
        LCTRL, RCTRL = "{LCTRL}", "{RCTRL}"
        LSHIFT, RSHIFT = "{LSHIFT}", "{RSHIFT}"
        LWIN, RWIN = "{LWIN}", "{RWIN}"
        ALT = "{ALT}"
        SPACE = "{SPACE}"
        # 方向键区
        UP, DOWN, LEFT, RIGHT = "{UP}", "{DOWN}", "{LEFT}", "{RIGHT}"

        @classmethod
        def Continuous(cls, key: str, times=1):
            """
            连续多次按键
            示例：
                Keys.Continuous(Keys.ENTER, 2)  # 输出{ENTER 2}
            :param key: 某个按键
            :param times: 连续几次
            :return:
            """
            if not isinstance(key, str):
                return ""
            if not (key.startswith("{") and key.endswith("}")):
                return ""
            if times > 1:
                key = re.findall(r"(?<=\{)(.+?)(?=\})", key)[0]
                return f"{{{key} {times}}}"
            return key

        Again = Copy = More = Multiple = Continuous

    def __init__(self, window_title=""):
        """
        实例化
        示例：
            Keyboard("无标题 - 记事本")           # 记事本新建窗口
            Keyboard(element.window_title)      # 用元素属性实例化
        :param window_title: 窗口标题名称，可使用元素对象的window_title属性传递
        """
        self.window_title = window_title

    def keypress_input(self, *keys, wait_seconds: int = Action.WaitSeconds):
        """
        按键输入，包含以下组件：模拟按键输入、热键输入
        示例：
            # 普通内容与特殊键
            Keyboard().keypress_input("abc", Keys.TAB + Keys.ENTER)

            # 普通内容与组合键
            Keyboard().keypress_input("abc", HotKeys.CTRL + HotKeys.A)

            # 普通内容与组合键+特殊键
            Keyboard().keypress_input(
                "abc", HotKeys.CTRL + Keys.W, HotKeys.ALT + Keys.F4)
        :param keys: 按键，接受多个按键
        :param wait_seconds: 等待时间秒数，默认3秒
        :return:
        """
        ikeyboard.key_send_cs(
            win_title=self.window_title,
            text="".join(keys),
            waitfor=wait_seconds
        )

    def control_input(self, *keys, wait_seconds: int = Action.WaitSeconds):
        """
        控件输入，包含以下组件：控件输入（工具-安装扩展程序-安装USB或PS/2控件驱动）
        示例：
            # 普通内容与特殊键
            Keyboard().control_input("abc", Keys.TAB + Keys.ENTER)

            # 普通内容与组合键
            Keyboard().control_input("abc", HotKeys.CTRL + HotKeys.A)

            # 普通内容与组合键+特殊键
            Keyboard().control_input(
                "abc", HotKeys.CTRL + Keys.W, HotKeys.ALT + Keys.F4)
        :param keys: 按键，接受多个按键
        :param wait_seconds: 等待时间秒数，默认3秒
        :return:
        """
        ikeyboard.control_send_cs(
            win_title=self.window_title,
            text="".join(keys),
            waitfor=wait_seconds
        )


class Mouse:
    """鼠标"""

    class Button:
        """按钮"""
        Left = MouseButton.Left
        Middle = MouseButton.Middle
        Right = MouseButton.Right

    def __init__(self, window_title=""):
        """
        实例化
        示例：
            Mouse()                         # 无窗口激活，例如点击桌面或仅屏幕
            Mouse("无标题 - 记事本")          # 激活记事本窗口
            Mouse(element.window_title)     # 用元素属性实例化
        :param window_title: （激活）窗口标题名称，可使用元素对象的window_title属性传递
        """
        self.window_title = window_title

    def click(self, position: tuple = (0, 0), times=1, button=Button.Left):
        """
        点击
        示例：
            Mouse().click((100, 100))          # 在屏幕x=100,y=100的位置点击左键
            Mouse("无标题 - 记事本").click()     # 激活记事本，并在屏幕位置点击左键
            Mouse().click(button=Button.Right)     # 右键
            Mouse().click(times=2)                 # 双击
        :param position: 坐标位置，（x, y）水平和垂直坐标数值，从屏幕左上角0开始
        :param times: 点击次数
        :param button: 鼠标按钮，左键left（默认），右键right，中键middle
        :return:
        """
        return ics.truple_mouse_click(
            distpos=position,
            win_title=self.window_title,
            times=times,
            mouse_button=button
        )

    def double_click(self, position: tuple = (0, 0), button=Button.Left):
        """双击"""
        return self.click(position=position, times=2, button=button)

    def drag(self, src_position: tuple = (0, 0), dist_position: tuple = (0, 0)):
        """
        拖拽
        :param src_position: 原坐标位置，（x, y）水平和垂直坐标数值，从屏幕左上角0开始
        :param dist_position: 目标坐标位置，（x, y）水平和垂直坐标数值，从屏幕左上角0开始
        :return:
        """
        return ics.do_drag_to_safe(
            srcpos=src_position,
            distpos=dist_position,
            win_title=self.window_title
        )

    @classmethod
    def _scroll(cls, up=True, times=1,
                ctrl=False, shift=False, alt=False):
        """
        滚动，支持辅助按键
        :param up: 是否向上滚动，默认向上True，向下False
        :param times: 滚动次数
        :param ctrl: 是否按住Ctrl键滚动鼠标，默认否
        :param shift: 是否按住Shift键滚动鼠标，默认否
        :param alt: 是否按住Alt键滚动鼠标，默认否
        :return:
        """
        direction = MouseScroll.Up if up else MouseScroll.Down
        hotkeys = [(ctrl, "17"), (shift, "16"), (alt, "18")]
        text = "|".join([value if hotkey else "" for hotkey, value in hotkeys])
        return ics.do_mouse_wheel(
            direction=direction,
            times=times,
            text=text
        )

    @classmethod
    def scroll_up(cls, times=1, ctrl=False, shift=False, alt=False):
        """
        向上滚动
        示例：
            Mouse.scroll_up()                # 向上滚动1下
            Mouse.scroll_up(3, ctrl=True)    # 按住Ctrl键向上滚动3下
        """
        return cls._scroll(True, times=times, ctrl=ctrl, shift=shift, alt=alt)

    @classmethod
    def scroll_down(cls, times=1, ctrl=False, shift=False, alt=False):
        """
        向下滚动
        示例：
            Mouse.scroll_down()                # 向下滚动1下
            Mouse.scroll_down(3, ctrl=True)    # 按住Ctrl键向下滚动3下
        """
        return cls._scroll(False, times=times, ctrl=ctrl, shift=shift, alt=alt)

    @classmethod
    def position(cls) -> tuple:
        """
        鼠标位置
        :return: 坐标位置(x, y)，如(100, 100)
        """
        return ics.get_mouse_pos()
