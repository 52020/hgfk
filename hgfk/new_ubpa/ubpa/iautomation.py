# -*- coding: utf-8 -*-

# CI-FLAG-NOT-COMPILE

"""
RPA通过uia操作程序

[Refactor] 2022/07/05 曹扬
[refactor] 20220905 haibo
"""

import functools
import json
import os
import time
from ctypes import c_wchar_p
from datetime import datetime
from platform import platform
from queue import Queue
from threading import Thread

import dateutil.parser
import pandas as pd
import uiautomation as automation

import ubpa.encrypt as encrypt
import ubpa.ics as ics
import ubpa.iimg as img
import ubpa.iocr as iocr
from ubpa.iconstant import TRY_INTERVAL, WAIT_FOR
from ubpa.ierror import WinNotFoundError
from ubpa.ilog import ILog
from ubpa.pub.control import ISWindow
from ubpa.pub.dll import Dll
from ubpa.pub.pubfun import get_screen_scale_rate
from ubpa.pub.system import Platform
from ubpa.pub.window import Window

ILoger = ILog(__file__)
uia_client_dll = Dll.uia_client()
RPA_TIMEOUT = 0


def is_win_server():
    """判断是否是Server平台"""
    try:
        platform_str = platform().lower()
    except Exception as e:
        raise Exception(f"获取系统平台信息错误:{e}")

    if not platform_str:
        return False

    if "server" in platform_str and "2012" in platform_str \
            or platform_str.startswith("Windows-8"):
        return True
    return False


class UIAResult:
    Success = "OK"

    def __init__(self, is_exception, result):
        super(UIAResult, self).__init__()
        self.is_exception = is_exception
        self.result = result


def alternative_thread_mode(func):
    """可以使用线程模式运行"""

    @functools.wraps(func)
    def wrapper(**kwargs):  # 目前程序里全都使用关键字参数，所以只将关键字参数传递给线程
        if is_win_server() is False:
            return func(**kwargs)

        ILoger.debug("Using Windows Server mode...")
        result_queue = Queue()  # 用于接收结果
        kwargs.update({"result_q": result_queue})
        uia_thread = Thread(target=func, kwargs=kwargs)
        uia_thread.setName("UIA")
        uia_thread.start()
        uia_thread.join()

        try:
            # 返回结果应该是"prefix:result"格式
            result: UIAResult = result_queue.get(timeout=5)
        except Exception as e:
            raise Exception(f"无法接收到到UIA线程结果信息: {e}")
        if result.is_exception is True:
            raise Exception(f"UIA线程执行出现异常:{result.result}")
        else:
            return result.result

    return wrapper


class SelectorParam:
    """表达式中的属性"""

    Selector = "selector"
    Win = "win"
    ControlTypeID = "ControlTypeID"
    ControlType = "ControlType"
    Index = "Index"
    Name = "Name"
    Aid = "aid"


def check_cef_send_message(control, next_selector: dict):
    """检查是否内嵌cef，并发送win32消息"""
    try:
        # 内嵌CEF发送消息，win32con.WM_GETOBJECT=61
        automation.Win32API.SendMessage(control.Handle, 61, 0, 1)
        # 给指定子控件发送消息
        if next_selector:
            index = int(next_selector.get(SelectorParam.Index, 1))
            child_control = control.GetChildren()[index - 1]
            automation.Win32API.SendMessage(child_control.Handle, 61, 0, 1)
    except Exception as ex:
        ILoger.warning(
            f"{control.ClassName} {hex(control.Handle)} {next_selector} {ex}")


@alternative_thread_mode
def get_element_rectangle(win_class=None, win_name=None, selector=None,
                          search_depth=2, waitfor=WAIT_FOR, result_q=None):
    """
    返回: ( left, top, right, bottom )  (设计器无组件对应)
    """
    __arguments = locals()
    try:
        automation.SetGlobalSearchTimeOut(waitfor)
        global RPA_TIMEOUT
        RPA_TIMEOUT = waitfor

        Window.activate_by_title(win_name, waitfor=waitfor)

        ctrl = get_control(win_class, win_name, selector, search_depth)
        if result_q is not None:
            result_q.put(UIAResult(False, ctrl.BoundingRectangle))
        return ctrl.BoundingRectangle
    except Exception as e:
        if result_q is not None:
            result_q.put(UIAResult(True, str(e)))
            return
        ILoger.error(e, __arguments)
        raise e


