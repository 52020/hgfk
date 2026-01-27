# coding=utf-8
# 编译日期：2024-04-24 16:53:50
# 版权所有：www.i-search.com.cn
import ubpa.init_input as iinput
from ubpa.base_util import StdOutHook, ExceptionHandler
import ubpa.itools.rpa_str as rpa_str
import ubpa.ibox as ibox
import string
import time
import pdb
from ubpa.ilog import ILog
import getopt
from sys import argv
import sys
import os
from ubpa.base_img import *

class SXCC_Number_Related_Operations:
     
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
      
    def SXCC_Number_To_Chine_Uppercase(self,Int_Number=3,Str_Pop_Up_Prompt="是"):
        '''把数字转换成中文大写\n（SXCC_Number_To_Chine_Uppercase）\n1.初始化\n'''
        Str_Process_Name="把数字转换成中文大写"
        Str_Chinese_Uppercase=""
        # 序列
        self.__logger.dlogs(job_no=self.job_no, logmsg='Flow:SXCC_Number_To_Chine_Uppercase,StepNodeTag:20240419163620938214,Title:序列,Note:')
        #输出
        self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:SXCC_Number_To_Chine_Uppercase,StepNodeTag:20240419163620938217,Title:输出,Note:')
        rpa_str.iprints("SXCC_Number_To_Chine_Uppercase Start")
        # Try异常
        self.__logger.dlogs(job_no=self.job_no, logmsg='Flow:SXCC_Number_To_Chine_Uppercase,StepNodeTag:20240419163620938216,Title:Try异常,Note:')
        try:
            #代码块
            self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:SXCC_Number_To_Chine_Uppercase,StepNodeTag:20240419163620938207,Title:代码块,Note:把数字转换成中文大写')
            numberList = ['零', '一', '二', '三', '四', '五', '六', '七', '八', '九']
            unitList = ["", "十", "百", "千", "万", '十万', '百万', '千万', '亿', '十亿', '百亿', '千亿', '万亿', '兆']
            # 转为字符串 获取传入字符串长度
            strnumber = str(Int_Number)
            lennumber = len(strnumber)
            # 需要获取相关单位
            Str_Chinese_Uppercase = ''
            for i in range(lennumber):
                # print('第{}次,Str_Chinese_Uppercase值为:{}'.format(i,Str_Chinese_Uppercase))
                if int(strnumber[i]) != 0:
                    # 判断万出现的次数 如果多次删除现有的 万 字 防止出现 五十万二万 重复
                    for unit in ['万', '亿']:
                        if Str_Chinese_Uppercase.count(unit) > 1:
                            print(Str_Chinese_Uppercase.count(unit))
                            Str_Chinese_Uppercase = Str_Chinese_Uppercase.replace(unit, '', 1)
                    # 获取当前数字对应的汉字 + 单位
                    Str_Chinese_Uppercase = Str_Chinese_Uppercase + numberList[int(strnumber[i])] + unitList[lennumber - i - 1]
                # 如果前一位也是零 那么直接跳出循环重新执行 //防止
                elif int(strnumber[i - 1]) == 0:
                    continue
                else:
                    # 如果都不是 也就是为 那么则直接加一个零
                    Str_Chinese_Uppercase = Str_Chinese_Uppercase + numberList[int(strnumber[i])]
            # 返回值 // rstrip 删除结尾的所有零
            Str_Chinese_Uppercase = Str_Chinese_Uppercase.rstrip('零')
            if (Int_Number >= 10 and Int_Number < 20):
                Str_Chinese_Uppercase=Str_Chinese_Uppercase[1:]
            
            print(Str_Chinese_Uppercase)
            #输出
            self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:SXCC_Number_To_Chine_Uppercase,StepNodeTag:20240419163620938219,Title:输出,Note:')
            rpa_str.iprints(Str_Process_Name+"成功")
            # IF分支
            self.__logger.dlogs(job_no=self.job_no, logmsg='Flow:SXCC_Number_To_Chine_Uppercase,StepNodeTag:20240419163620938218,Title:IF分支,Note:')
            if ("是" in Str_Pop_Up_Prompt) or ("Yes" in Str_Pop_Up_Prompt) or ("Y" in Str_Pop_Up_Prompt) :
                #输出
                self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:SXCC_Number_To_Chine_Uppercase,StepNodeTag:20240419163620938208,Title:输出,Note:')
                rpa_str.iprints("需要弹出提示")
                #消息框
                self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:SXCC_Number_To_Chine_Uppercase,StepNodeTag:20240419163620938211,Title:消息框,Note:')
                ibox.msgs_box(Str_Process_Name+"成功",title=r"提示",timeout=0)
            else:
                #输出
                self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:SXCC_Number_To_Chine_Uppercase,StepNodeTag:20240419163620938209,Title:输出,Note:')
                rpa_str.iprints("不需要弹出提示")
        except Exception as e:
            #输出
            self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:SXCC_Number_To_Chine_Uppercase,StepNodeTag:20240419163620938212,Title:输出,Note:')
            rpa_str.iprints(Str_Process_Name+"失败，请检查系统是否异常后，重新运行此组件，谢谢。","异常信息为："+str(e))
            #消息框
            self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:SXCC_Number_To_Chine_Uppercase,StepNodeTag:20240419163620938221,Title:消息框,Note:')
            ibox.msgs_box(Str_Process_Name+"失败，请检查系统是否异常后，重新运行此组件，谢谢。","异常信息为："+str(e),title=r"提示",timeout=0)
            #代码块
            self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:SXCC_Number_To_Chine_Uppercase,StepNodeTag:20240419163620938220,Title:代码块,Note:停止')
            exit()
        finally:
            pass
        #输出
        self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:SXCC_Number_To_Chine_Uppercase,StepNodeTag:20240419163620938213,Title:输出,Note:')
        rpa_str.iprints("SXCC_Number_To_Chine_Uppercase End")
        # Return返回
        self.__logger.dlogs(job_no=self.job_no, logmsg='Flow:SXCC_Number_To_Chine_Uppercase,StepNodeTag:20240419163620938210,Title:Return返回,Note:')
        return Str_Chinese_Uppercase
      
    def SXCC_Number_To_Letter(self,Int_Number=3,Str_Pop_Up_Prompt="是"):
        '''把数字转换成对应的字母\n（SXCC_Number_To_Letter）\n1.初始化\n'''
        Str_Process_Name="把数字转换成对应的字母"
        Str_Letter=""
        # 序列
        self.__logger.dlogs(job_no=self.job_no, logmsg='Flow:SXCC_Number_To_Letter,StepNodeTag:202404191537293972369,Title:序列,Note:')
        #输出
        self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:SXCC_Number_To_Letter,StepNodeTag:202404191537293972368,Title:输出,Note:')
        rpa_str.iprints("SXCC_Number_To_Letter Start")
        # Try异常
        self.__logger.dlogs(job_no=self.job_no, logmsg='Flow:SXCC_Number_To_Letter,StepNodeTag:202404191537294242393,Title:Try异常,Note:')
        try:
            #代码块
            self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:SXCC_Number_To_Letter,StepNodeTag:202404191550599792667,Title:代码块,Note:把数字转换成对应的字母')
            # 利用ASCII码把数字转换成对应的字母
            # Int_Number从0到25，代表A到Z
            Str_Letter=string.ascii_uppercase[Int_Number]
            print(Str_Letter)
            #输出
            self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:SXCC_Number_To_Letter,StepNodeTag:202404191556237462700,Title:输出,Note:')
            rpa_str.iprints(Str_Process_Name+"成功")
            # IF分支
            self.__logger.dlogs(job_no=self.job_no, logmsg='Flow:SXCC_Number_To_Letter,StepNodeTag:202404191556237462696,Title:IF分支,Note:')
            if ("是" in Str_Pop_Up_Prompt) or ("Yes" in Str_Pop_Up_Prompt) or ("Y" in Str_Pop_Up_Prompt) :
                #输出
                self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:SXCC_Number_To_Letter,StepNodeTag:202404191556237462701,Title:输出,Note:')
                rpa_str.iprints("需要弹出提示")
                #消息框
                self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:SXCC_Number_To_Letter,StepNodeTag:202404191556237462698,Title:消息框,Note:')
                ibox.msgs_box(Str_Process_Name+"成功",title=r"提示",timeout=0)
            else:
                #输出
                self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:SXCC_Number_To_Letter,StepNodeTag:202404191556237462697,Title:输出,Note:')
                rpa_str.iprints("不需要弹出提示")
        except Exception as e:
            #输出
            self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:SXCC_Number_To_Letter,StepNodeTag:202404191557044532724,Title:输出,Note:')
            rpa_str.iprints(Str_Process_Name+"失败，请检查系统是否异常后，重新运行此组件，谢谢。","异常信息为："+str(e))
            #消息框
            self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:SXCC_Number_To_Letter,StepNodeTag:202404191557044532722,Title:消息框,Note:')
            ibox.msgs_box(Str_Process_Name+"失败，请检查系统是否异常后，重新运行此组件，谢谢。","异常信息为："+str(e),title=r"提示",timeout=0)
            #代码块
            self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:SXCC_Number_To_Letter,StepNodeTag:202404191557044532725,Title:代码块,Note:停止')
            exit()
        finally:
            pass
        #输出
        self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:SXCC_Number_To_Letter,StepNodeTag:202404191537293972367,Title:输出,Note:')
        rpa_str.iprints("SXCC_Number_To_Letter End")
        # Return返回
        self.__logger.dlogs(job_no=self.job_no, logmsg='Flow:SXCC_Number_To_Letter,StepNodeTag:2024041916230606275,Title:Return返回,Note:')
        return Str_Letter
      
    def Main(self):
        # 序列
        self.__logger.dlogs(job_no=self.job_no, logmsg='Flow:Main,StepNodeTag:202404191536221862309,Title:序列,Note:')
        #输出
        self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:Main,StepNodeTag:202404191536221862307,Title:输出,Note:')
        rpa_str.iprints("Main Start")
        #输出
        self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:Main,StepNodeTag:202404191536221862308,Title:输出,Note:')
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
    pro = SXCC_Number_Related_Operations(robot_no=robot_no,proc_no=proc_no,job_no=job_no,input_arg=input_arg)
    pro.Main()
