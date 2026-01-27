# coding: utf8
"""
办公软件类，包含：Excel、Word、PDF、Email、等
"""
import os
from pathlib import Path, PurePath
from typing import Any

from ubpa import iexcel, iexchange, imail, ioutlook


class _DataType:
    none = None
    string = "string"
    int = "int"
    float = "float"
    time = "time"  # 日期时间格式，datetime


class _Sheet:
    """工作表"""

    def __init__(self, excel=None, sheet: [str, int] = 0):
        self.excel: (Excel, None) = excel
        self.sheet = sheet

    def create(self, name: [str, int, None] = None,
               before: [str, int, None] = None):
        """
        创建工作表
        示例：
            # 在当前sheet前面创建一个新的工作表
            Excel().Sheet().create()
            # 在当前sheet前面创建一个名为test的工作表
            Excel().Sheet().create('test')
            # 在紧邻第1个sheet的后面创建一个新的工作表
            Excel().Sheet().create(before=1)
            # 在紧邻Sheet1的后面创建一个新的工作表
            Excel().Sheet().create(before='Sheet1')
            # 在紧邻第1个sheet的后面创建一个名为test的工作表
            Excel().Sheet().create('test', 1)
        :param name: 新建工作表的名称，默认值为None
        :param before: 紧邻新建工作表的前一个工作表，可以是整型数或者已存在的工作表名
        :return: 新建工作表的名称
        """
        return iexcel.creat_sheet(
            path=self.excel.file_path,
            sheet=name,
            before=before,
            file_type=self.excel.open_type
        )


class _Row:
    """行"""

    def __init__(self, excel=None, sheet: [str, int] = 0):
        self.excel: (Excel, None) = excel
        self.sheet = sheet

    def write(self, text: Any, cell: str = "A1"):
        """
        写入内容到行
        实例：
            # 从默认单元格A1开始，在行中单元格依次写入1,2,3
            Excel().Row().write([1,2,3])

            # 从指定单元格B2开始，在行中单元格依次写入1,2,3
            Excel().Row().write([1,2,3], "B2")
        :param text: 写入内容，支持字符串、列表、元组、
            pandas.DataFrame、其他可迭代数据（不含字典）
        :param cell: 写入行的起始单元格，默认为A1
        :return:
        """
        iexcel.write_row(
            path=self.excel.file_path,
            text=text,
            sheet=self.sheet,
            cell=cell,
            file_type=self.excel.open_type
        )

    def read(self, cell: str = "A1") -> Any:
        """
        读取行内容
        示例：
            Excel().Row().read()            # 从默认单元格A1开始读取该行内容
            Excel().Row().read("A2")        # 从指定单元格A2开始读取该行内容
        :param cell: 读取行的起始单元格，默认为A1
        :return: 该行的所有值,返回类型为list
        """
        return iexcel.read_row(
            path=self.excel.file_path,
            sheet=self.sheet,
            cell=cell
        )

    def insert(self, text: Any, cell: str = "A1"):
        """
        插入行
        示例：
            # 在默认单元格A1所在行插入新的一行，并从A1开始依次写入1,2,3
            Excel().Row().insert([1,2,3])

            # 在指定单元格A2所在行插入新的一行，并从A2开始依次写入1,2,3
            Excel().Row().insert([1,2,3], "A2")
        :param text: 插入行时写入的内容，支持字符串、列表、元组、其他可迭代数据（不含字典）
        :param cell: 插入行时数据写入的起始单元格，默认为A1
        :return: 无
        """
        iexcel.ins_row(
            path=self.excel.file_path,
            sheet=self.sheet,
            cell=cell,
            data=text,
            file_type=self.excel.open_type
        )

    def delete(self, cell: str = "A1"):
        """
        删除单元格所在的行
        示例：
            Excel().Row().delete()          # 删除默认单元格A1所在的行
            Excel().Row().delete("A2")      # 删除指定单元格A2所在的行
        :param cell: 删除指定单元格所在的行，默认为A1
        :return: 无
        """
        iexcel.delete_row(
            path=self.excel.file_path,
            sheet=self.sheet,
            cell=cell,
            file_type=self.excel.open_type
        )

    def count(self):
        """
        工作表行数读取
        示例：
            Excel().Row().count()       # 读取当前工作表的行数
        :return: 当前工作表的行数
        """
        return iexcel.get_rows_count(
            path=self.excel.file_path,
            sheet=self.sheet
        )