@alternative_thread_mode
def do_moveto(win_class=None, win_name=None, selector=None, curson='center',
              offsetX=0, offsetY=0, search_depth=2, waitfor=WAIT_FOR,
              result_q=None, dpi=False):
    """
    鼠标移动

    :param win_class: 类名
    :param win_name: 标题
    :param selector: 路径
    :param curson: 点击位置
    :param offsetX: X轴偏移
    :param offsetY: Y轴偏移
    :param search_depth: 搜索等级
    :param waitfor: 最大超时
    :param result_q: 队列 (内部参数, 不对外暴露)
    :param dpi: 是否缩放
    :return:
    """
    __arguments = locals()
    try:
        automation.SetGlobalSearchTimeOut(waitfor)
        global RPA_TIMEOUT
        RPA_TIMEOUT = waitfor
        Window.activate_by_title(win_name, waitfor=waitfor)

        ctrl = get_control(win_class, win_name, selector, search_depth)

        if dpi and not Platform.ignore_rate():
            scale_rate = get_screen_scale_rate()
            offsetX = int(offsetX * scale_rate)
            offsetY = int(offsetY * scale_rate)

        ratioX, ratioY = get_pos_ratio(curson, offsetX, offsetY)

        ctrl.MoveCursor(ratioX, ratioY)
        if result_q is not None:
            result_q.put(UIAResult(False, UIAResult.Success))
    except Exception as e:
        if result_q is not None:
            result_q.put(UIAResult(True, str(e)))
            return
        ILoger.error(e, __arguments)
        raise e


@alternative_thread_mode
def get_text(win_class=None, win_name=None, selector=None, return_field='value',
             search_depth=2, waitfor=WAIT_FOR, result_q=None):
    """
    获取文本

    :param win_class: 类名
    :param win_name: 标题
    :param selector:路径
    :param return_field: 返回值   值/名称
    :param search_depth: 搜索等级
    :param waitfor: 最大超时
    :param result_q: 队列 (内部参数, 不对外暴露)
    :return:
    """
    __arguments = locals()
    try:
        automation.SetGlobalSearchTimeOut(waitfor)
        global RPA_TIMEOUT
        RPA_TIMEOUT = waitfor
        ctrl = get_control(win_class, win_name, selector, search_depth)

        ctrl = automation.Control.CreateControlFromControl(ctrl)
        ret_value = ctrl.AccessibleCurrentValue()
        ret_name = ctrl.AccessibleCurrentName()
        if return_field == "value":
            ret = ret_value
            if not ret and ret_name:
                ILoger.info(f"尝试设置【目标属性-返回值-名称】获取文本：[{ret_name}]")
        else:
            ret = ret_name
            if not ret and ret_value:
                ILoger.info(f"尝试设置【目标属性-返回值-值】获取文本：[{ret_name}]")
        if result_q is not None:
            result_q.put(UIAResult(False, ret))
            return
        return ret
    except Exception as e:
        if result_q is not None:
            result_q.put(UIAResult(True, str(e)))
            return
        ILoger.error(e, __arguments)
        raise e


@alternative_thread_mode
def set_text(win_class=None, win_name=None, selector=None, text=None,
             search_depth=2, waitfor=WAIT_FOR, result_q=None):
    """
    设置文本

    :param win_class: 类名
    :param win_name: 标题
    :param selector: 路径
    :param text: 需设置的文本
    :param search_depth: 搜索等级
    :param waitfor: 最大超时
    :param result_q: 队列 (内部参数, 不对外暴露)
    :return:
    """
    __arguments = locals()
    try:
        text = encrypt.decrypt(str(text))
        automation.SetGlobalSearchTimeOut(waitfor)
        global RPA_TIMEOUT
        RPA_TIMEOUT = waitfor
        Window.activate_by_title(win_name, waitfor=waitfor)

        ctrl = get_control(win_class, win_name, selector, search_depth)
        ctrl = automation.Control.CreateControlFromControl(ctrl)
        ctrl.SetValue(text)
        if result_q is not None:
            # 线程模式
            result_q.put(UIAResult(False, UIAResult.Success))
    except Exception as e:
        if result_q is not None:
            result_q.put(UIAResult(True, str(e)))
            return
        ILoger.error(e, __arguments)
        raise e


