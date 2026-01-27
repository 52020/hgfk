# coding=utf-8
# 编译日期：2023-08-21 15:58:58
# 版权所有：www.i-search.com.cn
import ubpa.idatabase as idatabase
import ubpa.init_input as iinput
import time
import pdb
from ubpa.ilog import ILog
import getopt
from sys import argv
import sys
import os
from ubpa.base_img import *

class MysqlInsert:
     
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
        if('input_arg' in kwargs.keys()):
            self.input_arg = kwargs['input_arg']
            if(len(self.input_arg) <= 0):
                self.input_arg = iinput.load_init(__file__)
            if self.input_arg is None:
                sys.exit(0)
    def Main(self):
        
        
        #创建数据库对象
        mysqlObj=idatabase.connect_database(database_type='Mysql',host='10.57.5.145',user='statisticsUser',password='FNYMjA4MTEqIwIypQaWNjUlBBQ==',database_name='process_time',port=3306,charset='utf8mb4')
        #状态为0时开始，为1时为结束,其他抛出异常
        if statusFlg==0:
            sqlTxt=f'''
                insert 
                into process_action_times(name, year, month, start_time, update_time,department_name) 
                values ( 
                  '{processName}'
                  , date_format(NOW(), '%Y')
                  , date_format(NOW(), '%m')
                  , NOW()
                  , NOW()
                  ,'{departmentName}'
                );
            '''
            startPro=idatabase.execute_database(db=mysqlObj,sql_execute=sqlTxt)
            sqlTxt2='''
                SELECT LAST_INSERT_ID();
            '''
            #获取插入号
            startProIdDf=idatabase.query_database(db=mysqlObj,sql_query=sqlTxt2)
            #获取id
            dataDcit['proId']=str(startProIdDf['LAST_INSERT_ID()'][0])
            dataDcit['执行结果']='成功'
        elif statusFlg==1:
            #获取id
            proId=shoudDict['proId']
            sqlTxt=f'''
            UPDATE process_action_times p1 
              INNER JOIN ( 
                select
                  start_time 
                from
                  process_action_times p2 
                WHERE
                  p2.id = {proId}
              ) p3 
            SET
              p1.end_time = NOW()
              , p1.update_time = NOW()
              , p1.action_success = 1
              , p1.action_time = TIMESTAMPDIFF(SECOND, p3.start_time, NOW()) 
              , p1.runcount='{runCount}'
            WHERE
              p1.id = {proId}
            '''
            startPro=idatabase.execute_database(db=mysqlObj,sql_execute=sqlTxt)
            dataDcit['执行结果']='成功'
        else:
            dataDcit['执行结果']='状态异常'
        idatabase.close_database(db=mysqlObj)
        return dataDcit
 
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
    pro = MysqlInsert(robot_no=robot_no,proc_no=proc_no,job_no=job_no,input_arg=input_arg)
    pro.Main()