class _Column:
    """列"""
    DataType = _DataType

    def __init__(self, excel=None, sheet: [str, int] = 0):
        self.excel: (Excel, None) = excel
        self.sheet = sheet

    def write(self, text: Any, cell: str = "A1"):
        """
        写入内容到列
        实例：
            # 从默认单元格A1开始，在列中单元格依次写入1,2,3
            Excel().Column().write([1,2,3])

            # 从指定单元格B2开始，在列中单元格依次写入1,2,3
            Excel().Column().write([1,2,3], "B2")
        :param text: 写入内容，支持字符串、列表、元组、pandas.DataFrame、其他可迭代数据（不含字典）
        :param cell: 写入列的起始单元格，默认为A1
        :return: 无
        """
        return iexcel.write_col(
            path=self.excel.file_path,
            text=text,
            sheet=self.sheet,
            cell=cell,
            file_type=self.excel.open_type
        )

    def read(self, cell: str = "A1", as_type=DataType.none) -> Any:
        """
        读取列内容
        示例：
            Excel().Column().read()            # 从默认单元格A1开始读取该列内容
            Excel().Column().read("A2")        # 从指定单元格A2开始读取该列内容
        :param cell: 读取列的起始单元格，默认为A1
        :param as_type: 转换单元格内容作为新的数据类型，string、int、float、time
        :return: 该列的所有值，返回类型为list
        """
        return iexcel.read_col(
            path=self.excel.file_path,
            sheet=self.sheet,
            cell=cell,
            cell_type=as_type
        )


class _Cell:
    """单元格"""
    DataType = _DataType

    def __init__(self, excel=None, sheet: [str, int] = 0):
        self.excel: (Excel, None) = excel
        self.sheet = sheet

    def write(self, text: Any, cell: str = "A1"):
        """
        写入内容到单元格
        示例：
            Excel().Cell().write("abc")         # 在默认单元格A1中写入abc
            Excel().Cell().write("abc","A2")    # 在单元格A2中写入abc
        :param text: 写入内容，支持字符串、列表、元组、pandas.DataFrame、其他可迭代数据（不含字典）
        :param cell: 写入指定的单元格，默认为A1
        :return: 无
        """
        return iexcel.write_cell(
            path=self.excel.file_path,
            text=text,
            sheet=self.sheet,
            cell=cell,
            file_type=self.excel.open_type
        )

    def read(self, cell: str = "A1", as_type=DataType.none) -> Any:
        """
        读取单元格内容
        示例：
            # 读取默认单元格A1中的值，并转换为字符串
            Excel().Cell().read(DataType.string)

            # 读取默认单元格A2中的值，并转换为字符串
            Excel().Cell().read(DataType.string,"A2")
        :param cell: 写入指定的单元格，默认为A1
        :param as_type: 转换单元格内容作为新的数据类型，string、int、float、time
        :return: 单元格内容值
        """
        return iexcel.read_cell(
            path=self.excel.file_path,
            sheet=self.sheet,
            cell=cell,
            cell_type=as_type
        )


class Excel:
    """Excel表格"""

    def __init__(self, file_path: [str, PurePath] = "", open_type="excel"):
        """
        实例化
        示例：
            Excel(".\\test.xlsx")            # 默认excel应用打开
            Excel(".\\test.xlsx", "file")    # file方式打开excel表格
        :param file_path: Excel表格文件路径
        :param open_type: 打开方式：excel或file，默认excel应用打开，或使用file方式打开
        """
        if os.path.isdir(file_path):
            raise Exception('当前路径为文件夹，请输入Excel文件路径')
        self.file_path = file_path
        self.open_type = open_type

    def _must_already_exist(self):
        """表格文件需已存在"""
        if not os.path.exists(self.file_path):
            raise FileNotFoundError(f"表格文件必须已存在 {self.file_path}")

    def create(self):
        """
        创建excel
        案例：
            Excel().create()
        :return: 新建excel文件路径
        """
        file_path = Path(self.file_path)
        return iexcel.create_excel(
            path=file_path.parent,
            file_name=file_path.name
        )

    @classmethod
    def close(cls):
        """
        关闭excel应用
        案例：
            Excel().close()     # 关闭excel应用
        :return:
        """
        return iexcel.close_excel_apps()

    def Sheet(self, sheet: [str, int] = 0) -> _Sheet:
        """
        工作表
        示例：
            Sheet()             # 默认操作当前工作表
            Sheet('Sheet1')     # 操作指定的Sheet1工作表
        :param sheet:
        :return:
        """
        self._must_already_exist()
        return _Sheet(self, sheet)

    def Row(self, sheet: [str, int] = 0) -> _Row:
        """
        行
        示例：
            Row()                       # 默认当前工作表
            Row('Sheet1')               # 指定Sheet1
        :param sheet: 指定工作表，可以是整型数或者字符串，默认为当前工作表
        :return:
        """
        self._must_already_exist()
        return _Row(self, sheet)

    def Column(self, sheet: [str, int] = 0) -> _Column:
        """
        列
        示例：
            Column()                    # 默认当前工作表
            Column('Sheet1')            # 指定Sheet1
        :param sheet: 指定工作表，可以是整型数或者字符串，默认为当前工作表
        :return:
        """
        self._must_already_exist()
        return _Column(self, sheet)

    def Cell(self, sheet: [str, int] = 0) -> _Cell:
        """
        单元格
        示例：
            Cell()                # 默认当前工作表，默认A1单元格
            Cell('Sheet1')        # 指定Sheet1，默认A1单元格
        :param sheet: 指定工作表，可以是整型数或者字符串，默认为当前工作表
        :return:
        """
        self._must_already_exist()
        return _Cell(self, sheet)


