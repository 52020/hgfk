# coding=utf-8
# 编译日期：2024-03-29 17:55:16
# 版权所有：www.i-search.com.cn
import ubpa.init_input as iinput
from ubpa.base_util import StdOutHook, ExceptionHandler
import ubpa.ics as ics
import ubpa.ichrome_firefox as ichrome_firefox
import ubpa.itools.rpa_time as rpa_time
import ubpa.iimg as iimg
import time
import pdb
from ubpa.ilog import ILog
import getopt
from sys import argv
import sys
import os
from ubpa.base_img import *

class HN_Report_import_data:
     
    def __init__(self,**kwargs):
        self.__logger = ILog(__file__)
        self.path = set_img_res_path(__file__)
        self.robot_no = ''
        self.proc_no = ''
        self.job_no = ''
        self.input_arg = ''
        if('robot_no' in kwargs.keys()):
            self.robot_no = kwargs['robot_no']
        if('proc_no' in kwargs.keys()):
            self.proc_no = kwargs['proc_no']
        if('job_no' in kwargs.keys()):
            self.job_no = kwargs['job_no']
        ILog.JOB_NO, ILog.OLD_STDOUT = self.job_no, sys.stdout
        sys.stdout = StdOutHook(self.job_no, sys.stdout)
        ExceptionHandler.JOB_NO, ExceptionHandler.OLD_STDERR = self.job_no, sys.stderr
        sys.excepthook = ExceptionHandler.handle_exception
        if('input_arg' in kwargs.keys()):
            self.input_arg = kwargs['input_arg']
            if(len(self.input_arg) <= 0):
                self.input_arg = iinput.load_init(__file__)
            if self.input_arg is None:
                sys.exit(0)
      
    def Main(self):
        long_value='t_hn_report_day'
        #鼠标点击
        self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:Main,StepNodeTag:20240328174515252873,Title:鼠标点击,Note:')
        iimg.do_click_pos(waitfor=30.000,button='left',curson='Center',image=r'snapshot_20240329170931227.png',image_size=r'122X17',win_title=r'数据库管理 - Google Chrome',continue_on_error='break',img_res_path = self.path)
        #Select项
        self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:Main,StepNodeTag:20240328164650238259,Title:Select项,Note:')
        ichrome_firefox.set_element_selected_item_chrome(waitfor=10.000,itemText='投保日期',title=r'PICC - 报表平台',url=r'http://10.135.1.218/report/console',attrMap={"hasReachedRelativeAncestor":"false","nodeHierarchyInfo":[{"isPresentInSelector":1,"otherAttributes":{},"selectorInfo":{"attributes":{"css-selector":"#tjrqlx","id":"tjrqlx","tag":"SELECT","xpath":"//*[@id=\"tjrqlx\"]"},"index":0,"tagName":"SELECT"}},{"isPresentInSelector":1,"otherAttributes":{},"selectorInfo":{"attributes":{"css-selector":"#rightIframe","id":"rightIframe","tag":"IFRAME","xpath":"//*[@id=\"rightIframe\"]"},"index":0,"tagName":"IFRAME"}}]},itemMode='text')
        #Select项
        self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:Main,StepNodeTag:20240328164859094268,Title:Select项,Note:')
        ichrome_firefox.set_element_selected_item_chrome(waitfor=10.000,itemText='大个险*',title=r'PICC - 报表平台',url=r'http://10.135.1.218/report/console',attrMap={"hasReachedRelativeAncestor":"false","nodeHierarchyInfo":[{"isPresentInSelector":1,"otherAttributes":{},"selectorInfo":{"attributes":{"css-selector":"#channel","id":"channel","tag":"SELECT","xpath":"//*[@id=\"channel\"]"},"index":0,"tagName":"SELECT"}},{"isPresentInSelector":1,"otherAttributes":{},"selectorInfo":{"attributes":{"css-selector":"#rightIframe","id":"rightIframe","tag":"IFRAME","xpath":"//*[@id=\"rightIframe\"]"},"index":0,"tagName":"IFRAME"}}]},itemMode='text')
        #Select项
        self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:Main,StepNodeTag:20240328164917307270,Title:Select项,Note:')
        ichrome_firefox.set_element_selected_item_chrome(waitfor=10.000,itemText='长险',title=r'PICC - 报表平台',url=r'http://10.135.1.218/report/console',attrMap={"hasReachedRelativeAncestor":"false","nodeHierarchyInfo":[{"isPresentInSelector":1,"otherAttributes":{},"selectorInfo":{"attributes":{"css-selector":"#cdxbstj","id":"cdxbstj","tag":"SELECT","xpath":"//*[@id=\"cdxbstj\"]"},"index":0,"tagName":"SELECT"}},{"isPresentInSelector":1,"otherAttributes":{},"selectorInfo":{"attributes":{"css-selector":"#rightIframe","id":"rightIframe","tag":"IFRAME","xpath":"//*[@id=\"rightIframe\"]"},"index":0,"tagName":"IFRAME"}}]},itemMode='text')
        #鼠标点击
        self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:Main,StepNodeTag:20240328164958452274,Title:鼠标点击,Note:')
        ichrome_firefox.do_click_pos_chrome(waitfor=10.000,run_mode='unctrl',button='left',curson='center',continue_on_error='break',title=r'PICC - 报表平台',url=r'http://10.135.1.218/report/console',attrMap={"xpath":"//*[@id=\"begindate\"]"})
        #鼠标点击
        self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:Main,StepNodeTag:20240328165014904276,Title:鼠标点击,Note:')
        ichrome_firefox.do_click_pos_chrome(waitfor=10.000,run_mode='unctrl',button='left',curson='center',continue_on_error='break',title=r'PICC - 报表平台',url=r'http://10.135.1.218/report/console',attrMap={"hasReachedRelativeAncestor":"false","nodeHierarchyInfo":[{"isPresentInSelector":1,"otherAttributes":{},"selectorInfo":{"attributes":{"css-selector":"#dpTodayInput","id":"dpTodayInput","tag":"INPUT","type":"button","xpath":"//*[@id=\"dpTodayInput\"]"},"index":0,"tagName":"INPUT"}},{"isPresentInSelector":1,"otherAttributes":{},"selectorInfo":{"attributes":{"css-selector":"html:nth-child(1) > body:nth-child(2) > div:nth-child(3) > iframe:nth-child(1)","src":"http://10.135.1.218/dsas/jsp/js/datepicker/My97DatePicker.htm","tag":"IFRAME","xpath":"/html/body/div[1]/iframe[1]"},"index":0,"tagName":"IFRAME"}},{"isPresentInSelector":1,"otherAttributes":{},"selectorInfo":{"attributes":{"css-selector":"#rightIframe","id":"rightIframe","tag":"IFRAME","xpath":"//*[@id=\"rightIframe\"]"},"index":0,"tagName":"IFRAME"}}]})
        #鼠标点击
        self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:Main,StepNodeTag:20240328165235374280,Title:鼠标点击,Note:')
        ichrome_firefox.do_click_pos_chrome(waitfor=10.000,run_mode='unctrl',button='left',curson='center',times=2,continue_on_error='break',title=r'PICC - 报表平台',url=r'http://10.135.1.218/report/console',attrMap={"hasReachedRelativeAncestor":"false","nodeHierarchyInfo":[{"isPresentInSelector":1,"otherAttributes":{},"selectorInfo":{"attributes":{"css-selector":"#download","id":"download","tag":"IMG","xpath":"//*[@id=\"download\"]"},"index":0,"tagName":"IMG"}},{"isPresentInSelector":1,"otherAttributes":{},"selectorInfo":{"attributes":{"css-selector":"#rightIframe","id":"rightIframe","tag":"IFRAME","xpath":"//*[@id=\"rightIframe\"]"},"index":0,"tagName":"IFRAME"}}]})
        #等待时间
        self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:Main,StepNodeTag:20240328165458164284,Title:等待时间,Note:')
        rpa_time.time_sleep(wait_time=60)
        #执行命令
        self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:Main,StepNodeTag:20240328165544776302,Title:执行命令,Note:')
        ics.do_popen_exe(command='rename *明细表.zip long_yushou_data.zip',work_path='C:/Users/Administrator/Downloads',block=True)
        time.sleep(0.6)
        #代码块
        self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:Main,StepNodeTag:202403281823556131403,Title:代码块,Note:解压缩文件')
        import zipfile
        
        zip_file = 'C:/Users/Administrator/Downloads/long_yushou_data.zip'
        extract_folder = 'C:/Users/Administrator/Downloads/'
        
        with zipfile.ZipFile(zip_file, 'r') as zip_ref:
            zip_ref.extractall(extract_folder)
        
        print(f'{zip_file} 已成功解压缩到 {extract_folder} 文件夹中。')
        #执行命令
        self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:Main,StepNodeTag:20240328170041213384,Title:执行命令,Note:修改csv为long_yushou_data')
        ics.do_popen_exe(command='rename *admin141*.csv long_yushou_data.csv',work_path='C:/Users/Administrator/Downloads',block=True)
        time.sleep(0.6)
        #代码块
        self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:Main,StepNodeTag:20240328170150603400,Title:代码块,Note:处理csv并删除第一行')
        import csv
        
        # 读取文件并删除第一行数据
        with open('C:/Users/Administrator/Downloads/long_yushou_data.csv', 'r', newline='') as f:
            reader = csv.reader(f)
            data = list(reader)[1:]
        
        # 保存文件
        with open('C:/Users/Administrator/Downloads/long_yushou_data.csv', 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(data)
        
        print("删除第一行数据并保存成功")
        
        #执行命令
        self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:Main,StepNodeTag:20240328170822079489,Title:执行命令,Note:修改csv为long_yushou_data')
        ics.do_popen_exe(command='del *.zip',work_path='C:/Users/Administrator/Downloads',block=True)
        time.sleep(0.6)
        #鼠标点击
        self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:Main,StepNodeTag:20240328170919223502,Title:鼠标点击,Note:')
        iimg.do_click_pos(waitfor=30.000,button='left',curson='Center',image=r'snapshot_20240328175357677.png',image_size=r'98X19',win_title=r'PICC - 报表平台 - Google Chrome',confidence=0.5,continue_on_error='break',img_res_path = self.path)
        #鼠标点击
        self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:Main,StepNodeTag:20240328171139393522,Title:鼠标点击,Note:')
        ichrome_firefox.do_click_pos_chrome(waitfor=10.000,run_mode='unctrl',button='left',curson='center',continue_on_error='break',title=r'数据库管理',url=r'https://abi.deci.picclife.cn/eweb/titlepage.do?title=%25u6570%25u636E%25u5E93%25u7BA1%25u7406&url=%2Fedatasource%2Fjdbc.do%253Faction%253Dviewjdbcmgr%2526jdbcName%253Dgbase_db_141',attrMap={"hasReachedRelativeAncestor":"false","nodeHierarchyInfo":[{"isPresentInSelector":1,"otherAttributes":{},"selectorInfo":{"attributes":{"css-selector":"#ESEN$ECoolElement2","id":"ESEN$ECoolElement2","tag":"LI","xpath":"//*[@id=\"ESEN$ECoolElement2\"]"},"index":0,"tagName":"LI"}},{"isPresentInSelector":1,"otherAttributes":{},"selectorInfo":{"attributes":{"css-selector":"#eweb_titlepage_frame","id":"eweb_titlepage_frame","tag":"IFRAME","xpath":"//*[@id=\"eweb_titlepage_frame\"]"},"index":0,"tagName":"IFRAME"}}]})
        time.sleep(1)
        #鼠标点击
        self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:Main,StepNodeTag:20240328171200735526,Title:鼠标点击,Note:')
        iimg.do_click_pos(waitfor=30.000,button='left',curson='Center',image=r'snapshot_20240328181119853.png',image_size=r'26X17',win_title=r'数据库管理 - Google Chrome',continue_on_error='break',img_res_path = self.path)
        #鼠标点击
        self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:Main,StepNodeTag:20240328171238518536,Title:鼠标点击,Note:')
        iimg.do_click_pos(waitfor=30.000,button='left',curson='Center',image=r'snapshot_20240328180811021.png',image_size=r'53X19',win_title=r'打开',continue_on_error='break',img_res_path = self.path)
        #等待时间
        self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:Main,StepNodeTag:202403291418293844070,Title:等待时间,Note:')
        rpa_time.time_sleep(wait_time=2)
        #鼠标点击
        self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:Main,StepNodeTag:202403281757354791088,Title:鼠标点击,Note:')
        iimg.do_click_pos(waitfor=30.000,button='left',curson='Center',times=2,image=r'snapshot_20240328180917530.png',image_size=r'150X21',win_title=r'打开',continue_on_error='break',img_res_path = self.path)
        time.sleep(1)
        #鼠标点击
        self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:Main,StepNodeTag:20240328171536025552,Title:鼠标点击,Note:')
        ichrome_firefox.do_click_pos_chrome(waitfor=10.000,run_mode='unctrl',button='left',curson='center',continue_on_error='break',title=r'数据库管理',url=r'https://abi.deci.picclife.cn/eweb/titlepage.do?title=%25u6570%25u636E%25u5E93%25u7BA1%25u7406&url=%2Fedatasource%2Fjdbc.do%253Faction%253Dviewjdbcmgr%2526jdbcName%253Dgbase_db_141',attrMap={"xpath":"/html/body/div[1]/div[2]/button[1]"})
        #鼠标点击
        self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:Main,StepNodeTag:202403291650269481483,Title:鼠标点击,Note:')
        ichrome_firefox.do_click_pos_chrome(waitfor=10.000,run_mode='unctrl',button='left',curson='center',continue_on_error='break',title=r'数据库管理',url=r'https://abi.deci.picclife.cn/eweb/titlepage.do?title=%25u6570%25u636E%25u5E93%25u7BA1%25u7406&url=%2Fedatasource%2Fjdbc.do%253Faction%253Dviewjdbcmgr%2526jdbcName%253Dgbase_db_141',attrMap={"xpath":"//*[@id=\"appendElement\"]/div[1]/span[1]"})
        #设置文本
        self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:Main,StepNodeTag:20240328172313531591,Title:设置文本,Note:')
        ichrome_firefox.set_element_val_chrome(waitfor=10.000,text=r't_hn_report_day',title=r'数据库管理',url=r'https://abi.deci.picclife.cn/eweb/titlepage.do?title=%25u6570%25u636E%25u5E93%25u7BA1%25u7406&url=%2Fedatasource%2Fjdbc.do%253Faction%253Dviewjdbcmgr%2526jdbcName%253Dgbase_db_141',attrMap={"xpath":"//*[@id=\"append-input\"]/div[1]/input[1]"})
        #鼠标点击
        self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:Main,StepNodeTag:20240328172413156605,Title:鼠标点击,Note:')
        ichrome_firefox.do_click_pos_chrome(waitfor=10.000,run_mode='unctrl',button='left',curson='center',continue_on_error='break',title=r'数据库管理',url=r'https://abi.deci.picclife.cn/eweb/titlepage.do?title=%25u6570%25u636E%25u5E93%25u7BA1%25u7406&url=%2Fedatasource%2Fjdbc.do%253Faction%253Dviewjdbcmgr%2526jdbcName%253Dgbase_db_141',attrMap={"xpath":"/html/body/div[1]/div[2]/button[1]"})
        #等待时间
        self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:Main,StepNodeTag:202403291104576273572,Title:等待时间,Note:')
        rpa_time.time_sleep(wait_time=300)
        #鼠标点击
        self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:Main,StepNodeTag:202403291021348393271,Title:鼠标点击,Note:')
        ichrome_firefox.do_click_pos_chrome(waitfor=0.200,run_mode='unctrl',button='left',curson='center',continue_on_error='break',title=r'数据库管理',url=r'https://abi.deci.picclife.cn/eweb/titlepage.do?title=%25u6570%25u636E%25u5E93%25u7BA1%25u7406&url=%2Fedatasource%2Fjdbc.do%253Faction%253Dviewjdbcmgr%2526jdbcName%253Dgbase_db_141',attrMap={"hasReachedRelativeAncestor":"false","nodeHierarchyInfo":[{"isPresentInSelector":1,"otherAttributes":{},"selectorInfo":{"attributes":{"css-selector":"#jdbcrightpanel > div:nth-child(1) > div:nth-child(1) > ul:nth-child(1) > li:nth-child(2) > i:nth-child(3)","parentid":"jdbcrightpanel","tag":"I","xpath":"//*[@id=\"jdbcrightpanel\"]/div[1]/div[1]/ul[1]/li[2]/i[2]"},"index":0,"tagName":"I"}},{"isPresentInSelector":1,"otherAttributes":{},"selectorInfo":{"attributes":{"css-selector":"#eweb_titlepage_frame","id":"eweb_titlepage_frame","tag":"IFRAME","xpath":"//*[@id=\"eweb_titlepage_frame\"]"},"index":0,"tagName":"IFRAME"}}]})
        #执行命令
        self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:Main,StepNodeTag:202403291057293003397,Title:执行命令,Note:修改csv为long_yushou_data')
        ics.do_popen_exe(command='del long_yushou_data.csv',work_path='C:/Users/Administrator/Downloads',block=True)
        time.sleep(0.6)
        #鼠标点击
        self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:Main,StepNodeTag:202403291709416451939,Title:鼠标点击,Note:')
        iimg.do_click_pos(waitfor=30.000,button='left',curson='Center',image=r'snapshot_20240329170931227.png',image_size=r'122X17',win_title=r'数据库管理 - Google Chrome',continue_on_error='break',img_res_path = self.path)
        #Select项
        self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:Main,StepNodeTag:202403291051228143290,Title:Select项,Note:')
        ichrome_firefox.set_element_selected_item_chrome(waitfor=10.000,itemText='承保日期',title=r'PICC - 报表平台',url=r'http://10.135.1.218/report/console',attrMap={"hasReachedRelativeAncestor":"false","nodeHierarchyInfo":[{"isPresentInSelector":1,"otherAttributes":{},"selectorInfo":{"attributes":{"css-selector":"#tjrqlx","id":"tjrqlx","tag":"SELECT","xpath":"//*[@id=\"tjrqlx\"]"},"index":0,"tagName":"SELECT"}},{"isPresentInSelector":1,"otherAttributes":{},"selectorInfo":{"attributes":{"css-selector":"#rightIframe","id":"rightIframe","tag":"IFRAME","xpath":"//*[@id=\"rightIframe\"]"},"index":0,"tagName":"IFRAME"}}]},itemMode='text')
        #Select项
        self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:Main,StepNodeTag:202403291051228143298,Title:Select项,Note:')
        ichrome_firefox.set_element_selected_item_chrome(waitfor=10.000,itemText='大个险*',title=r'PICC - 报表平台',url=r'http://10.135.1.218/report/console',attrMap={"hasReachedRelativeAncestor":"false","nodeHierarchyInfo":[{"isPresentInSelector":1,"otherAttributes":{},"selectorInfo":{"attributes":{"css-selector":"#channel","id":"channel","tag":"SELECT","xpath":"//*[@id=\"channel\"]"},"index":0,"tagName":"SELECT"}},{"isPresentInSelector":1,"otherAttributes":{},"selectorInfo":{"attributes":{"css-selector":"#rightIframe","id":"rightIframe","tag":"IFRAME","xpath":"//*[@id=\"rightIframe\"]"},"index":0,"tagName":"IFRAME"}}]},itemMode='text')
        #Select项
        self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:Main,StepNodeTag:202403291051228143284,Title:Select项,Note:')
        ichrome_firefox.set_element_selected_item_chrome(waitfor=10.000,itemText='短险',title=r'PICC - 报表平台',url=r'http://10.135.1.218/report/console',attrMap={"hasReachedRelativeAncestor":"false","nodeHierarchyInfo":[{"isPresentInSelector":1,"otherAttributes":{},"selectorInfo":{"attributes":{"css-selector":"#cdxbstj","id":"cdxbstj","tag":"SELECT","xpath":"//*[@id=\"cdxbstj\"]"},"index":0,"tagName":"SELECT"}},{"isPresentInSelector":1,"otherAttributes":{},"selectorInfo":{"attributes":{"css-selector":"#rightIframe","id":"rightIframe","tag":"IFRAME","xpath":"//*[@id=\"rightIframe\"]"},"index":0,"tagName":"IFRAME"}}]},itemMode='text')
        #鼠标点击
        self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:Main,StepNodeTag:202403291713154941973,Title:鼠标点击,Note:')
        ichrome_firefox.do_click_pos_chrome(waitfor=10.000,run_mode='unctrl',button='left',curson='center',continue_on_error='break',title=r'PICC - 报表平台',url=r'http://10.135.1.218/report/console',attrMap={"xpath":"//*[@id=\"begindate\"]"})
        #鼠标点击
        self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:Main,StepNodeTag:202403291051228143289,Title:鼠标点击,Note:')
        ichrome_firefox.do_click_pos_chrome(waitfor=10.000,run_mode='unctrl',button='left',curson='center',continue_on_error='break',title=r'PICC - 报表平台',url=r'http://10.135.1.218/report/console',attrMap={"hasReachedRelativeAncestor":"false","nodeHierarchyInfo":[{"isPresentInSelector":1,"otherAttributes":{},"selectorInfo":{"attributes":{"css-selector":"#dpTodayInput","id":"dpTodayInput","tag":"INPUT","type":"button","xpath":"//*[@id=\"dpTodayInput\"]"},"index":0,"tagName":"INPUT"}},{"isPresentInSelector":1,"otherAttributes":{},"selectorInfo":{"attributes":{"css-selector":"html:nth-child(1) > body:nth-child(2) > div:nth-child(3) > iframe:nth-child(1)","src":"http://10.135.1.218/dsas/jsp/js/datepicker/My97DatePicker.htm","tag":"IFRAME","xpath":"/html/body/div[1]/iframe[1]"},"index":0,"tagName":"IFRAME"}},{"isPresentInSelector":1,"otherAttributes":{},"selectorInfo":{"attributes":{"css-selector":"#rightIframe","id":"rightIframe","tag":"IFRAME","xpath":"//*[@id=\"rightIframe\"]"},"index":0,"tagName":"IFRAME"}}]})
        #鼠标点击
        self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:Main,StepNodeTag:202403291712554311966,Title:鼠标点击,Note:')
        ichrome_firefox.do_click_pos_chrome(waitfor=10.000,run_mode='unctrl',button='left',curson='center',times=2,continue_on_error='break',title=r'PICC - 报表平台',url=r'http://10.135.1.218/report/console',attrMap={"hasReachedRelativeAncestor":"false","nodeHierarchyInfo":[{"isPresentInSelector":1,"otherAttributes":{},"selectorInfo":{"attributes":{"css-selector":"#download","id":"download","tag":"IMG","xpath":"//*[@id=\"download\"]"},"index":0,"tagName":"IMG"}},{"isPresentInSelector":1,"otherAttributes":{},"selectorInfo":{"attributes":{"css-selector":"#rightIframe","id":"rightIframe","tag":"IFRAME","xpath":"//*[@id=\"rightIframe\"]"},"index":0,"tagName":"IFRAME"}}]})
        #等待时间
        self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:Main,StepNodeTag:202403291051228143303,Title:等待时间,Note:')
        rpa_time.time_sleep(wait_time=60)
        #执行命令
        self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:Main,StepNodeTag:202403291051228143286,Title:执行命令,Note:')
        ics.do_popen_exe(command='rename *明细表.zip short_yushou_data.zip',work_path='C:/Users/Administrator/Downloads',block=True)
        time.sleep(0.6)
        #代码块
        self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:Main,StepNodeTag:202403291051228143283,Title:代码块,Note:解压缩文件')
        import zipfile
        
        zip_file = 'C:/Users/Administrator/Downloads/short_yushou_data.zip'
        extract_folder = 'C:/Users/Administrator/Downloads/'
        
        with zipfile.ZipFile(zip_file, 'r') as zip_ref:
            zip_ref.extractall(extract_folder)
        
        print(f'{zip_file} 已成功解压缩到 {extract_folder} 文件夹中。')
        #执行命令
        self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:Main,StepNodeTag:202403291051228143305,Title:执行命令,Note:修改csv为long_yushou_data')
        ics.do_popen_exe(command='rename *admin141*.csv short_yushou_data.csv',work_path='C:/Users/Administrator/Downloads',block=True)
        time.sleep(0.6)
        #代码块
        self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:Main,StepNodeTag:202403291051228143300,Title:代码块,Note:处理csv并删除第一行')
        import csv
        
        # 读取文件并删除第一行数据
        with open('C:/Users/Administrator/Downloads/short_yushou_data.csv', 'r', newline='') as f:
            reader = csv.reader(f)
            data = list(reader)[1:]
        
        # 保存文件
        with open('C:/Users/Administrator/Downloads/short_yushou_data.csv', 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(data)
        
        print("删除第一行数据并保存成功")
        
        #执行命令
        self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:Main,StepNodeTag:202403291051228143296,Title:执行命令,Note:修改csv为long_yushou_data')
        ics.do_popen_exe(command='del *.zip',work_path='C:/Users/Administrator/Downloads',block=True)
        time.sleep(0.6)
        #鼠标点击
        self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:Main,StepNodeTag:202403291051228143285,Title:鼠标点击,Note:')
        iimg.do_click_pos(waitfor=30.000,button='left',curson='Center',image=r'snapshot_20240328175357677.png',image_size=r'98X19',win_title=r'PICC - 报表平台 - Google Chrome',confidence=0.5,continue_on_error='break',img_res_path = self.path)
        #鼠标点击
        self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:Main,StepNodeTag:202403291051228143302,Title:鼠标点击,Note:')
        ichrome_firefox.do_click_pos_chrome(waitfor=10.000,run_mode='unctrl',button='left',curson='center',continue_on_error='break',title=r'数据库管理',url=r'https://abi.deci.picclife.cn/eweb/titlepage.do?title=%25u6570%25u636E%25u5E93%25u7BA1%25u7406&url=%2Fedatasource%2Fjdbc.do%253Faction%253Dviewjdbcmgr%2526jdbcName%253Dgbase_db_141',attrMap={"hasReachedRelativeAncestor":"false","nodeHierarchyInfo":[{"isPresentInSelector":1,"otherAttributes":{},"selectorInfo":{"attributes":{"css-selector":"#ESEN$ECoolElement2","id":"ESEN$ECoolElement2","tag":"LI","xpath":"//*[@id=\"ESEN$ECoolElement2\"]"},"index":0,"tagName":"LI"}},{"isPresentInSelector":1,"otherAttributes":{},"selectorInfo":{"attributes":{"css-selector":"#eweb_titlepage_frame","id":"eweb_titlepage_frame","tag":"IFRAME","xpath":"//*[@id=\"eweb_titlepage_frame\"]"},"index":0,"tagName":"IFRAME"}}]})
        time.sleep(1)
        #鼠标点击
        self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:Main,StepNodeTag:202403291051228143301,Title:鼠标点击,Note:')
        iimg.do_click_pos(waitfor=30.000,button='left',curson='Center',image=r'snapshot_20240328181119853.png',image_size=r'26X17',win_title=r'数据库管理 - Google Chrome',continue_on_error='break',img_res_path = self.path)
        #鼠标点击
        self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:Main,StepNodeTag:202403291051228143295,Title:鼠标点击,Note:')
        iimg.do_click_pos(waitfor=30.000,button='left',curson='Center',image=r'snapshot_20240328180811021.png',image_size=r'53X19',win_title=r'打开',continue_on_error='break',img_res_path = self.path)
        time.sleep(6)
        #鼠标点击
        self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:Main,StepNodeTag:202403291051228143291,Title:鼠标点击,Note:')
        iimg.do_click_pos(waitfor=30.000,button='left',curson='Center',times=2,image=r'snapshot_20240329110022976.png',image_size=r'151X20',win_title=r'打开',continue_on_error='break',img_res_path = self.path)
        #鼠标点击
        self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:Main,StepNodeTag:20240329151538318536,Title:鼠标点击,Note:')
        ichrome_firefox.do_click_pos_chrome(waitfor=10.000,run_mode='unctrl',button='left',curson='center',continue_on_error='break',title=r'数据库管理',url=r'https://abi.deci.picclife.cn/eweb/titlepage.do?title=%25u6570%25u636E%25u5E93%25u7BA1%25u7406&url=%2Fedatasource%2Fjdbc.do%253Faction%253Dviewjdbcmgr%2526jdbcName%253Dgbase_db_141',attrMap={"aaname":"下一步"})
        #鼠标点击
        self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:Main,StepNodeTag:202403291051228143307,Title:鼠标点击,Note:')
        ichrome_firefox.do_click_pos_chrome(waitfor=10.000,run_mode='unctrl',button='left',curson='center',continue_on_error='break',title=r'数据库管理',url=r'https://abi.deci.picclife.cn/eweb/titlepage.do?title=%25u6570%25u636E%25u5E93%25u7BA1%25u7406&url=%2Fedatasource%2Fjdbc.do%253Faction%253Dviewjdbcmgr%2526jdbcName%253Dgbase_db_141',attrMap={"xpath":"//*[@id=\"appendElement\"]/div[1]/span[1]"})
        #设置文本
        self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:Main,StepNodeTag:20240329151551838544,Title:设置文本,Note:')
        ichrome_firefox.set_element_val_chrome(waitfor=10.000,text=r't_hn_report_day',title=r'数据库管理',url=r'https://abi.deci.picclife.cn/eweb/titlepage.do?title=%25u6570%25u636E%25u5E93%25u7BA1%25u7406&url=%2Fedatasource%2Fjdbc.do%253Faction%253Dviewjdbcmgr%2526jdbcName%253Dgbase_db_141',attrMap={"xpath":"//*[@id=\"append-input\"]/div[1]/input[1]"})
        #鼠标点击
        self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:Main,StepNodeTag:20240329151646934558,Title:鼠标点击,Note:')
        ichrome_firefox.do_click_pos_chrome(waitfor=10.000,run_mode='unctrl',button='left',curson='center',continue_on_error='break',title=r'数据库管理',url=r'https://abi.deci.picclife.cn/eweb/titlepage.do?title=%25u6570%25u636E%25u5E93%25u7BA1%25u7406&url=%2Fedatasource%2Fjdbc.do%253Faction%253Dviewjdbcmgr%2526jdbcName%253Dgbase_db_141',attrMap={"xpath":"/html/body/div[1]/div[2]/button[1]"})
        #等待时间
        self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:Main,StepNodeTag:202403291105109693574,Title:等待时间,Note:')
        rpa_time.time_sleep(wait_time=300)
        #鼠标点击
        self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:Main,StepNodeTag:202403291051228143288,Title:鼠标点击,Note:')
        ichrome_firefox.do_click_pos_chrome(waitfor=0.200,run_mode='unctrl',button='left',curson='center',continue_on_error='break',title=r'数据库管理',url=r'https://abi.deci.picclife.cn/eweb/titlepage.do?title=%25u6570%25u636E%25u5E93%25u7BA1%25u7406&url=%2Fedatasource%2Fjdbc.do%253Faction%253Dviewjdbcmgr%2526jdbcName%253Dgbase_db_141',attrMap={"hasReachedRelativeAncestor":"false","nodeHierarchyInfo":[{"isPresentInSelector":1,"otherAttributes":{},"selectorInfo":{"attributes":{"css-selector":"#jdbcrightpanel > div:nth-child(1) > div:nth-child(1) > ul:nth-child(1) > li:nth-child(2) > i:nth-child(3)","parentid":"jdbcrightpanel","tag":"I","xpath":"//*[@id=\"jdbcrightpanel\"]/div[1]/div[1]/ul[1]/li[2]/i[2]"},"index":0,"tagName":"I"}},{"isPresentInSelector":1,"otherAttributes":{},"selectorInfo":{"attributes":{"css-selector":"#eweb_titlepage_frame","id":"eweb_titlepage_frame","tag":"IFRAME","xpath":"//*[@id=\"eweb_titlepage_frame\"]"},"index":0,"tagName":"IFRAME"}}]})
        #执行命令
        self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:Main,StepNodeTag:202403291058563633428,Title:执行命令,Note:修改csv为long_yushou_data')
        ics.do_popen_exe(command='del short_yushou_data.csv',work_path='C:/Users/Administrator/Downloads',block=True)
        time.sleep(0.6)
 
if __name__ == '__main__':
    ILog.begin_init()
    robot_no = ''
    proc_no = ''
    job_no = ''
    input_arg = ''
    try:
        argv = sys.argv[1:]
        opts, args = getopt.getopt(argv,"hr:p:j:i:",["robot = ","proc = ","job = ","input = "])
    except getopt.GetoptError:
        print ('robot.py -r <robot> -p <proc> -j <job>')
    for opt, arg in opts:
        if opt == '-h':
            print ('robot.py -r <robot> -p <proc> -j <job>')
        elif opt in ("-r", "--robot"):
            robot_no = arg
        elif opt in ("-p", "--proc"):
            proc_no = arg
        elif opt in ("-j", "--job"):
            job_no = arg
        elif opt in ("-i", "--input"):
            input_arg = arg
    pro = HN_Report_import_data(robot_no=robot_no,proc_no=proc_no,job_no=job_no,input_arg=input_arg)
    pro.Main()
