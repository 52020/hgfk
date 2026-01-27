# coding=utf-8
# 编译日期：2025-06-06 16:02:37
# 版权所有：www.i-search.com.cn
import ubpa.init_input as iinput
from ubpa.base_util import StdOutHook, ExceptionHandler
import ubpa.itools.rpa_str as rpa_str
import ubpa.ibox as ibox
import ubpa.iautomation as iautomation
import ubpa.itools.rpa_time as rpa_time
import ubpa.ifile as ifile
import time
import pdb
from ubpa.ilog import ILog
import getopt
from sys import argv
import sys
import os
from ubpa.base_img import *

class SXCC_File_Download:
     
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
      
    def SXCC_File_Download(self,Str_File_Path=r"C:\Users\Administrator\新建文件夹\文件下载测试.xlsx",Str_Pop_Up_Prompt="是"):
        '''文件下载设置保存到指定绝对路径\n（SXCC_File_Download）\n1.添加动态加载另存为窗口功能\n'''
        # 序列
        self.__logger.dlogs(job_no=self.job_no, logmsg='Flow:SXCC_File_Download,StepNodeTag:20240419144438086859,Title:序列,Note:')
        #输出
        self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:SXCC_File_Download,StepNodeTag:20240419144438086858,Title:输出,Note:')
        rpa_str.iprints("SXCC_File_Download Start")
        # Try异常
        self.__logger.dlogs(job_no=self.job_no, logmsg='Flow:SXCC_File_Download,StepNodeTag:20240419144656197919,Title:Try异常,Note:')
        try:
            # For循环
            self.__logger.dlogs(job_no=self.job_no, logmsg='Flow:SXCC_File_Download,StepNodeTag:2025060614164693427,Title:For循环,Note:')
            for i in range(1,61):
                #输出
                self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:SXCC_File_Download,StepNodeTag:2025060614172355430,Title:输出,Note:')
                rpa_str.iprints("另存为窗口加载次数："+str(i))
                #元素是否存在
                self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:SXCC_File_Download,StepNodeTag:2025060614175476632,Title:元素是否存在,Note:')
                selectorJson={"selector":[{"ControlType":"按钮","ControlTypeID":"0xC350","Index":"1"},{"ControlType":"对话框","ControlTypeID":"0xC370","Index":"1"}]}
                tvar_2025060614182984540=iautomation.is_element_existed_in_uia(waitfor=5.000,curson='center',win_class=r'Chrome_WidgetWin_1',selector=selectorJson)
                # IF分支
                self.__logger.dlogs(job_no=self.job_no, logmsg='Flow:SXCC_File_Download,StepNodeTag:20250606142910391112,Title:IF分支,Note:')
                if tvar_2025060614182984540:
                    #输出
                    self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:SXCC_File_Download,StepNodeTag:20250606142919350116,Title:输出,Note:')
                    rpa_str.iprints("另存为窗口加载成功，继续运行")
                    # Break中断
                    self.__logger.dlogs(job_no=self.job_no, logmsg='Flow:SXCC_File_Download,StepNodeTag:20250606143507070162,Title:Break中断,Note:')
                    break
                else:
                    #输出
                    self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:SXCC_File_Download,StepNodeTag:20250606142922951122,Title:输出,Note:')
                    rpa_str.iprints("另存为窗口加载失败，继续加载")
                    # IF分支
                    self.__logger.dlogs(job_no=self.job_no, logmsg='Flow:SXCC_File_Download,StepNodeTag:20250606142957814126,Title:IF分支,Note:')
                    if i==60:
                        #输出
                        self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:SXCC_File_Download,StepNodeTag:20250606143025937145,Title:输出,Note:')
                        rpa_str.iprints("另存为窗口加载60次，未加载成功，请查找原因，谢谢。")
                        #消息框
                        self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:SXCC_File_Download,StepNodeTag:20250606143025937147,Title:消息框,Note:')
                        ibox.msgs_box("另存为窗口加载60次，未加载成功，请查找原因，谢谢。",title=r"提示",timeout=0)
                        #代码块
                        self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:SXCC_File_Download,StepNodeTag:20250606143025937146,Title:代码块,Note:停止')
                        exit()
                    else:
                        pass
            #等待时间
            self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:SXCC_File_Download,StepNodeTag:20250606143341045157,Title:等待时间,Note:')
            rpa_time.time_sleep(wait_time=2)
            #设置文本
            self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:SXCC_File_Download,StepNodeTag:20240419144656197929,Title:设置文本,Note:')
            time.sleep(3)
            selectorJson={"selector":[{"ControlType":"编辑","ControlTypeID":"0xC354","Index":"1"},{"ControlType":"组合框","ControlTypeID":"0xC353","Index":"1"},{"ControlType":"窗格","ControlTypeID":"0xC371","Index":"3"},{"ControlType":"窗格","ControlTypeID":"0xC371","Index":"5"},{"ControlType":"窗格","ControlTypeID":"0xC371","Index":"1"},{"ControlType":"窗格","ControlTypeID":"0xC371","Index":"1"}]}
            iautomation.set_text(waitfor=10.000,win_class=r'#32770',text=Str_File_Path,selector=selectorJson)
            #鼠标点击
            self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:SXCC_File_Download,StepNodeTag:20240419144656197935,Title:鼠标点击,Note:')
            selectorJson={"selector":[{"ControlType":"按钮","ControlTypeID":"0xC350","Index":"1"}]}
            iautomation.do_click(waitfor=10.000,run_mode='ctrl',button='left',curson='center',dpi=False,win_class=r'#32770',selector=selectorJson)
            time.sleep(1)
            #鼠标点击
            self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:SXCC_File_Download,StepNodeTag:202404251600182521107,Title:鼠标点击,Note:')
            selectorJson={"selector":[{"ControlType":"按钮","ControlTypeID":"0xC350","Index":"1"},{"ControlType":"窗格","ControlTypeID":"0xC371","Index":"1"},{"ControlType":"对话框","ControlTypeID":"0xC370","Index":"1"},{"ControlType":"对话框","ControlTypeID":"0xC370","Index":"1"}]}
            iautomation.do_click(waitfor=2.000,run_mode='ctrl',button='left',curson='center',continue_on_error=r'continue',dpi=False,win_class=r'Chrome_WidgetWin_1',selector=selectorJson)
            # While循环
            self.__logger.dlogs(job_no=self.job_no, logmsg='Flow:SXCC_File_Download,StepNodeTag:20240419144656198940,Title:While循环,Note:')
            while True:
                #目录是否存在
                self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:SXCC_File_Download,StepNodeTag:20240419144656197920,Title:目录是否存在,Note:')
                tvar_20240419144656197921=ifile.exist_dir(dir=Str_File_Path)
                # IF分支
                self.__logger.dlogs(job_no=self.job_no, logmsg='Flow:SXCC_File_Download,StepNodeTag:20240419144656197931,Title:IF分支,Note:')
                if tvar_20240419144656197921:
                    #输出
                    self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:SXCC_File_Download,StepNodeTag:20240419144656197922,Title:输出,Note:')
                    rpa_str.iprints(Str_File_Path+"文件下载完成，继续运行")
                    # Break中断
                    self.__logger.dlogs(job_no=self.job_no, logmsg='Flow:SXCC_File_Download,StepNodeTag:20240419144656197928,Title:Break中断,Note:')
                    break
                else:
                    #输出
                    self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:SXCC_File_Download,StepNodeTag:20240419144656197936,Title:输出,Note:')
                    rpa_str.iprints(Str_File_Path+"文件未下载完成，等待2秒，继续加载")
                    #等待时间
                    self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:SXCC_File_Download,StepNodeTag:20240419144656197924,Title:等待时间,Note:')
                    rpa_time.time_sleep(wait_time=2)
            #输出
            self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:SXCC_File_Download,StepNodeTag:202404191450369841018,Title:输出,Note:')
            rpa_str.iprints("文件下载设置保存到指定绝对路径成功")
            # IF分支
            self.__logger.dlogs(job_no=self.job_no, logmsg='Flow:SXCC_File_Download,StepNodeTag:202404191450369841017,Title:IF分支,Note:')
            if ("是" in Str_Pop_Up_Prompt) or ("Yes" in Str_Pop_Up_Prompt) or ("Y" in Str_Pop_Up_Prompt) :
                #输出
                self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:SXCC_File_Download,StepNodeTag:202404191450369841019,Title:输出,Note:')
                rpa_str.iprints("需要弹出提示")
                #消息框
                self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:SXCC_File_Download,StepNodeTag:202404191450369841020,Title:消息框,Note:')
                ibox.msgs_box("文件下载设置保存到指定绝对路径成功",title=r"提示",timeout=0)
            else:
                #输出
                self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:SXCC_File_Download,StepNodeTag:202404191450369841022,Title:输出,Note:')
                rpa_str.iprints("不需要弹出提示")
        except Exception as e:
            #输出
            self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:SXCC_File_Download,StepNodeTag:202404191449418801006,Title:输出,Note:')
            rpa_str.iprints("文件下载设置保存到指定绝对路径失败","异常信息为："+str(e))
            #消息框
            self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:SXCC_File_Download,StepNodeTag:202404191449418801007,Title:消息框,Note:')
            ibox.msgs_box("文件下载设置保存到指定绝对路径失败，请检查系统是否异常后，重新运行此组件，谢谢。","异常信息为："+str(e),title=r"提示",timeout=0)
            #代码块
            self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:SXCC_File_Download,StepNodeTag:202404191449418801009,Title:代码块,Note:停止')
            exit()
        finally:
            pass
        #输出
        self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:SXCC_File_Download,StepNodeTag:20240419144438053842,Title:输出,Note:')
        rpa_str.iprints("SXCC_File_Download End")
      
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
    pro = SXCC_File_Download(robot_no=robot_no,proc_no=proc_no,job_no=job_no,input_arg=input_arg)
    pro.Main()