class Email:
    """邮件类"""

    class Mail:
        """普通邮件"""

        def __init__(self, server="mail.smtp.com", port=25, sender="",
                     password=""):
            """
            初始化
            示例：
                # 使用默认server、port和ssl，创建自己的邮箱对象
                Email().Mail(sender="123@test.com",password="456")
            :param server: 邮件服务器
            :param port: 服务器端口号
            :param sender: 邮箱账号
            :param password: 对应服务的密码
            :return: 无
            """
            self.server = server
            self.port = port
            self.sender = sender
            self.password = password

        def send(self, receivers="", cc="", bcc="", subject="", content="",
                 attach_files: str = "", ssl='no', method="text"):
            """
            发送邮件
            示例：
                Email().Mail().send(
                    receivers="abc@test.com",cc="cc.test.com",bcc="bcc.test.com",
                    subject="subject_test",content="content_test", ssl="no"
                    method="text", attach_files=r"C:\test1.txt,C:\test2.txt")
            :param receivers: 收件人，多个邮箱英文逗号分隔。
            :param cc: 抄送
            :param bcc: 密送
            :param subject: 邮件主题/标题
            :param content: 邮件正文
            :param attach_files: 附件路径，多个文件英文逗号分隔。
            :param ssl: 是否使用ssl加密，yes/no，默认为no.加密发送使用465端口
            :param method: 发送邮件的格式，html/text，默认为text
            :return:
            """
            imail.send_smtp_mail(
                server=self.server,
                port=self.port,
                sender=self.sender,
                psw=self.password,
                receivers=receivers,
                cc=cc,
                bcc=bcc,
                subject=subject,
                body=content,
                attachments=attach_files,
                ssl=ssl,
                method=method
            )

    class ExchangeMail:
        """exchange邮件"""

        def __init__(self, server="", domain="", username="", password="",
                     sender=""):
            """
            初始化
            示例：
                Email().ExchangeMail(
                    server="192.168.10.20", domain="", username="test_user",
                    password="abc", sender="123@test.com")
            :param server: 服务器地址，例如"192.168.10.20"
            :param domain: AD域名，可不填
            :param username: 用户名
            :param password: 密码
            :param sender: 发件人
            :return:
            """
            self.server = server
            self.domain = domain
            self.username = username
            self.password = password
            self.sender = sender

        def send(self, receivers="", cc="", bcc="", subject="", content="",
                 attach_files="", mail_type="text"):
            """
            发送exchange邮件
            示例：
                Email().ExchangeMail().send(
                    receiver="abc@test.com",cc="cc@test.com",
                    bcc="bcc@test.com",subject="subject_test",
                    content="content_test", mail_type="text"
                    attach_files=r"C:\test1.txt,C:\test2.txt")
            :param receivers: 收件人，多个邮箱英文逗号,分隔。
            :param cc: 抄送
            :param bcc: 密送
            :param subject: 主题
            :param content: 内容
            :param attach_files: 附件文件路径，多个文件英文逗号,分隔。
            :param mail_type: 邮件类型，text/html，默认为text
            :return: 发送成功返回True，否则异常
            """
            return iexchange.send_mail(
                server=self.server,
                domain=self.domain,
                username=self.username,
                password=self.password,
                primary_smtp_address=self.sender,
                receiver=receivers,
                cc=cc,
                bcc=bcc,
                subject=subject,
                content=content,
                attach_files=attach_files,
                mail_type=mail_type,
            )

    class OutlookMail:
        """outlook邮件"""

        @classmethod
        def send(cls, receivers="", cc="", bcc="", subject="", content="",
                 attach_files=""):
            """
            发送outlook邮件
            示例：
                Email().OutlookMail().send(
                    receiver="abc@test.com",cc="cc@test.com",
                    bcc="bcc@test.com",subject="subject_test",
                    content="content_test",
                    attach_files=r"C:\test1.txt,C:\test2.txt")
            :param receivers: 收件人，多个邮箱英文分号;分隔。
            :param cc: 抄送
            :param bcc: 密送
            :param subject: 主题
            :param content: 内容
            :param attach_files: 附件文件路径，多个文件英文逗号分隔。
            :return: 发送成功返回True，否则异常
            """
            return ioutlook.send_outlook(
                receiver=receivers,
                cc=cc,
                bcc=bcc,
                subject=subject,
                body=content,
                attachments=attach_files,
            )
