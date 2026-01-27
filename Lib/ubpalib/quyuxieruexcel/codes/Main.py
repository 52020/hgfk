# coding=utf-8
# 编译日期：2023-12-08 10:44:41
# 版权所有：www.i-search.com.cn
import ubpa.init_input as iinput
from ubpa.base_util import StdOutHook, ExceptionHandler
import itertools
import ubpa.iexcel as iexcel
import ubpa.iplatform as iplatform
import time
import pdb
from ubpa.ilog import ILog
import getopt
from sys import argv
import sys
import os
from ubpa.base_img import *

class quyuxieruexcel:
     
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
      
    def Main(self,data=None,file=None,danyuange="A1",gongzuobiao="Sheet1",dakaifangshi=0):
        desktop=None
        #设置变量
        self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:Main,StepNodeTag:20231208101242910271,Title:设置变量,Note:')
        iplatform.setAsset(name=dakaifangshi,value="应用" if dakaifangshi else 'file',robot_no=self.robot_no,job_no=self.job_no,proc_no=self.proc_no)
        # For循环
        self.__logger.dlogs(job_no=self.job_no, logmsg='Flow:Main,StepNodeTag:202312071743591216528,Title:For循环,Note:')
        for tvar_202312071743591216529 in data:
            #写入行
            self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:Main,StepNodeTag:202312071743591216527,Title:写入行,Note:')
            iexcel.write_row(path=file,text=tvar_202312071743591216529,sheet=gongzuobiao,cell=danyuange,file_type=dakaifangshi)
            #代码块
            self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:Main,StepNodeTag:202312071809430996821,Title:代码块,Note:')
            danyuange = ''.join([str(int(''.join(g)) + 1) if k else ''.join(g) for k, g in itertools.groupby(danyuange, str.isdigit)])
 
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
    pro = quyuxieruexcel(robot_no=robot_no,proc_no=proc_no,job_no=job_no,input_arg=input_arg)
    pro.Main()