@alternative_thread_mode
def do_check(win_class=None, win_name=None, selector=None, action="check",
             search_depth=2, waitfor=WAIT_FOR, result_q=None):
    """
    设置checkbox的选中状态

    :param win_class: 类名
    :param win_name: 标题
    :param selector: 路径
    :param action: 动作 uncheck / check
    :param search_depth: 搜索等级
    :param waitfor: 最大超时
    :param result_q: 队列 (内部参数, 不对外暴露)
    :return:
    """
    __arguments = locals()
    try:
        automation.SetGlobalSearchTimeOut(waitfor)
        global RPA_TIMEOUT
        RPA_TIMEOUT = waitfor
        Window.activate_by_title(win_name, waitfor=waitfor)

        ctrl = get_control(win_class, win_name, selector, search_depth)
        ctrl = automation.Control.CreateControlFromControl(ctrl)
        state = ctrl.CurrentToggleState()

        ret = None
        if (action == "check" and state == 0) or \
                (action == "uncheck" and state == 1):
            ret = ctrl.Toggle()

        if result_q is not None:
            # 线程模式
            result_q.put(UIAResult(False, ret))
            return
        return ret
    except Exception as e:
        if result_q is not None:
            # 线程模式
            result_q.put(UIAResult(True, str(e)))
            return
        ILoger.error(e, __arguments)
        raise e


def is_checked(win_class=None, win_name=None, selector=None, search_depth=2,
               waitfor=WAIT_FOR):
    """
        是否checked

    :param win_class: 类型
    :param win_name: 名称
    :param selector: 路径
    :param search_depth: 搜索等级
    :param waitfor: 超时
    :return:  勾选状态 返回为True     未勾选状态 返回False
    """
    __arguments = locals()
    ILoger.debug('[is_checked] Start')
    try:
        automation.SetGlobalSearchTimeOut(waitfor)
        global RPA_TIMEOUT
        RPA_TIMEOUT = waitfor
        ctrl = get_control(win_class, win_name, selector, search_depth)
        ctrl = automation.Control.CreateControlFromControl(ctrl)
        state = ctrl.CurrentToggleState()
        # 1是勾选状态   0是未勾选状态   None: 非checkbox类型
        if state is None:
            raise Exception("您选中的元素不是复选框,无法判断状态!")

        return state == 1
    except Exception as e:
        ILoger.error(e, __arguments)
        raise e
    finally:
        ILoger.debug('[is_checked] End')


@alternative_thread_mode
def get_selected_item(win_class=None, win_name=None, selector=None,
                      search_depth=2, waitfor=WAIT_FOR, result_q=None):
    """
    获取select当前选择项 (设计器无组件对应)

    :param win_class: 类型
    :param win_name:名称
    :param selector:路径
    :param search_depth:搜索等级
    :param waitfor: 超时
    :param result_q: 队列 (内部参数, 不对外暴露)
    :return:
    """
    __arguments = locals()
    try:
        automation.SetGlobalSearchTimeOut(waitfor)
        global RPA_TIMEOUT
        RPA_TIMEOUT = waitfor
        Window.activate_by_title(win_name, waitfor=waitfor)

        ctrl = get_control(win_class, win_name, selector, search_depth)
        ctrl = automation.Control.CreateControlFromControl(ctrl)
        if result_q is not None:
            # 线程模式
            result_q.put(UIAResult(False, ctrl.CurrentValue()))
            return
        return ctrl.CurrentValue()
    except Exception as e:
        if result_q is not None:
            # 线程模式
            result_q.put(UIAResult(True, str(e)))
            return
        ILoger.error(e, __arguments)
        raise e


@alternative_thread_mode
def do_selecte_item(win_class=None, win_name=None, selector=None,
                    select_string=None, search_depth=2, waitfor=WAIT_FOR,
                    result_q=None):
    """
    select项选择

    :param win_class: 类型
    :param win_name:名称
    :param selector:路径
    :param select_string: 需设置的select项值
    :param search_depth:搜索等级
    :param waitfor: 超时
    :param result_q: 队列 (内部参数, 不对外暴露)
    :return:
    """
    __arguments = locals()
    try:
        automation.SetGlobalSearchTimeOut(waitfor)
        global RPA_TIMEOUT
        RPA_TIMEOUT = waitfor
        Window.activate_by_title(win_name, waitfor=waitfor)

        ctrl = get_control(win_class, win_name, selector, search_depth)
        ctrl = automation.Control.CreateControlFromControl(ctrl)
        ctrl.Select(select_string)
        if result_q is not None:
            # 线程模式
            result_q.put(UIAResult(False, UIAResult.Success))
    except Exception as e:
        if result_q is not None:
            # 线程模式
            result_q.put(UIAResult(True, str(e)))
            return
        ILoger.error(e, __arguments)
        raise e


def do_get_pos(left=None, top=None, width=None, height=None, curson='center',
               offsetX=0, offsetY=0):
    cursor_x = None
    cursor_y = None
    curs = str(curson).lower()
    try:
        if curs == "center":
            cursor_x = left + width / 2 + offsetX
            cursor_y = top + height / 2 + offsetY
        elif curs == "lefttop":
            cursor_x = left + offsetX
            cursor_y = top + offsetY
        elif curs == "righttop":
            cursor_x = left + width + offsetX
            cursor_y = top + offsetY
        elif curs == "leftbottom":
            cursor_x = left + offsetX
            cursor_y = top + height + offsetY
        elif curs == "rightbottom":
            cursor_x = left + width + offsetX
            cursor_y = top + height + offsetY
        else:
            raise Exception("未知模式, 请您重新选择!")
        return cursor_x, cursor_y
    except Exception as e:
        ILoger.error(e)
        raise e


