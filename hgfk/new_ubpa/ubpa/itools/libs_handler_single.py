# -*- coding:utf-8 -*- 
# Created on 2020/4/9
# author: Tao.JunXin
import sys

from _libs_handler_single import get_file_dic_revision

if __name__ == '__main__':
    # filename = r'D:\robotTool2\studio-v6\project\baidu_01'
    # filename = r'D:\robotTool2\studio-v6\project\NewProject1'
    # filename = r'D:\robotTool2\studio-v6\project\NewProject2'
    # filename = r'D:\robotTool2\studio-v6\project\NewProject3'
    # filename = r'D:\robotTool2\studio-v6\project\NewProject4'
    # filename = r'D:\robotTool2\studio-v6\project\NewProject26'
    # rfw_addr = r'C:\Users\tanbinbin\Desktop\Project7.rfw'
    filename = sys.argv[1]
    rfw_addr = sys.argv[2]
    get_file_dic_revision(filename, rfw_addr)
