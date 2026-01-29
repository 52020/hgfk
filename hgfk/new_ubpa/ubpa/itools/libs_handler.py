# -*- coding:utf-8 -*- 
# Created on 2020/4/9
# author: Tao.JunXin
import sys

from _libs_handler import get_file_dic

if __name__ == '__main__':
    # filename = r'D:\robotTool2\studio-v6\project'
    # rfw_addr = r'C:\Users\tanbinbin\Desktop\Project6.rfw'
    filename = sys.argv[1]
    rfw_addr = sys.argv[2]
    get_file_dic(filename, rfw_addr)