def do_click_element(win_class=None, win_name=None, selector=None,
                     search_depth=2, continue_on_error='break',
                     waitfor=WAIT_FOR):
    """
    鼠标点击 内部方法
    """
    ctrl = None
    try:
        automation.SetGlobalSearchTimeOut(waitfor)
        global RPA_TIMEOUT
        RPA_TIMEOUT = waitfor
        is_window: ISWindow = Window.activate_by_title(
            win_name, win_class=win_class, waitfor=waitfor,
            search_depth=search_depth)

        win_title = is_window.title if is_window else win_name
        ctrl = get_control(win_class, win_title, selector, search_depth)
        ctrl = automation.Control.CreateControlFromControl(ctrl)
        ctrl.SetFocus()

        if isinstance(ctrl, automation.CheckBoxControl):
            ctrl.Toggle()
            return

        do_click_element_msg(ctrl)

        if isinstance(ctrl, automation.InvokePattern) and ctrl.IsInvokePatternAvailable():
            ctrl.Invoke()

    except Exception as e:
        ILoger.error(e)

        if continue_on_error == "continue":
            ILoger.debug("没有找到可点击元素，尝试点击上一层")
            try:
                parent_ctrl = ctrl.GetParentControl()
                do_click_element_msg(parent_ctrl)
                if isinstance(parent_ctrl, automation.InvokePattern) and parent_ctrl.IsInvokePatternAvailable():
                    parent_ctrl.Invoke()
            except Exception as e:
                ILoger.debug(f"点击上一层同样失败，忽略错误继续运行: {e}")
        else:
            raise e


def do_click_element_msg(control):
    lparam = control.Handle
    automation.Win32API.PostMessage(lparam, 0x0201, 1, 0)
    automation.Win32API.PostMessage(lparam, 0x0202, 1, 0)


def do_click(win_class=None, win_name=None, selector=None, button='left',
             curson='center', offsetX=0, offsetY=0, times=1, search_depth=2,
             continue_on_error='break', waitfor=WAIT_FOR, run_mode='unctrl',
             result_q=None, dpi=False):
    """
    鼠标点击

    :param win_class: 类名
    :param win_name: 标题
    :param selector: 路径
    :param button: 鼠标按键
    :param curson: 点击位置
    :param offsetX: X轴偏移
    :param offsetY: Y轴偏移
    :param times: 按键次数
    :param search_depth: 搜索等级
    :param continue_on_error: 是否继续执行,默认为break,如果为continue,则不会抛出异常
    :param waitfor: 最大超时
    :param run_mode: 执行模式 ctrl: 消息模式(后台操作)   unctrl: 非消息模式(界面操作)
    :param result_q: 队列 (内部参数, 不对外暴露)
    :param dpi: 是否缩放
    :return:
    """
    __arguments = locals()
    start_time = time.time()
    try:
        while True:
            try:
                automation.SetGlobalSearchTimeOut(waitfor)
                global RPA_TIMEOUT
                RPA_TIMEOUT = waitfor

                if run_mode == 'ctrl':
                    return do_click_element(win_class=win_class,
                                            win_name=win_name,
                                            selector=selector,
                                            search_depth=search_depth,
                                            continue_on_error=continue_on_error)

                is_window: ISWindow = Window.activate_by_title(
                    win_name, win_class=win_class, waitfor=waitfor)

                win_title = is_window.title if is_window else win_name
                ctrl = get_control(win_class, win_title, selector, search_depth)

                if run_mode == 'unctrl':
                    if dpi and not Platform.ignore_rate():
                        scale_rate = get_screen_scale_rate()
                        offsetX = int(offsetX * scale_rate)
                        offsetY = int(offsetY * scale_rate)

                    ratioX, ratioY = get_pos_ratio(curson, offsetX, offsetY)
                    if button == 'left':
                        if times == 1:
                            ctrl.Click(ratioX, ratioY)
                        else:
                            ctrl.DoubleClick(ratioX, ratioY)
                    elif button == 'right':
                        ctrl.RightClick(ratioX, ratioY)
                    elif button == 'middle':
                        ctrl.MiddleClick(ratioX, ratioY)
                return
            except Exception as e:
                run_time = time.time() - start_time
                if run_time >= waitfor:
                    ILoger.error(e, __arguments)
                    raise e
                else:
                    ILoger.debug(f'Attempt Failure - Wait for Attempt: {e}')
                    time.sleep(TRY_INTERVAL)
    except Exception as e:
        ILoger.error(e, __arguments)
        if continue_on_error == "continue":
            return
        else:
            raise e


