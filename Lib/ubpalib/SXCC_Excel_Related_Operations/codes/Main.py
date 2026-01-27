# coding=utf-8
# 编译日期：2024-04-24 16:51:50
# 版权所有：www.i-search.com.cn
import ubpa.init_input as iinput
from ubpa.base_util import StdOutHook, ExceptionHandler
import ubpa.itools.rpa_str as rpa_str
import ubpa.ibox as ibox
import xlwings as xw
import os
import openpyxl
from comtypes.client import CreateObject
import time
import pdb
from ubpa.ilog import ILog
import getopt
from sys import argv
import sys
import os
from ubpa.base_img import *

class SXCC_Excel_Related_Operations:
     
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
      
    def SXCC_Excel_2_Sheet_Copy_Paste(self,Str_Input_Excel_Path=None,Str_Input_Sheet_Name=None,Str_Output_Excel_Path=None,Str_Output_Sheet_Name=None,Str_Pop_Up_Prompt="是"):
        '''Excel中两个Sheet页全部复制粘贴\n（SXCC_Excel_2_Sheet_Copy_Paste）\n1.初始化\n'''
        Str_Process_Name="Excel中两个Sheet页全部复制粘贴"
        # 序列
        self.__logger.dlogs(job_no=self.job_no, logmsg='Flow:SXCC_Excel_2_Sheet_Copy_Paste,StepNodeTag:202404191537293972369,Title:序列,Note:')
        #输出
        self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:SXCC_Excel_2_Sheet_Copy_Paste,StepNodeTag:202404191537293972368,Title:输出,Note:')
        rpa_str.iprints("SXCC_Excel_2_Sheet_Copy_Paste Start")
        # Try异常
        self.__logger.dlogs(job_no=self.job_no, logmsg='Flow:SXCC_Excel_2_Sheet_Copy_Paste,StepNodeTag:202404191537294242393,Title:Try异常,Note:')
        try:
            #代码块
            self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:SXCC_Excel_2_Sheet_Copy_Paste,StepNodeTag:202404191550599792667,Title:代码块,Note:Excel中两个Sheet页全部复制粘贴')
            app = xw.App(visible=False, add_book=False)  # 界面设置
            app.display_alerts = False  # 关闭提示信息
            app.screen_updating = False  # 关闭显示更新
            
            # 打开第一个表，源表格（复制表格）
            wb1 = app.books.open(Str_Input_Excel_Path)
            wss1 = wb1.sheets
            for i in range(0,len(wss1)):
                if wss1[i].name==Str_Input_Sheet_Name:
                    ws1=wss1[i]
                    break
            
            # 打开第二个表，目标表格（粘贴表格）
            wb2 = app.books.open(Str_Output_Excel_Path)
            ws2 = wb2.sheets.add(Str_Output_Sheet_Name, before=wb2.sheets[0].name)
            
            # 我的理解是，"A1"就是在excel里点一下A1，然后ctrl + shift + →↓ ，全选
            ws1.api.Range("A1").CurrentRegion.Copy(ws2.api.Range("A1"))
            ws2.api.Range("A1").Select()
            
            # 自动调整行高列宽
            # ws2.autofit()
            
            wb1.save()
            wb1.close()
            wb2.save()
            wb2.close()
            app.quit()
            
            
            #输出
            self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:SXCC_Excel_2_Sheet_Copy_Paste,StepNodeTag:202404191556237462700,Title:输出,Note:')
            rpa_str.iprints(Str_Process_Name+"成功")
            # IF分支
            self.__logger.dlogs(job_no=self.job_no, logmsg='Flow:SXCC_Excel_2_Sheet_Copy_Paste,StepNodeTag:202404191556237462696,Title:IF分支,Note:')
            if ("是" in Str_Pop_Up_Prompt) or ("Yes" in Str_Pop_Up_Prompt) or ("Y" in Str_Pop_Up_Prompt) :
                #输出
                self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:SXCC_Excel_2_Sheet_Copy_Paste,StepNodeTag:202404191556237462701,Title:输出,Note:')
                rpa_str.iprints("需要弹出提示")
                #消息框
                self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:SXCC_Excel_2_Sheet_Copy_Paste,StepNodeTag:202404191556237462698,Title:消息框,Note:')
                ibox.msgs_box(Str_Process_Name+"成功",title=r"提示",timeout=0)
            else:
                #输出
                self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:SXCC_Excel_2_Sheet_Copy_Paste,StepNodeTag:202404191556237462697,Title:输出,Note:')
                rpa_str.iprints("不需要弹出提示")
        except Exception as e:
            #输出
            self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:SXCC_Excel_2_Sheet_Copy_Paste,StepNodeTag:202404191557044532724,Title:输出,Note:')
            rpa_str.iprints(Str_Process_Name+"失败，请检查是否关闭这两个Excel表格，系统是否异常后，重新运行此组件，谢谢。","异常信息为："+str(e))
            #消息框
            self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:SXCC_Excel_2_Sheet_Copy_Paste,StepNodeTag:202404191557044532722,Title:消息框,Note:')
            ibox.msgs_box(Str_Process_Name+"失败，请检查是否关闭这两个Excel表格，系统是否异常后，重新运行此组件，谢谢。","异常信息为："+str(e),title=r"提示",timeout=0)
            #代码块
            self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:SXCC_Excel_2_Sheet_Copy_Paste,StepNodeTag:202404191557044532725,Title:代码块,Note:停止')
            exit()
        finally:
            pass
        #输出
        self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:SXCC_Excel_2_Sheet_Copy_Paste,StepNodeTag:202404191537293972367,Title:输出,Note:')
        rpa_str.iprints("SXCC_Excel_2_Sheet_Copy_Paste End")
      
    def SXCC_Excel_To_PDF(self,Str_Excel_Path=None,Str_PDF_Path=None,Str_Pop_Up_Prompt="是"):
        '''Excel导出为PDF\n（SXCC_Excel_To_PDF）\n1.初始化\n'''
        Str_Process_Name="Excel导出为PDF"
        # 序列
        self.__logger.dlogs(job_no=self.job_no, logmsg='Flow:SXCC_Excel_To_PDF,StepNodeTag:202404191602122262770,Title:序列,Note:')
        #输出
        self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:SXCC_Excel_To_PDF,StepNodeTag:202404191602122262767,Title:输出,Note:')
        rpa_str.iprints("SXCC_Excel_To_PDF Start")
        # Try异常
        self.__logger.dlogs(job_no=self.job_no, logmsg='Flow:SXCC_Excel_To_PDF,StepNodeTag:202404191602122262768,Title:Try异常,Note:')
        try:
            #代码块
            self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:SXCC_Excel_To_PDF,StepNodeTag:202404191602122262766,Title:代码块,Note:Excel导出为PDF')
            # 打开Excel应用  
            excel = CreateObject("Excel.Application")  
            excel.Visible = False  # 不显示Excel窗口  
            
            # 打开Excel文件  
            workbook = excel.Workbooks.Open(Str_Excel_Path)  
            
            # 创建一个新的PDF文件并保存所有工作表  
            workbook.ExportAsFixedFormat(0, Str_PDF_Path)  # 0代表导出为PDF格式  
            
            # 关闭Excel文件和应用  
            workbook.Save()  
            workbook.Close()  
            excel.Quit()  
            
            #输出
            self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:SXCC_Excel_To_PDF,StepNodeTag:202404191602122262762,Title:输出,Note:')
            rpa_str.iprints(Str_Process_Name+"成功")
            # IF分支
            self.__logger.dlogs(job_no=self.job_no, logmsg='Flow:SXCC_Excel_To_PDF,StepNodeTag:202404191602122262765,Title:IF分支,Note:')
            if ("是" in Str_Pop_Up_Prompt) or ("Yes" in Str_Pop_Up_Prompt) or ("Y" in Str_Pop_Up_Prompt) :
                #输出
                self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:SXCC_Excel_To_PDF,StepNodeTag:202404191602122262758,Title:输出,Note:')
                rpa_str.iprints("需要弹出提示")
                #消息框
                self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:SXCC_Excel_To_PDF,StepNodeTag:202404191602122262764,Title:消息框,Note:')
                ibox.msgs_box(Str_Process_Name+"成功",title=r"提示",timeout=0)
            else:
                #输出
                self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:SXCC_Excel_To_PDF,StepNodeTag:202404191602122262763,Title:输出,Note:')
                rpa_str.iprints("不需要弹出提示")
        except Exception as e:
            #输出
            self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:SXCC_Excel_To_PDF,StepNodeTag:202404191602122262759,Title:输出,Note:')
            rpa_str.iprints(Str_Process_Name+"失败，请检查是否关闭这个Excel表格，系统是否异常后，重新运行此组件，谢谢。","异常信息为："+str(e))
            #消息框
            self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:SXCC_Excel_To_PDF,StepNodeTag:202404191602122262760,Title:消息框,Note:')
            ibox.msgs_box(Str_Process_Name+"失败，请检查是否关闭这个Excel表格，系统是否异常后，重新运行此组件，谢谢。","异常信息为："+str(e),title=r"提示",timeout=0)
            #代码块
            self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:SXCC_Excel_To_PDF,StepNodeTag:202404191602122262761,Title:代码块,Note:停止')
            exit()
        finally:
            pass
        #输出
        self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:SXCC_Excel_To_PDF,StepNodeTag:202404191602122262771,Title:输出,Note:')
        rpa_str.iprints("SXCC_Excel_To_PDF End")
      
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
    pro = SXCC_Excel_Related_Operations(robot_no=robot_no,proc_no=proc_no,job_no=job_no,input_arg=input_arg)
    pro.Main()
