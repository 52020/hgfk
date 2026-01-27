# coding=utf-8
# 编译日期：2024-04-24 17:01:14
# 版权所有：www.i-search.com.cn
import ubpa.init_input as iinput
from ubpa.base_util import StdOutHook, ExceptionHandler
import ubpa.itools.rpa_str as rpa_str
import ubpa.ibox as ibox
import platform
import time
import pdb
from ubpa.ilog import ILog
import getopt
from sys import argv
import sys
import os
from ubpa.base_img import *

class SXCC_System_Information:
     
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
      
    def SXCC_System_Information(self,Str_Pop_Up_Prompt="是"):
        '''获取操作系统信息\n（SXCC_System_Information）\n1.初始化\n'''
        Str_Process_Name="获取操作系统信息"
        Dict_System_Information={}
        # 序列
        self.__logger.dlogs(job_no=self.job_no, logmsg='Flow:SXCC_System_Information,StepNodeTag:20240419161323676353,Title:序列,Note:')
        #输出
        self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:SXCC_System_Information,StepNodeTag:20240419161323676356,Title:输出,Note:')
        rpa_str.iprints("SXCC_System_Information Start")
        # Try异常
        self.__logger.dlogs(job_no=self.job_no, logmsg='Flow:SXCC_System_Information,StepNodeTag:20240419161323676355,Title:Try异常,Note:')
        try:
            #代码块
            self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:SXCC_System_Information,StepNodeTag:20240419161323676357,Title:代码块,Note:获取操作系统信息')
            # 获取操作系统名称
            os_name = platform.system()
            
            # 获取操作系统版本
            os_release = platform.release()
            
            # 获取操作系统位数
            os_arch = platform.architecture()[0]
            
            Dict_System_Information={"操作系统名称":os_name,"操作系统版本":os_release,"操作系统位数":os_arch}
            print(Dict_System_Information)
            #输出
            self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:SXCC_System_Information,StepNodeTag:20240419161323676361,Title:输出,Note:')
            rpa_str.iprints(Str_Process_Name+"成功")
            # IF分支
            self.__logger.dlogs(job_no=self.job_no, logmsg='Flow:SXCC_System_Information,StepNodeTag:20240419161323676358,Title:IF分支,Note:')
            if ("是" in Str_Pop_Up_Prompt) or ("Yes" in Str_Pop_Up_Prompt) or ("Y" in Str_Pop_Up_Prompt) :
                #输出
                self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:SXCC_System_Information,StepNodeTag:20240419161323676365,Title:输出,Note:')
                rpa_str.iprints("需要弹出提示")
                #消息框
                self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:SXCC_System_Information,StepNodeTag:20240419161323676359,Title:消息框,Note:')
                ibox.msgs_box(Str_Process_Name+"成功",title=r"提示",timeout=0)
            else:
                #输出
                self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:SXCC_System_Information,StepNodeTag:20240419161323676360,Title:输出,Note:')
                rpa_str.iprints("不需要弹出提示")
        except Exception as e:
            #输出
            self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:SXCC_System_Information,StepNodeTag:20240419161323676364,Title:输出,Note:')
            rpa_str.iprints(Str_Process_Name+"失败，请检查系统是否异常后，重新运行此组件，谢谢。","异常信息为："+str(e))
            #消息框
            self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:SXCC_System_Information,StepNodeTag:20240419161323676363,Title:消息框,Note:')
            ibox.msgs_box(Str_Process_Name+"失败，请检查系统是否异常后，重新运行此组件，谢谢。","异常信息为："+str(e),title=r"提示",timeout=0)
            #代码块
            self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:SXCC_System_Information,StepNodeTag:20240419161323676362,Title:代码块,Note:停止')
            exit()
        finally:
            pass
        #输出
        self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:SXCC_System_Information,StepNodeTag:20240419161323676352,Title:输出,Note:')
        rpa_str.iprints("SXCC_System_Information End")
        # Return返回
        self.__logger.dlogs(job_no=self.job_no, logmsg='Flow:SXCC_System_Information,StepNodeTag:2024042316380840761,Title:Return返回,Note:')
        return Dict_System_Information
      
    def Main(self):
        # 序列
        self.__logger.dlogs(job_no=self.job_no, logmsg='Flow:Main,StepNodeTag:20240419161245883319,Title:序列,Note:')
        #输出
        self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:Main,StepNodeTag:20240419161245883317,Title:输出,Note:')
        rpa_str.iprints("Main Start")
        #输出
        self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:Main,StepNodeTag:20240419161245883318,Title:输出,Note:')
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
    pro = SXCC_System_Information(robot_no=robot_no,proc_no=proc_no,job_no=job_no,input_arg=input_arg)
    pro.Main()