def get_pos_ratio(curson='center', offsetX=0, offsetY=0):
    # 如果是小数的话,则以百分比来算
    if isinstance(offsetX, float) and isinstance(offsetY, float):
        ratio_x = offsetX
        ratio_y = offsetY
    else:
        ratio_x = round(offsetX)
        ratio_y = round(offsetY)

    if curson == 'center':
        ratio_x = 0.5
        ratio_y = 0.5
    elif curson == 'lefttop':
        ratio_x = offsetX
        ratio_y = offsetY
    elif curson == 'rightbottom':
        if offsetX == 0:
            ratio_x = -1
        else:
            ratio_x = 0 - offsetX

        if offsetY == 0:
            ratio_y = -1
        else:
            ratio_y = 0 - offsetY
    return ratio_x, ratio_y


def get_win_control(win_class=None, win_name=None, search_depth=2):
    try:
        kwargs = {"searchDepth": search_depth}
        if win_class:
            kwargs["ClassName"] = win_class
        if win_name:
            kwargs["SubName"] = win_name
        wind = automation.Control(**kwargs)
        global RPA_TIMEOUT
        if not wind.Exists(RPA_TIMEOUT):
            raise WinNotFoundError("根据类名与标题, 超时未找到对应程序.")
        return wind
    except Exception as e:
        raise e


def get_control(win_class=None, win_name=None, selector=None, search_depth=2):
    try:
        win = get_win_control(win_class, win_name, search_depth)
        selectors: list = selector.get(SelectorParam.Selector, [])
        if not selectors:
            # 无路径，直接返回窗口control
            return win
        if len(selectors) == 1:  # 如果只有一选项，而且只有名字
            _selector: dict = selectors[0]
            name = _selector.get(SelectorParam.Name, "")
            control_type = int(
                _selector.get(SelectorParam.ControlTypeID, "0"), 16)
            index = int(_selector.get(SelectorParam.Index, 1))

            if name and not control_type:
                # 直接按照窗口标题名字查找
                return get_control_by_name(win, name, index)
        return get_last_control(win, selectors)
    except Exception as e:
        ILoger.error(e)
        raise e


def get_last_control(win_control, selectors: list):
    """从后往前逐步获取ctrl"""
    try:
        ctrl = win_control
        check_cef_send_message(ctrl, selectors[-1])
        for i, _selector in enumerate(reversed(selectors)):
            ctrl = get_one_control(ctrl, _selector)
            next_selector = selectors[-2 - i] if i + 1 < len(selectors) else {}
            check_cef_send_message(ctrl, next_selector)
        return ctrl
    except Exception as e:
        raise e


def get_one_control(control, selector):
    try:
        name = selector.get(SelectorParam.Name, "")
        # 16进制转10进制
        control_type = int(selector.get(SelectorParam.ControlTypeID, "0"), 16)
        index = int(selector.get(SelectorParam.Index, 1))

        if not name and not control_type:
            raise Exception('ui parameter cannot be all null')

        kwargs = {
            "searchFromControl": control,
            "foundIndex": index,
            "searchDepth": 1,
        }
        if name:
            kwargs["SubName"] = name
        if control_type:
            kwargs["ControlType"] = control_type
        return automation.Control(**kwargs)
    except Exception as e:
        raise e


def get_control_by_name(control, name, foundIndex=1):
    try:
        ctrl = automation.Control(searchFromControl=control, SubName=name,
                                  foundIndex=foundIndex)
        return ctrl
    except Exception as e:
        ILoger.error(e)
        raise e


@alternative_thread_mode
def get_element_rect(win_class=None, win_name=None, selector=None,
                     curson='lefttop', offsetX=0, offsetY=0, search_depth=2,
                     result_q=None, waitfor=WAIT_FOR):
    """
    获取元素位置

    :param win_class: 类名
    :param win_name: 标题
    :param selector: 路径
    :param curson: 点击位置
    :param offsetX: X轴偏移
    :param offsetY: Y轴偏移
    :param search_depth: 搜索等级
    :param result_q: 队列 (内部参数, 不对外暴露)
    :param waitfor: 最大超时
    :return:  (cursor_x, cursor_y, width, height)
    """
    __arguments = locals()
    try:
        automation.SetGlobalSearchTimeOut(waitfor)
        global RPA_TIMEOUT
        RPA_TIMEOUT = waitfor
        Window.activate_by_title(win_name, waitfor=waitfor)

        ctrl = get_control(win_class, win_name, selector, search_depth)
        left, top, right, bottom = ctrl.BoundingRectangle
        width = right - left
        height = bottom - top

        if curson:
            left, top = do_get_pos(left, top, width, height, curson=curson,
                                   offsetX=offsetX, offsetY=offsetY)

        if result_q is not None:
            # 线程模式
            result_q.put(UIAResult(False, (left, top, width, height)))
            return
        return left, top, width, height
    except Exception as e:
        if result_q is not None:
            # 线程模式
            result_q.put(UIAResult(True, str(e)))
            return
        ILoger.error(e, __arguments)
        raise e


