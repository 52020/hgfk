# coding=utf-8
# 编译日期：2024-12-30 16:12:04
# 版权所有：www.i-search.com.cn
import ubpa.init_input as iinput
from ubpa.base_util import StdOutHook, ExceptionHandler
import ubpa.itools.rpa_str as rpa_str
import ubpa.iplatform as iplatform
import ubpa.ibox as ibox
import ubpa.ichrome_firefox as ichrome_firefox
import ubpa.ikeyboard as ikeyboard
import ubpa.iwin as iwin
import ubpa.ibrowse as ibrowse
import ubpa.itools.rpa_time as rpa_time
import ubpa.ifile as ifile
import ubpa.iautomation as iautomation
import time
import pdb
from ubpa.ilog import ILog
import getopt
from sys import argv
import sys
import os
from ubpa.base_img import *

class SXCC_ODS_Related_Operations_P:
     
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
      
    def SXCC_ODS_Automatic_Login_P(self,Str_ODS_Google_Chrome_Path=r"E:\Chrome_86_odsportal\GoogleChromePortable.exe",Str_ODS_User="",Str_ODS_Password="",Str_Pop_Up_Prompt="是"):
        '''ODS系统自动登录-OCR生产环境（谷歌浏览器）\n（SXCC_ODS_Automatic_Login_P）\n1.初始化\n'''
        Str_OCR_APP_URL=None
        Str_OCR_APP_KEY=None
        Str_OCR_APP_SECRET=None
        Int_Loop_Index_Number=None
        Str_Image_Path=None
        Str_Identifying_Code_Text=None
        # 序列
        self.__logger.dlogs(job_no=self.job_no, logmsg='Flow:SXCC_ODS_Automatic_Login_P,StepNodeTag:20240419142146324201,Title:序列,Note:')
        #输出
        self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:SXCC_ODS_Automatic_Login_P,StepNodeTag:20240419142146324200,Title:输出,Note:')
        rpa_str.iprints("SXCC_ODS_Automatic_Login Start")
        #获取变量
        self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:SXCC_ODS_Automatic_Login_P,StepNodeTag:20240419142146324198,Title:获取变量,Note:')
        Str_OCR_APP_URL=iplatform.getAsset(name='集团OCR生产环境通用识别api_url',timeout=10000,robot_no=self.robot_no,job_no=self.job_no,proc_no=self.proc_no)
        #获取变量
        self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:SXCC_ODS_Automatic_Login_P,StepNodeTag:20240419142146324197,Title:获取变量,Note:')
        Str_OCR_APP_KEY=iplatform.getAsset(name='集团OCR生产环境通用识别app_key',timeout=10000,robot_no=self.robot_no,job_no=self.job_no,proc_no=self.proc_no)
        #获取变量
        self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:SXCC_ODS_Automatic_Login_P,StepNodeTag:20240419142146324196,Title:获取变量,Note:')
        Str_OCR_APP_SECRET=iplatform.getAsset(name='集团OCR生产环境通用识别app_secret',timeout=10000,robot_no=self.robot_no,job_no=self.job_no,proc_no=self.proc_no)
        #打开浏览器
        self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:SXCC_ODS_Automatic_Login_P,StepNodeTag:20240419142146324193,Title:打开浏览器,Note:')
        ibrowse.open_browser(browser_type='chrome',url="http://10.135.1.163",path=Str_ODS_Google_Chrome_Path,param='--start-maximized',maximum=1,max_sleep=3)
        time.sleep(1)
        #最大化窗口
        self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:SXCC_ODS_Automatic_Login_P,StepNodeTag:20240419142146285165,Title:最大化窗口,Note:')
        iwin.do_win_maximize(waitfor=10.000,win_title=r'Google Chrome')
        #模拟按键
        self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:SXCC_ODS_Automatic_Login_P,StepNodeTag:20240419142146292172,Title:模拟按键,Note:')
        ikeyboard.key_send_cs(waitfor=10.000,win_title=r'Google Chrome',text='{ESC}')
        # For循环
        self.__logger.dlogs(job_no=self.job_no, logmsg='Flow:SXCC_ODS_Automatic_Login_P,StepNodeTag:20240419142146313180,Title:For循环,Note:')
        for Int_Loop_Index_Number in range(1,4):
            # Try异常
            self.__logger.dlogs(job_no=self.job_no, logmsg='Flow:SXCC_ODS_Automatic_Login_P,StepNodeTag:20240419142146319186,Title:Try异常,Note:')
            try:
                #设置文本
                self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:SXCC_ODS_Automatic_Login_P,StepNodeTag:20240419142146316184,Title:设置文本,Note:')
                ichrome_firefox.set_element_val_chrome(waitfor=3.000,text=Str_ODS_User,title=r'登录',url=r"http*",attrMap={"xpath":"//*[@id=\"username\"]"})
                #设置文本
                self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:SXCC_ODS_Automatic_Login_P,StepNodeTag:20240419142146319187,Title:设置文本,Note:')
                ichrome_firefox.set_element_val_chrome(waitfor=3.000,text=Str_ODS_Password,title=r'登录',url=r"http*",attrMap={"xpath":"//*[@id=\"password\"]"})
                #元素截图
                self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:SXCC_ODS_Automatic_Login_P,StepNodeTag:20240419142146321189,Title:元素截图,Note:')
                Str_Image_Path=ichrome_firefox.capture_image_chrome(waitfor=10.000,title=r'登录',url=r"http*",attrMap={"xpath":"//*[@id=\"checkImg\"]"})
                #代码块
                self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:SXCC_ODS_Automatic_Login_P,StepNodeTag:20240419142146289168,Title:代码块,Note:验证码图片转文本')
                from PIL import Image
                import os
                import urllib
                import requests
                import base64
                import json
                from urllib.parse import urlencode,quote
                
                def img_to_base64(img_path):
                    with open(img_path, 'rb') as read:
                        b64 = base64.b64encode(read.read())
                    return b64
                def ocr_identify(file_path,APP_URL='',APP_KEY='',APP_SECRET=''):
                #    api_url = "http://10.111.10.208:80/ex-reco-web/ocr/v1/table_api"
                #    api_url = "http://10.111.10.208:80/ex-reco-web/ocr/v1/general"
                #     api_url = "http://api-south.infra.picclife.cn/ocr/v1/general?apikey=69444db5578d4210a0114eabba53e836"
                #     api_url = f"http://10.57.3.179:28121/ocr/v1/general?apikey={APP_KEY}"
                    api_url = APP_URL
                    image_base64 = img_to_base64(file_path)
                    result = {}
                    headers = {'content-type ':'application/x-www-from-urlencoded'}
                
                    data = {'image_base64': image_base64, 
                            'app_key':APP_KEY,
                            'app_secret':APP_SECRET}
                    r = requests.post(api_url, data=data, verify=False)
                    result = json.loads(r.text)
                    all_data = ''
                    page_data = ''
                    for i in result['result']:
                        page_data = page_data + i['words'] + '\n'
                    print(page_data)
                    return page_data
                    
                Str_Identifying_Code_Text=ocr_identify(file_path=Str_Image_Path,APP_URL=Str_OCR_APP_URL,APP_KEY=Str_OCR_APP_KEY,APP_SECRET=Str_OCR_APP_SECRET)
                #设置文本
                self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:SXCC_ODS_Automatic_Login_P,StepNodeTag:20240419142146313182,Title:设置文本,Note:')
                ichrome_firefox.set_element_val_chrome(waitfor=10.000,text=Str_Identifying_Code_Text,title=r'登录',url=r"http*",attrMap={"xpath":"//*[@id=\"checkCode\"]"})
                #鼠标点击
                self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:SXCC_ODS_Automatic_Login_P,StepNodeTag:20240419142146309178,Title:鼠标点击,Note:')
                ichrome_firefox.do_click_pos_chrome(waitfor=10.000,run_mode='ctrl',button='left',curson='center',continue_on_error='break',title=r'登录',url=r"http*",attrMap={"xpath":"//li[text()='登录']"})
                time.sleep(2)
                #元素是否存在
                self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:SXCC_ODS_Automatic_Login_P,StepNodeTag:20240419142146289169,Title:元素是否存在,Note:')
                tvar_20240419100137135324=ichrome_firefox.is_element_existed_in_chrome(waitfor=10.000,curson='center',title=r'首页',url=r"http*",attrMap={"hasReachedRelativeAncestor":"false","nodeHierarchyInfo":[{"isPresentInSelector":1,"otherAttributes":{},"selectorInfo":{"attributes":{"css-selector":"#buttonUl > li:nth-child(1) > img:nth-child(1)","parentid":"buttonUl","tag":"IMG","xpath":"//*[@id=\"buttonUl\"]/li[1]/img[1]"},"index":0,"tagName":"IMG"}}]})
                # IF分支
                self.__logger.dlogs(job_no=self.job_no, logmsg='Flow:SXCC_ODS_Automatic_Login_P,StepNodeTag:20240419142146324191,Title:IF分支,Note:')
                if tvar_20240419100137135324:
                    #输出
                    self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:SXCC_ODS_Automatic_Login_P,StepNodeTag:20240419142146285161,Title:输出,Note:')
                    rpa_str.iprints("ODS系统自动登录成功")
                    # IF分支
                    self.__logger.dlogs(job_no=self.job_no, logmsg='Flow:SXCC_ODS_Automatic_Login_P,StepNodeTag:20240419142146285152,Title:IF分支,Note:')
                    if ("是" in Str_Pop_Up_Prompt) or ("Yes" in Str_Pop_Up_Prompt) or ("Y" in Str_Pop_Up_Prompt) :
                        #输出
                        self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:SXCC_ODS_Automatic_Login_P,StepNodeTag:20240419142146285154,Title:输出,Note:')
                        rpa_str.iprints("需要弹出提示")
                        #消息框
                        self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:SXCC_ODS_Automatic_Login_P,StepNodeTag:20240419142146285153,Title:消息框,Note:')
                        ibox.msgs_box("ODS系统自动登录成功",title=r"提示",timeout=0)
                    else:
                        #输出
                        self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:SXCC_ODS_Automatic_Login_P,StepNodeTag:20240419142146285151,Title:输出,Note:')
                        rpa_str.iprints("不需要弹出提示")
                    # Break中断
                    self.__logger.dlogs(job_no=self.job_no, logmsg='Flow:SXCC_ODS_Automatic_Login_P,StepNodeTag:20240419142146285155,Title:Break中断,Note:')
                    break
                else:
                    # IF分支
                    self.__logger.dlogs(job_no=self.job_no, logmsg='Flow:SXCC_ODS_Automatic_Login_P,StepNodeTag:20240419142146295175,Title:IF分支,Note:')
                    if Int_Loop_Index_Number==3:
                        #输出
                        self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:SXCC_ODS_Automatic_Login_P,StepNodeTag:20240419142146285150,Title:输出,Note:')
                        rpa_str.iprints("ODS系统自动登录失败（已重试3次），未知原因")
                        #消息框
                        self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:SXCC_ODS_Automatic_Login_P,StepNodeTag:20240419142146285162,Title:消息框,Note:')
                        ibox.msgs_box("ODS系统自动登录失败（已重试3次），请检查系统是否异常后，重新运行此组件，谢谢。",title=r"提示",timeout=0)
                        #代码块
                        self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:SXCC_ODS_Automatic_Login_P,StepNodeTag:20240419142146285163,Title:代码块,Note:停止')
                        exit()
                    else:
                        pass
            except Exception as e:
                #元素是否存在
                self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:SXCC_ODS_Automatic_Login_P,StepNodeTag:20240419142146295176,Title:元素是否存在,Note:')
                tvar_20240419100137133297=ichrome_firefox.is_element_existed_in_chrome(waitfor=10.000,curson='center',title=r'首页',url=r"http*",attrMap={"hasReachedRelativeAncestor":"false","nodeHierarchyInfo":[{"isPresentInSelector":1,"otherAttributes":{},"selectorInfo":{"attributes":{"css-selector":"#buttonUl > li:nth-child(1) > img:nth-child(1)","parentid":"buttonUl","tag":"IMG","xpath":"//*[@id=\"buttonUl\"]/li[1]/img[1]"},"index":0,"tagName":"IMG"}}]})
                # IF分支
                self.__logger.dlogs(job_no=self.job_no, logmsg='Flow:SXCC_ODS_Automatic_Login_P,StepNodeTag:20240419142146292171,Title:IF分支,Note:')
                if tvar_20240419100137133297:
                    #输出
                    self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:SXCC_ODS_Automatic_Login_P,StepNodeTag:20240419142146324192,Title:输出,Note:')
                    rpa_str.iprints("ODS系统自动登录成功")
                    # IF分支
                    self.__logger.dlogs(job_no=self.job_no, logmsg='Flow:SXCC_ODS_Automatic_Login_P,StepNodeTag:20240419142146285160,Title:IF分支,Note:')
                    if ("是" in Str_Pop_Up_Prompt) or ("Yes" in Str_Pop_Up_Prompt) or ("Y" in Str_Pop_Up_Prompt) :
                        #输出
                        self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:SXCC_ODS_Automatic_Login_P,StepNodeTag:20240419142146285159,Title:输出,Note:')
                        rpa_str.iprints("需要弹出提示")
                        #消息框
                        self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:SXCC_ODS_Automatic_Login_P,StepNodeTag:20240419142146285157,Title:消息框,Note:')
                        ibox.msgs_box("ODS系统自动登录成功",title=r"提示",timeout=0)
                    else:
                        #输出
                        self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:SXCC_ODS_Automatic_Login_P,StepNodeTag:20240419142146285156,Title:输出,Note:')
                        rpa_str.iprints("不需要弹出提示")
                    # Break中断
                    self.__logger.dlogs(job_no=self.job_no, logmsg='Flow:SXCC_ODS_Automatic_Login_P,StepNodeTag:20240419142146285158,Title:Break中断,Note:')
                    break
                else:
                    #输出
                    self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:SXCC_ODS_Automatic_Login_P,StepNodeTag:20240419142146295174,Title:输出,Note:')
                    rpa_str.iprints("ODS系统自动登录失败","异常信息为："+str(e))
                    #消息框
                    self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:SXCC_ODS_Automatic_Login_P,StepNodeTag:20240419142146313181,Title:消息框,Note:')
                    ibox.msgs_box("ODS系统自动登录失败，请检查系统是否异常后，重新运行此组件，谢谢。","异常信息为："+str(e),title=r"提示",timeout=0)
                    #代码块
                    self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:SXCC_ODS_Automatic_Login_P,StepNodeTag:20240419142146289167,Title:代码块,Note:停止')
                    exit()
            finally:
                pass
        #输出
        self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:SXCC_ODS_Automatic_Login_P,StepNodeTag:20240419142146324202,Title:输出,Note:')
        rpa_str.iprints("SXCC_ODS_Automatic_Login End")
      
    def SXCC_ODS_File_Download(self,Str_File_Path=r"C:\Users\Administrator\新建文件夹\C.xlsx",Str_Pop_Up_Prompt="是"):
        '''ODS系统文件下载设置保存到指定路径（谷歌浏览器，报表平台）\n（SXCC_ODS_File_Download）\n1.初始化\n'''
        # 序列
        self.__logger.dlogs(job_no=self.job_no, logmsg='Flow:SXCC_ODS_File_Download,StepNodeTag:20240419144438086859,Title:序列,Note:')
        #输出
        self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:SXCC_ODS_File_Download,StepNodeTag:20240419144438086858,Title:输出,Note:')
        rpa_str.iprints("SXCC_ODS_File_Download Start")
        # Try异常
        self.__logger.dlogs(job_no=self.job_no, logmsg='Flow:SXCC_ODS_File_Download,StepNodeTag:20240419144656197919,Title:Try异常,Note:')
        try:
            #鼠标点击
            self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:SXCC_ODS_File_Download,StepNodeTag:20240419144656198939,Title:鼠标点击,Note:')
            time.sleep(3)
            ichrome_firefox.do_click_pos_chrome(waitfor=10.000,run_mode='ctrl',button='left',curson='center',continue_on_error='break',title=r'PICC - 报表平台',url=r'http*',attrMap={"aaname":"*Excel*"})
            # For循环
            self.__logger.dlogs(job_no=self.job_no, logmsg='Flow:SXCC_ODS_File_Download,StepNodeTag:20240419144656197912,Title:For循环,Note:')
            for x in range(1,601):
                #输出
                self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:SXCC_ODS_File_Download,StepNodeTag:20240419144656197934,Title:输出,Note:')
                rpa_str.iprints("加载次数："+str(x))
                #元素是否存在
                self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:SXCC_ODS_File_Download,StepNodeTag:20240419144656197932,Title:元素是否存在,Note:')
                tvar_20240419144656197933=ichrome_firefox.is_element_existed_in_chrome(waitfor=5.000,curson='center',title=r'IBM Cognos Viewer',url=r'http*',attrMap={"xpath":"//*[@id=\"CVReport_NS_\"]/table[1]/tbody[1]/tr[1]/td[2]"})
                # IF分支
                self.__logger.dlogs(job_no=self.job_no, logmsg='Flow:SXCC_ODS_File_Download,StepNodeTag:20240419144656198944,Title:IF分支,Note:')
                if tvar_20240419144656197933:
                    #输出
                    self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:SXCC_ODS_File_Download,StepNodeTag:20240419144656197918,Title:输出,Note:')
                    rpa_str.iprints("已跳转到“另存为”界面，继续运行")
                    # Break中断
                    self.__logger.dlogs(job_no=self.job_no, logmsg='Flow:SXCC_ODS_File_Download,StepNodeTag:20240419144656197923,Title:Break中断,Note:')
                    break
                else:
                    #输出
                    self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:SXCC_ODS_File_Download,StepNodeTag:20240419144656197915,Title:输出,Note:')
                    rpa_str.iprints("未跳转到“另存为”界面，继续加载")
                    # IF分支
                    self.__logger.dlogs(job_no=self.job_no, logmsg='Flow:SXCC_ODS_File_Download,StepNodeTag:202404191453058671040,Title:IF分支,Note:')
                    if x==600:
                        #输出
                        self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:SXCC_ODS_File_Download,StepNodeTag:202404191453058671041,Title:输出,Note:')
                        rpa_str.iprints("ODS系统文件下载设置保存到指定路径失败（已加载600次），未知原因")
                        #消息框
                        self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:SXCC_ODS_File_Download,StepNodeTag:202404191453058671038,Title:消息框,Note:')
                        ibox.msgs_box("ODS系统文件下载设置保存到指定路径失败（已加载600次），请检查系统是否异常后，重新运行此组件，谢谢。",title=r"提示",timeout=0)
                    else:
                        pass
            #设置文本
            self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:SXCC_ODS_File_Download,StepNodeTag:20240419144656197929,Title:设置文本,Note:')
            time.sleep(3)
            selectorJson={"selector":[{"ControlType":"编辑","ControlTypeID":"0xC354","Index":"1"},{"ControlType":"组合框","ControlTypeID":"0xC353","Index":"1"},{"ControlType":"窗格","ControlTypeID":"0xC371","Index":"3"},{"ControlType":"窗格","ControlTypeID":"0xC371","Index":"5"},{"ControlType":"窗格","ControlTypeID":"0xC371","Index":"1"},{"ControlType":"窗格","ControlTypeID":"0xC371","Index":"1"}]}
            iautomation.set_text(waitfor=10.000,win_name=r'另存为',win_class=r'#32770',text=Str_File_Path,selector=selectorJson)
            #鼠标点击
            self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:SXCC_ODS_File_Download,StepNodeTag:20240419144656197935,Title:鼠标点击,Note:')
            selectorJson={"selector":[{"ControlType":"按钮","ControlTypeID":"0xC350","Index":"1"}]}
            iautomation.do_click(waitfor=10.000,run_mode='ctrl',button='left',curson='center',dpi=False,win_name=r'另存为',win_class=r'#32770',selector=selectorJson)
            time.sleep(1)
            #鼠标点击
            self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:SXCC_ODS_File_Download,StepNodeTag:202404251600182521107,Title:鼠标点击,Note:')
            selectorJson={"selector":[{"Name":'是(Y)'}]}
            iautomation.do_click(waitfor=2.000,run_mode='ctrl',button='left',curson='center',continue_on_error=r'continue',dpi=False,win_class=r'Chrome_WidgetWin_1',selector=selectorJson)
            #关闭窗口
            self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:SXCC_ODS_File_Download,StepNodeTag:20240419144656197916,Title:关闭窗口,Note:')
            time.sleep(3)
            iwin.do_win_close(waitfor=10.000,win_title=r'IBM',win_class=r'Chrome_WidgetWin_1')
            # While循环
            self.__logger.dlogs(job_no=self.job_no, logmsg='Flow:SXCC_ODS_File_Download,StepNodeTag:20240419144656198940,Title:While循环,Note:')
            while True:
                #目录是否存在
                self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:SXCC_ODS_File_Download,StepNodeTag:20240419144656197920,Title:目录是否存在,Note:')
                tvar_20240419144656197921=ifile.exist_dir(dir=Str_File_Path)
                # IF分支
                self.__logger.dlogs(job_no=self.job_no, logmsg='Flow:SXCC_ODS_File_Download,StepNodeTag:20240419144656197931,Title:IF分支,Note:')
                if tvar_20240419144656197921:
                    #输出
                    self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:SXCC_ODS_File_Download,StepNodeTag:20240419144656197922,Title:输出,Note:')
                    rpa_str.iprints(Str_File_Path+"文件下载完成，继续运行")
                    # Break中断
                    self.__logger.dlogs(job_no=self.job_no, logmsg='Flow:SXCC_ODS_File_Download,StepNodeTag:20240419144656197928,Title:Break中断,Note:')
                    break
                else:
                    #输出
                    self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:SXCC_ODS_File_Download,StepNodeTag:20240419144656197936,Title:输出,Note:')
                    rpa_str.iprints(Str_File_Path+"文件未下载完成，等待2秒，继续加载")
                    #等待时间
                    self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:SXCC_ODS_File_Download,StepNodeTag:20240419144656197924,Title:等待时间,Note:')
                    rpa_time.time_sleep(wait_time=2)
            #输出
            self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:SXCC_ODS_File_Download,StepNodeTag:202404191450369841018,Title:输出,Note:')
            rpa_str.iprints("ODS系统文件下载设置保存到指定路径成功")
            # IF分支
            self.__logger.dlogs(job_no=self.job_no, logmsg='Flow:SXCC_ODS_File_Download,StepNodeTag:202404191450369841017,Title:IF分支,Note:')
            if ("是" in Str_Pop_Up_Prompt) or ("Yes" in Str_Pop_Up_Prompt) or ("Y" in Str_Pop_Up_Prompt) :
                #输出
                self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:SXCC_ODS_File_Download,StepNodeTag:202404191450369841019,Title:输出,Note:')
                rpa_str.iprints("需要弹出提示")
                #消息框
                self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:SXCC_ODS_File_Download,StepNodeTag:202404191450369841020,Title:消息框,Note:')
                ibox.msgs_box("ODS系统文件下载设置保存到指定路径成功",title=r"提示",timeout=0)
            else:
                #输出
                self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:SXCC_ODS_File_Download,StepNodeTag:202404191450369841022,Title:输出,Note:')
                rpa_str.iprints("不需要弹出提示")
        except Exception as e:
            #输出
            self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:SXCC_ODS_File_Download,StepNodeTag:202404191449418801006,Title:输出,Note:')
            rpa_str.iprints("ODS系统文件下载设置保存到指定路径失败","异常信息为："+str(e))
            #消息框
            self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:SXCC_ODS_File_Download,StepNodeTag:202404191449418801007,Title:消息框,Note:')
            ibox.msgs_box("ODS系统文件下载设置保存到指定路径失败，请检查系统是否异常后，重新运行此组件，谢谢。","异常信息为："+str(e),title=r"提示",timeout=0)
            #代码块
            self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:SXCC_ODS_File_Download,StepNodeTag:202404191449418801009,Title:代码块,Note:停止')
            exit()
        finally:
            pass
        #输出
        self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:SXCC_ODS_File_Download,StepNodeTag:20240419144438053842,Title:输出,Note:')
        rpa_str.iprints("SXCC_ODS_File_Download End")
      
    def SXCC_ODS_Report_Search(self,Str_Report_Name="分年期首年期交保费收入表(new)",Str_Pop_Up_Prompt="是"):
        '''ODS系统报表搜索进入相关页面（谷歌浏览器，报表平台）\n（SXCC_ODS_Report_Search）\n1.修改查询后等待时间\n'''
        # 序列
        self.__logger.dlogs(job_no=self.job_no, logmsg='Flow:SXCC_ODS_Report_Search,StepNodeTag:20240419142243794315,Title:序列,Note:')
        #输出
        self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:SXCC_ODS_Report_Search,StepNodeTag:20240419142243794316,Title:输出,Note:')
        rpa_str.iprints("SXCC_ODS_Report_Search Start")
        # Try异常
        self.__logger.dlogs(job_no=self.job_no, logmsg='Flow:SXCC_ODS_Report_Search,StepNodeTag:20240419142642600482,Title:Try异常,Note:')
        try:
            #鼠标点击
            self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:SXCC_ODS_Report_Search,StepNodeTag:20240419142642600487,Title:鼠标点击,Note:')
            time.sleep(2)
            ichrome_firefox.do_click_pos_chrome(waitfor=10.000,run_mode='ctrl',button='left',curson='center',continue_on_error='break',title=r'PICC - 报表平台',url=r'http*',attrMap={"aaname":"报表搜索"})
            time.sleep(2)
            #设置文本
            self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:SXCC_ODS_Report_Search,StepNodeTag:20240419142642601488,Title:设置文本,Note:')
            ichrome_firefox.set_element_val_chrome(waitfor=10.000,text=Str_Report_Name,title=r'PICC - 报表平台',url=r'http*',attrMap={"xpath":"//*[@id=\"searchReport\"]"})
            #鼠标点击
            self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:SXCC_ODS_Report_Search,StepNodeTag:20240419142642600472,Title:鼠标点击,Note:')
            ichrome_firefox.do_click_pos_chrome(waitfor=10.000,run_mode='ctrl',button='left',curson='center',continue_on_error='break',title=r'PICC - 报表平台',url=r'http*',attrMap={"xpath":"//*[@id=\"searchReportBtn\"]"})
            #等待时间
            self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:SXCC_ODS_Report_Search,StepNodeTag:20240419142642601502,Title:等待时间,Note:')
            rpa_time.time_sleep(wait_time=10)
            #鼠标点击
            self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:SXCC_ODS_Report_Search,StepNodeTag:20240419142642601489,Title:鼠标点击,Note:')
            ichrome_firefox.do_click_pos_chrome(waitfor=10.000,run_mode='ctrl',button='left',curson='center',continue_on_error='break',title=r'PICC - 报表平台',url=r'http*',attrMap={"xpath":"//*[@id=\"serachTable\"]/tbody[1]/tr[1]/td[2]/a[1]"})
            # For循环
            self.__logger.dlogs(job_no=self.job_no, logmsg='Flow:SXCC_ODS_Report_Search,StepNodeTag:20240419142642601491,Title:For循环,Note:')
            for x in range(1,301):
                #输出
                self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:SXCC_ODS_Report_Search,StepNodeTag:20240419142642600485,Title:输出,Note:')
                rpa_str.iprints("加载次数："+str(x))
                #元素是否存在
                self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:SXCC_ODS_Report_Search,StepNodeTag:20240419142642600480,Title:元素是否存在,Note:')
                tvar_20240419142642600481=ichrome_firefox.is_element_existed_in_chrome(waitfor=2.000,curson='center',title=r'PICC - 报表平台',url=r'http*',attrMap={"xpath":"//*[@id=\"query\"]"})
                # IF分支
                self.__logger.dlogs(job_no=self.job_no, logmsg='Flow:SXCC_ODS_Report_Search,StepNodeTag:20240419142642601504,Title:IF分支,Note:')
                if tvar_20240419142642600481:
                    #输出
                    self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:SXCC_ODS_Report_Search,StepNodeTag:20240419142642600477,Title:输出,Note:')
                    rpa_str.iprints("已跳转到相关界面，继续运行")
                    # Break中断
                    self.__logger.dlogs(job_no=self.job_no, logmsg='Flow:SXCC_ODS_Report_Search,StepNodeTag:20240419142642600479,Title:Break中断,Note:')
                    break
                else:
                    #输出
                    self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:SXCC_ODS_Report_Search,StepNodeTag:20240419142642600484,Title:输出,Note:')
                    rpa_str.iprints("未跳转到相关报表界面，继续加载")
                    # IF分支
                    self.__logger.dlogs(job_no=self.job_no, logmsg='Flow:SXCC_ODS_Report_Search,StepNodeTag:20240419143102364584,Title:IF分支,Note:')
                    if x==300:
                        #输出
                        self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:SXCC_ODS_Report_Search,StepNodeTag:20240419143139136594,Title:输出,Note:')
                        rpa_str.iprints("ODS系统报表搜索进入相关页面失败（已加载300次），未知原因")
                        #消息框
                        self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:SXCC_ODS_Report_Search,StepNodeTag:20240419143200565603,Title:消息框,Note:')
                        ibox.msgs_box("ODS系统报表搜索进入相关页面失败（已加载300次），请检查系统是否异常后，重新运行此组件，谢谢。",title=r"提示",timeout=0)
                    else:
                        pass
            #输出
            self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:SXCC_ODS_Report_Search,StepNodeTag:20240419143307420615,Title:输出,Note:')
            rpa_str.iprints("ODS系统报表搜索进入相关页面成功")
            # IF分支
            self.__logger.dlogs(job_no=self.job_no, logmsg='Flow:SXCC_ODS_Report_Search,StepNodeTag:20240419143330599622,Title:IF分支,Note:')
            if ("是" in Str_Pop_Up_Prompt) or ("Yes" in Str_Pop_Up_Prompt) or ("Y" in Str_Pop_Up_Prompt) :
                #输出
                self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:SXCC_ODS_Report_Search,StepNodeTag:20240419143330599623,Title:输出,Note:')
                rpa_str.iprints("需要弹出提示")
                #消息框
                self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:SXCC_ODS_Report_Search,StepNodeTag:20240419143330599624,Title:消息框,Note:')
                ibox.msgs_box("ODS系统报表搜索进入相关页面成功",title=r"提示",timeout=0)
            else:
                #输出
                self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:SXCC_ODS_Report_Search,StepNodeTag:20240419143330599621,Title:输出,Note:')
                rpa_str.iprints("不需要弹出提示")
        except Exception as e:
            #输出
            self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:SXCC_ODS_Report_Search,StepNodeTag:20240419143443405638,Title:输出,Note:')
            rpa_str.iprints("ODS系统报表搜索进入相关页面失败","异常信息为："+str(e))
            #消息框
            self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:SXCC_ODS_Report_Search,StepNodeTag:20240419143443405639,Title:消息框,Note:')
            ibox.msgs_box("ODS系统报表搜索进入相关页面失败，请检查系统是否异常后，重新运行此组件，谢谢。","异常信息为："+str(e),title=r"提示",timeout=0)
            #代码块
            self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:SXCC_ODS_Report_Search,StepNodeTag:20240419143443405641,Title:代码块,Note:停止')
            exit()
        finally:
            pass
        #输出
        self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:SXCC_ODS_Report_Search,StepNodeTag:20240419142243794314,Title:输出,Note:')
        rpa_str.iprints("SXCC_ODS_Report_Search End")
      
    def flow1(self):
        Str_Image_Path=r"C:\Users\app_oper\Desktop\新建文件夹\截图20241115095731853.png"
        Str_Identifying_Code_Text=None
        #代码块
        self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:flow1,StepNodeTag:2024111509593545452,Title:代码块,Note:OCR生产环境，验证码图片转文本')
        from PIL import Image
        import os
        import urllib
        import requests
        import base64
        import json
        from urllib.parse import urlencode,quote
        
        def img_to_base64(img_path):
            with open(img_path, 'rb') as read:
                b64 = base64.b64encode(read.read())
            return b64
        def ocr_identify(file_path,APP_URL='',APP_KEY='',APP_SECRET=''):
        #    api_url = "http://10.111.10.208:80/ex-reco-web/ocr/v1/table_api"
        #    api_url = "http://10.111.10.208:80/ex-reco-web/ocr/v1/general"
        #     api_url = "http://api-south.infra.picclife.cn/ocr/v1/general?apikey=69444db5578d4210a0114eabba53e836"
        #     api_url = f"http://10.57.3.179:28121/ocr/v1/general?apikey={APP_KEY}"
            api_url = APP_URL
            image_base64 = img_to_base64(file_path)
            result = {}
            headers = {'content-type ':'application/x-www-from-urlencoded'}
        
            data = {'image_base64': image_base64, 
                    'app_key':APP_KEY,
                    'app_secret':APP_SECRET}
            r = requests.post(api_url, data=data, verify=False)
            result = json.loads(r.text)
            all_data = ''
            page_data = ''
            for i in result['result']:
                page_data = page_data + i['words'] + '\n'
            print(page_data)
            return page_data
            
        Str_Identifying_Code_Text=ocr_identify(file_path=Str_Image_Path,APP_URL="http://engine.group.ocr.piccnet:28121/ocr/v1/general",APP_KEY="18d14a6556ca4af994fb1a905f3e9a9d",APP_SECRET="ccd5ed6fdd584d98894c15a7ec19c09b")
      
    def Main(self):
        # 序列
        self.__logger.dlogs(job_no=self.job_no, logmsg='Flow:Main,StepNodeTag:20240419100137131282,Title:序列,Note:')
        #输出
        self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:Main,StepNodeTag:20240419100137137353,Title:输出,Note:')
        rpa_str.iprints("Main Start")
        #输出
        self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:Main,StepNodeTag:20240419100137129266,Title:输出,Note:')
        rpa_str.iprints("Main End")
 
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
    pro = SXCC_ODS_Related_Operations_P(robot_no=robot_no,proc_no=proc_no,job_no=job_no,input_arg=input_arg)
    pro.Main()
