# coding: utf8
"""
控制台类对象，包含：平台服务器端、机器人端、控制器监控端、等
"""

from typing import Any

from ubpa import iplatform
from ubpa.iobject.element import Action


class Server:
    """平台服务器"""

    class Owner:
        """服务端文件所有者"""
        user = iplatform.EnumUpType.User  # 个人
        proc = iplatform.EnumUpType.Proc  # 流程

    def __init__(self, robot_no="", job_no="", proc_no=""):
        """
        实例化
        示例：
            Server()   # 空信息实例化可以运行，但无法与服务端交互

            # 手动使用服务端信息实例化，机器人mac地址，作业uuid，项目名称
            Server(
                "B0-7B-25-18-25-B8",
                "ce3d1e4f-085a-42f4-9d4c-c985d3446b7a",
                "NewProject1")

            # 设计器流程中运行使用，注意：第三方编辑器调试时无法使用此方法
            Server(self.robot_no, self.job_no, self.proc_no)
        :param robot_no: 机器人编号，设计器运行默认空
        :param job_no: 作业编号，默认空
        :param proc_no: 流程项目编号（项目名称，如：NewProject1），默认空
        """
        self.robot_no = robot_no
        self.job_no = job_no
        self.proc_no = proc_no

    def set_var(self, name, value, wait_seconds: int = Action.WaitSeconds):
        """
        设置变量
        示例：
            Server().get_var("变量名称", "变量的值（不局限于字符串类型值）")
        :param name: 变量名称
        :param value: 变量值
        :param wait_seconds: 等待时间秒数，默认3秒
        :return: 设置结果
        """
        return iplatform.setAsset(
            name=name,
            value=value,
            timeout=wait_seconds,
            robot_no=self.robot_no,
            job_no=self.job_no,
            proc_no=self.proc_no
        )

    def get_var(self, name, wait_seconds: int = Action.WaitSeconds) -> Any:
        """
        获取变量
        示例：
            Server().get_var("变量名称")
        :param name: 变量名称
        :param wait_seconds: 等待时间秒数，默认3秒
        :return: 变量值
        """
        return iplatform.getAsset(
            name=name,
            timeout=wait_seconds,
            robot_no=self.robot_no,
            job_no=self.job_no,
            proc_no=self.proc_no
        )

    def delete_file(self, name="", owner=Owner.proc,
                    wait_seconds: int = Action.WaitSeconds) -> bool:
        """
        删除文件
        示例：
            Server().delete_file("a.txt", Owner.user)   # 删除服务端用户a.txt文件
        :param name: 服务端文件名称（含文件格式）
        :param owner: 文件所有者，流程proc、用户user，默认proc
        :param wait_seconds: 等待时间秒数，默认3秒
        :return:
        """
        return iplatform.delete_file_v2(
            file_name=name,
            up_type=owner,
            timeout=wait_seconds,
            robot_no=self.robot_no,
            job_no=self.job_no,
            proc_no=self.proc_no
        )