def is_element_existed_in_uia(win_class=None, win_name=None, selector=None,
                              curson='lefttop', offsetX=0, offsetY=0,
                              search_depth=2, waitfor=WAIT_FOR):
    """
    元素是否存在

    :param win_class: 类名
    :param win_name: 标题
    :param selector: 路径
    :param curson: 点击位置
    :param offsetX: X轴偏移
    :param offsetY: Y轴偏移
    :param search_depth: 搜索等级
    :param waitfor: 最大超时
    :return: 是否存在
    """
    __arguments = locals()
    ILoger.debug("[is_element_existed_in_uia] Start")
    try:
        get_element_rect(win_class=win_class, win_name=win_name,
                         selector=selector, curson=curson,
                         offsetX=offsetX, offsetY=offsetY,
                         search_depth=search_depth, waitfor=waitfor)
        ILoger.debug("[is_element_existed_in_uia] Found")
        return True
    except Exception as e:
        ILoger.debug(f"[is_element_existed_in_uia] Not found: {e}")
        return False


def capture_element_img(win_class=None, win_name=None, selector=None,
                        in_img_path=None, in_img_name=None,
                        search_depth=2, waitfor=WAIT_FOR):
    """
    元素截图

    :param win_class: 类名
    :param win_name: 标题
    :param selector: 路径
    :param in_img_path: 指定图片保存目录
    :param in_img_name: 指定图片名称
    :param search_depth: 搜索等级
    :param waitfor: 最大超时
    :return:
    """
    __arguments = locals()
    try:
        x, y, width, height = get_element_rect(
            win_class=win_class, win_name=win_name, selector=selector,
            curson='lefttop', search_depth=search_depth)

        in_img_path = img.capture_image(win_title=win_name, win_text='',
                                        in_img_path=in_img_path,
                                        in_img_name=in_img_name,
                                        left_indent=x,
                                        top_indent=y,
                                        width=width, height=height,
                                        waitfor=waitfor)
        return in_img_path
    except Exception as e:
        ILoger.error(e, __arguments)
        raise e


def match_text(win_class=None, win_name=None, selector=None,
               return_field='value', search_depth=2, mtext=None,
               waitfor=WAIT_FOR):
    """
    是否包含文本

    :param win_class: 窗口类
    :param win_name: 窗口标题
    :param selector: 元素信息
    :param return_field: 返回值
    :param search_depth: 搜索等级
    :param mtext: 匹配文本
    :param waitfor: 等待时间
    :return: True / False
    """
    __arguments = locals()
    try:
        start_time = time.time()
        while True:
            text = get_text(win_class=win_class, win_name=win_name,
                            selector=selector, return_field=return_field,
                            search_depth=search_depth, waitfor=WAIT_FOR)
            if str(mtext) in str(text):
                return True
            else:
                ILoger.debug(f"[{mtext}] 未匹配获取的文本 [{text}]")
                runtime = time.time() - start_time
                if runtime >= waitfor:
                    return False
                time.sleep(TRY_INTERVAL)
    except Exception as e:
        ILoger.error(e, __arguments)
        raise e


