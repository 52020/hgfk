# coding=utf-8
# 编译日期：2024-07-29 17:12:39
# 版权所有：www.i-search.com.cn
import ubpa.init_input as iinput
from ubpa.base_util import StdOutHook, ExceptionHandler
import ubpa.itools.rpa_str as rpa_str
import ubpa.ibox as ibox
from PIL import Image
import time
import pdb
from ubpa.ilog import ILog
import getopt
from sys import argv
import sys
import os
from ubpa.base_img import *

class SXCC_Pic_Related_Operations:
     
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
      
    def SXCC_Cut_Pic(self,Str_Input_Pic_Path=None,Int_Input_Left=0,Int_Input_Upper=0,Int_Input_Right=10,Int_Input_Lower=10,Str_Output_Pic_Path=None,Str_Pop_Up_Prompt="是"):
        '''剪切图片\n（SXCC_Cut_Pic）\n1.初始化\n'''
        Str_Process_Name="剪切图片"
        # 序列
        self.__logger.dlogs(job_no=self.job_no, logmsg='Flow:SXCC_Cut_Pic,StepNodeTag:202404191537293972369,Title:序列,Note:')
        #输出
        self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:SXCC_Cut_Pic,StepNodeTag:202404191537293972368,Title:输出,Note:')
        rpa_str.iprints("SXCC_Cut_Pic Start")
        # Try异常
        self.__logger.dlogs(job_no=self.job_no, logmsg='Flow:SXCC_Cut_Pic,StepNodeTag:202404191537294242393,Title:Try异常,Note:')
        try:
            #代码块
            self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:SXCC_Cut_Pic,StepNodeTag:202404191550599792667,Title:代码块,Note:剪切图片')
            # 打开图片文件
            img = Image.open(Str_Input_Pic_Path)
            # 定义剪切区域，通常用左上角坐标和右下角坐标表示
            left, upper = int(Int_Input_Left), int(Int_Input_Upper)   # 原点(0, 0)开始
            right, lower = int(Int_Input_Right), int(Int_Input_Lower)  # 剪切到的位置
            # 使用crop方法剪切图片
            cropped_img = img.crop((left, upper, right, lower))
            # 保存剪切后的图片
            cropped_img.save(Str_Output_Pic_Path)
            #输出
            self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:SXCC_Cut_Pic,StepNodeTag:202404191556237462700,Title:输出,Note:')
            rpa_str.iprints(Str_Process_Name+"成功")
            # IF分支
            self.__logger.dlogs(job_no=self.job_no, logmsg='Flow:SXCC_Cut_Pic,StepNodeTag:202404191556237462696,Title:IF分支,Note:')
            if ("是" in Str_Pop_Up_Prompt) or ("Yes" in Str_Pop_Up_Prompt) or ("Y" in Str_Pop_Up_Prompt) :
                #输出
                self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:SXCC_Cut_Pic,StepNodeTag:202404191556237462701,Title:输出,Note:')
                rpa_str.iprints("需要弹出提示")
                #消息框
                self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:SXCC_Cut_Pic,StepNodeTag:202404191556237462698,Title:消息框,Note:')
                ibox.msgs_box(Str_Process_Name+"成功",title=r"提示",timeout=0)
            else:
                #输出
                self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:SXCC_Cut_Pic,StepNodeTag:202404191556237462697,Title:输出,Note:')
                rpa_str.iprints("不需要弹出提示")
        except Exception as e:
            #输出
            self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:SXCC_Cut_Pic,StepNodeTag:202404191557044532724,Title:输出,Note:')
            rpa_str.iprints(Str_Process_Name+"失败，请检查是否关闭此图片，系统是否异常后，重新运行此组件，谢谢。","异常信息为："+str(e))
            #消息框
            self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:SXCC_Cut_Pic,StepNodeTag:202404191557044532722,Title:消息框,Note:')
            ibox.msgs_box(Str_Process_Name+"失败，请检查是否关闭此图片，系统是否异常后，重新运行此组件，谢谢。","异常信息为："+str(e),title=r"提示",timeout=0)
            #代码块
            self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:SXCC_Cut_Pic,StepNodeTag:202404191557044532725,Title:代码块,Note:停止')
            exit()
        finally:
            pass
        #输出
        self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:SXCC_Cut_Pic,StepNodeTag:202404191537293972367,Title:输出,Note:')
        rpa_str.iprints("SXCC_Cut_Pic End")
      
    def SXCC_Splicing_Pic_Portrait(self,List_Input_Pic_Path=[],Int_Input_Pixel_Spacing=5,Str_Output_Pic_Path=None,Str_Pop_Up_Prompt="是"):
        '''多张图片纵向拼接（有间隔）\n（SXCC_Splicing_Pic_Portrait）\n1.初始化\n'''
        Str_Process_Name="多张图片纵向拼接（有间隔）"
        # 序列
        self.__logger.dlogs(job_no=self.job_no, logmsg='Flow:SXCC_Splicing_Pic_Portrait,StepNodeTag:20240729170743937976,Title:序列,Note:')
        #输出
        self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:SXCC_Splicing_Pic_Portrait,StepNodeTag:20240729170743937973,Title:输出,Note:')
        rpa_str.iprints("SXCC_Splicing_Pic_Portrait Start")
        # Try异常
        self.__logger.dlogs(job_no=self.job_no, logmsg='Flow:SXCC_Splicing_Pic_Portrait,StepNodeTag:20240729170743937974,Title:Try异常,Note:')
        try:
            #代码块
            self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:SXCC_Splicing_Pic_Portrait,StepNodeTag:20240729170743937964,Title:代码块,Note:多张图片纵向拼接（有间隔）')
            # 定义你要合并的图片路径列表
            image_paths = List_Input_Pic_Path
            # 创建一个新的Image实例，用于存放合并后的图像，Int_Input_Pixel_Spacing是指像素
            result_image = Image.new('RGB', (max(Image.open(image).width for image in image_paths), sum(Image.open(image).height for image in image_paths)+len(image_paths)*int(Int_Input_Pixel_Spacing)), color='white')
            # 遍历每个图片，将它们按顺序放置到结果图像上
            y_offset = 0
            for path in image_paths:
                img = Image.open(path)
                result_image.paste(img, (0, y_offset))
                y_offset += img.height+int(Int_Input_Pixel_Spacing)
            # 最后保存合并后的图片
            result_image.save(Str_Output_Pic_Path)
            #输出
            self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:SXCC_Splicing_Pic_Portrait,StepNodeTag:20240729170743937969,Title:输出,Note:')
            rpa_str.iprints(Str_Process_Name+"成功")
            # IF分支
            self.__logger.dlogs(job_no=self.job_no, logmsg='Flow:SXCC_Splicing_Pic_Portrait,StepNodeTag:20240729170743937972,Title:IF分支,Note:')
            if ("是" in Str_Pop_Up_Prompt) or ("Yes" in Str_Pop_Up_Prompt) or ("Y" in Str_Pop_Up_Prompt) :
                #输出
                self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:SXCC_Splicing_Pic_Portrait,StepNodeTag:20240729170743937965,Title:输出,Note:')
                rpa_str.iprints("需要弹出提示")
                #消息框
                self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:SXCC_Splicing_Pic_Portrait,StepNodeTag:20240729170743937971,Title:消息框,Note:')
                ibox.msgs_box(Str_Process_Name+"成功",title=r"提示",timeout=0)
            else:
                #输出
                self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:SXCC_Splicing_Pic_Portrait,StepNodeTag:20240729170743937970,Title:输出,Note:')
                rpa_str.iprints("不需要弹出提示")
        except Exception as e:
            #输出
            self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:SXCC_Splicing_Pic_Portrait,StepNodeTag:20240729170743937966,Title:输出,Note:')
            rpa_str.iprints(Str_Process_Name+"失败，请检查是否关闭这些图片，系统是否异常后，重新运行此组件，谢谢。","异常信息为："+str(e))
            #消息框
            self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:SXCC_Splicing_Pic_Portrait,StepNodeTag:20240729170743937967,Title:消息框,Note:')
            ibox.msgs_box(Str_Process_Name+"失败，请检查是否关闭这些图片，系统是否异常后，重新运行此组件，谢谢。","异常信息为："+str(e),title=r"提示",timeout=0)
            #代码块
            self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:SXCC_Splicing_Pic_Portrait,StepNodeTag:20240729170743937968,Title:代码块,Note:停止')
            exit()
        finally:
            pass
        #输出
        self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:SXCC_Splicing_Pic_Portrait,StepNodeTag:20240729170743937977,Title:输出,Note:')
        rpa_str.iprints("SXCC_Splicing_Pic_Portrait End")
      
    def SXCC_Splicing_Pic_Transverse(self,List_Input_Pic_Path=[],Int_Input_Pixel_Spacing=5,Str_Output_Pic_Path=None,Str_Pop_Up_Prompt="是"):
        '''多张图片横向拼接（有间隔）\n（SXCC_Splicing_Pic_Transverse）\n1.初始化\n'''
        Str_Process_Name="多张图片横向拼接（有间隔）"
        # 序列
        self.__logger.dlogs(job_no=self.job_no, logmsg='Flow:SXCC_Splicing_Pic_Transverse,StepNodeTag:20240729165919352834,Title:序列,Note:')
        #输出
        self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:SXCC_Splicing_Pic_Transverse,StepNodeTag:20240729165919352837,Title:输出,Note:')
        rpa_str.iprints("SXCC_Splicing_Pic_Transverse Start")
        # Try异常
        self.__logger.dlogs(job_no=self.job_no, logmsg='Flow:SXCC_Splicing_Pic_Transverse,StepNodeTag:20240729165919352836,Title:Try异常,Note:')
        try:
            #代码块
            self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:SXCC_Splicing_Pic_Transverse,StepNodeTag:20240729165919352846,Title:代码块,Note:多张图片横向拼接（有间隔）')
            # 定义你要合并的图片路径列表
            image_paths = List_Input_Pic_Path
            # 创建一个新的Image实例，用于存放合并后的图像，Int_Input_Pixel_Spacing是指像素
            result_image = Image.new('RGB', (sum(Image.open(image).width for image in image_paths)+len(image_paths)*int(Int_Input_Pixel_Spacing), max(Image.open(image).height for image in image_paths)), color='white')
            # 遍历每个图片，将它们按顺序放置到结果图像上
            x_offset = 0
            for path in image_paths:
                img = Image.open(path)
                result_image.paste(img, (x_offset, 0))
                x_offset += img.width+int(Int_Input_Pixel_Spacing)
            # 最后保存合并后的图片
            result_image.save(Str_Output_Pic_Path)
            #输出
            self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:SXCC_Splicing_Pic_Transverse,StepNodeTag:20240729165919352841,Title:输出,Note:')
            rpa_str.iprints(Str_Process_Name+"成功")
            # IF分支
            self.__logger.dlogs(job_no=self.job_no, logmsg='Flow:SXCC_Splicing_Pic_Transverse,StepNodeTag:20240729165919352838,Title:IF分支,Note:')
            if ("是" in Str_Pop_Up_Prompt) or ("Yes" in Str_Pop_Up_Prompt) or ("Y" in Str_Pop_Up_Prompt) :
                #输出
                self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:SXCC_Splicing_Pic_Transverse,StepNodeTag:20240729165919352845,Title:输出,Note:')
                rpa_str.iprints("需要弹出提示")
                #消息框
                self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:SXCC_Splicing_Pic_Transverse,StepNodeTag:20240729165919352839,Title:消息框,Note:')
                ibox.msgs_box(Str_Process_Name+"成功",title=r"提示",timeout=0)
            else:
                #输出
                self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:SXCC_Splicing_Pic_Transverse,StepNodeTag:20240729165919352840,Title:输出,Note:')
                rpa_str.iprints("不需要弹出提示")
        except Exception as e:
            #输出
            self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:SXCC_Splicing_Pic_Transverse,StepNodeTag:20240729165919352844,Title:输出,Note:')
            rpa_str.iprints(Str_Process_Name+"失败，请检查是否关闭这些图片，系统是否异常后，重新运行此组件，谢谢。","异常信息为："+str(e))
            #消息框
            self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:SXCC_Splicing_Pic_Transverse,StepNodeTag:20240729165919352843,Title:消息框,Note:')
            ibox.msgs_box(Str_Process_Name+"失败，请检查是否关闭这些图片，系统是否异常后，重新运行此组件，谢谢。","异常信息为："+str(e),title=r"提示",timeout=0)
            #代码块
            self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:SXCC_Splicing_Pic_Transverse,StepNodeTag:20240729165919352842,Title:代码块,Note:停止')
            exit()
        finally:
            pass
        #输出
        self.__logger.dlogs(job_no=self.job_no,logmsg='Flow:SXCC_Splicing_Pic_Transverse,StepNodeTag:20240729165919352833,Title:输出,Note:')
        rpa_str.iprints("SXCC_Splicing_Pic_Transverse End")
      
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
    pro = SXCC_Pic_Related_Operations(robot_no=robot_no,proc_no=proc_no,job_no=job_no,input_arg=input_arg)
    pro.Main()