def click_ocr_text(win_class=None, win_name=None, selector=None,
                   button='left', curson='center', offsetX=0,
                   offsetY=0, times=1, search_depth=2,
                   continue_on_error='break',
                   target_text="", rule="contain", target_index=1,
                   ocr_engine=0, apiKey="", secretKey="",
                   waitfor=30,
                   img_res_path=None):
    """
        点击ocr文本

    :param win_class: 窗口类
    :param win_name: 窗口标题
    :param selector: 元素信息
    :param button: 鼠标按键
    :param curson: 点击位置
    :param offsetX: X轴偏移
    :param offsetY: Y轴偏移
    :param times: 点击次数
    :param search_depth: 搜素等级
    :param continue_on_error:  异常时继续  continue / break
    :param target_text: 目标文本
    :param rule: 匹配规则, contain / equal
    :param target_index: 索引
    :param ocr_engine: 搜素引擎   互联网 / 私有化
    :param apiKey: (已弃用参数)
    :param secretKey: (已弃用参数)
    :param waitfor: 超时
    :param img_res_path:
    :return:
    """
    __arguments = locals()

    def capture_and_recognize(x, y, _width, _height) -> list:
        """截图并识别图片内文本"""
        img_path = img.capture_image(win_title=win_name, win_text='',
                                     in_img_path=None, in_img_name=None,
                                     left_indent=x, top_indent=y,
                                     width=_width, height=_height,
                                     waitfor=waitfor)
        try:
            ocr_result = iocr.general_pos_recognize(
                image_path=img_path, apiKey=apiKey,
                secretKey=secretKey, ocr_engine=ocr_engine)
            return ocr_result
        except Exception as e:
            raise Exception(f"识别结果为空 {e}")
        finally:
            os.remove(img_path)

    def match_data(_ocr_result):
        """按规则匹配数据"""
        contain_list, equal_list = [], []
        for i in _ocr_result:
            if target_text in i["words"]:
                contain_list.append(i)
            if target_text == i["words"]:
                equal_list.append(i)
        return contain_list if rule == "contain" else equal_list

    def text_inner_pos(_target_list):
        """获取文本在区域内的坐标，支持偏移量"""
        inner_x = None
        inner_y = None
        if len(_target_list) >= target_index:
            inner_pos: dict = _target_list[target_index - 1]['location']
            inner_x, inner_y = do_get_pos(left=inner_pos["left"],
                                          top=inner_pos["top"],
                                          width=inner_pos["width"],
                                          height=inner_pos["height"],
                                          curson=curson,
                                          offsetX=offsetX,
                                          offsetY=offsetY)
        else:
            raise Exception(
                f"符合规则{len(_target_list)}条 小于 目标位置{target_index}")
        if inner_x is None and inner_y is None:
            raise Exception("无可用目标")
        return inner_x, inner_y

    start_time = time.time()
    try:
        if not target_text:
            raise Exception("请填写 目标文本")

        if isinstance(target_index, int):
            if target_index <= 0:
                raise Exception("目标索引 应大于或等于1")
        else:
            raise Exception("目标索引 应为int类型")

        if times <= 0:
            raise Exception("按键次数应大于或等于1")

        while True:
            try:
                automation.SetGlobalSearchTimeOut(waitfor)
                global RPA_TIMEOUT
                RPA_TIMEOUT = waitfor
                Window.activate_by_title(win_name, waitfor=waitfor)
                # 按区域截图并ocr识别出文本
                cursor_x, cursor_y, width, height = get_element_rect(
                    win_class=win_class, win_name=win_name,
                    selector=selector, curson='lefttop',
                    search_depth=search_depth, waitfor=waitfor)
                ocr_result = capture_and_recognize(
                    cursor_x, cursor_y, width, height)
                target_list = match_data(ocr_result)
                crd = [(i, v["words"])
                       for i, v in enumerate(target_list, start=1)]
                ILoger.info(f"符合{rule}规则的数据 {crd}")
                # 图片内的文本坐标
                inner_x, inner_y = text_inner_pos(target_list)
                # 点击坐标
                ics._mouse_click_cs(button=button, x=cursor_x + inner_x,
                                    y=cursor_y + inner_y, mode=None,
                                    times=times)
                return True
            except Exception as e:
                run_time = time.time() - start_time
                if run_time >= waitfor:
                    ILoger.error(e, __arguments)
                    raise e
                else:
                    ILoger.debug(f'Attempt Failure - Wait for Attempt: {e}')
                    time.sleep(TRY_INTERVAL)
    except Exception as e:
        ILoger.error(e, __arguments)
        if continue_on_error == "continue":
            return
        else:
            raise e


def get_structData(win_class=None, win_name=None, selector=None,
                   columns_setting=None, max_limit=500, waitfor=WAIT_FOR):
    """
        结构化数据抓取, 只实现表格的数据抓取,而且没有翻页功能

    :param win_class: 类
    :param win_name: 标题
    :param selector: 元素信息
    :param columns_setting: 列设置
    :param max_limit: 限制大小
    :param waitfor: 翻页的等待超时
    :return: 抓取的表格数据(dataFrame)
    """
    __arguments = locals()
    ILoger.debug('[get_structData] Start')
    try:
        # 需要先声明变量拷贝，不可直接使用
        InitInstance = uia_client_dll.InitInstance
        ReleaseInstance = uia_client_dll.ReleaseInstance
        getStructTableData = uia_client_dll.getStructTableData
        getStructTableData.restype = c_wchar_p
        getStructTableData.argtypes = [c_wchar_p, c_wchar_p, c_wchar_p]

        InitInstance()
        data_rows = 0  # 已经获取到的数据行数
        dataframe = None  # 最终返回的dataFrame

        start_time = time.time()
        is_table = True
        while True:
            result = getStructTableData(
                win_name, win_class, json.dumps(selector, ensure_ascii=False))
            return_data: dict = json.loads(result)
            ret_code = return_data.get("retCode", "getExtractData未返回retCode")
            ret_error = return_data.get("retError", "getExtractData未返回retError")
            if ret_code == 1:
                data = return_data.get("retData", {}).get("extractDatas", [])
                # 单次获取到的dataframe
                dataframe = __extract_analytical_data(
                    data, is_table, columns_setting)
                data_rows = dataframe.shape[0]
                ILoger.info(f"截至本次运行, data_rows行数是: {data_rows}")
                dataframe = dataframe[0: max_limit]
                break
            else:
                runtime = time.time() - start_time
                if runtime >= waitfor / 1000:
                    raise Exception(f"执行结构化数据抓取操作时, 发生错误: {ret_error}")
                time.sleep(2)
        return dataframe
    except Exception as e:
        ILoger.error(e, __arguments)
        raise e
    finally:
        ReleaseInstance()
        ILoger.debug('[get_structData] End')


def __extract_analytical_data(
        row_data: dict, is_table: bool, columns_settings: list):
    """按表格设置（列名、列属性）解析数据
    row_data 有序行数据 示例数据（文件目录）
    [{
        '大小': {'attrs': ['text'], 'index': 3, 'values': ['']},
        '类型': {'attrs': ['text'], 'index': 2, 'values': ['文件夹']},
        '名称': {'attrs': ['text'], 'index': 0, 'values': ['Windows 系统']},
        '修改日期': {'attrs': ['text'], 'index': 1, 'values': ['2022/4/1 18:33']}
    },...]
    columns_settings 有序列名 示例数据（文件目录）
    [{
        "DataType": "text", "IsTable": 1, "IsVisible": 1, "Name": "名称New",
        "ReferenceName": "名称", "Value": "7-Zip", "attr": "text"
    },...]"""
    # 列的设置，新的名称、列数据类型
    org_new_column_names = {}  # 原名称和新名称map
    datetime_columns = {}  # 日期时间类型列
    number_columns = {}  # 数字类型列
    string_columns = {}  # 字符串类型列，无需转换
    for setting in columns_settings:
        if setting["IsVisible"] == 0:
            # 跳过隐藏列
            continue
        # 列的原名称和用户指定的新名称
        org_column_name = setting["ReferenceName"]
        new_column_name = setting["Name"]
        org_new_column_names[org_column_name] = new_column_name
        # 用户设定的列属性：text（默认）、date（日期）、int（数字）
        attr = setting["attr"]
        if attr == "date":
            datetime_columns[org_column_name] = setting["DateFormat"]
        elif attr == "int":
            # 数字分为int和float
            number_columns[org_column_name] = setting["NumType"]
        elif attr == "text":
            string_columns[org_column_name] = setting["DataType"]
        else:
            raise Exception("目前只支持text,date,int格式")

    # 保留[列设置]中的列
    df = pd.DataFrame(row_data)[org_new_column_names.keys()]
    # 按列提取值
    for column in org_new_column_names.keys():
        df[column] = df[column].apply(lambda r: r["values"][0])

    def to_datetime(_cell, _column):
        """单元格数据转为日期格式"""
        date_format = datetime_columns[_column]
        try:
            try:
                dt = datetime.strptime(str(_cell), format=date_format)
            except:
                dt = dateutil.parser.parse(_cell)
            if isinstance(dt, datetime):
                # 相关bug  9351  10477
                # 如果是1900或1970年，则改为当前年份。
                if ("%Y" not in date_format) and (dt.year in [1900, 1970]):
                    dt.replace(year=datetime.now().year)
            _cell = pd.to_datetime(dt, errors="raise")
        except Exception as e:
            pass
        return _cell

    # 转换日期格式的值
    for dt_col in datetime_columns:
        df[dt_col] = df[dt_col].apply(lambda cell: to_datetime(cell, dt_col))

    def to_number(_cell, _column):
        number_type = number_columns[_column]
        try:
            _cell = float(_cell)
            if number_type == "int":
                _cell = int(_cell)
        except Exception as e:
            pass
        return _cell

    # 转换日期格式的值
    for num_col in number_columns:
        df[num_col] = df[num_col].apply(lambda cell: to_number(cell, num_col))

    # 列名重命名
    df.rename(columns=org_new_column_names, inplace=True)
    return df
