# -*- coding: utf-8 -*-
# author: cy
# date: 2021/12/13
# aim: 提供给C端转换数字
import sys


def convert_type(text="", cell_format=""):
    try:
        if cell_format == "float":
            text = float(text)
        else:
            text = int(text.split(".")[0])
        print(str(text))
        return str(text)
    except Exception as e:
        print("error")
        return ("error")
        
if __name__ == '__main__':
    convert_type(text=sys.argv[1], cell_format=sys.argv[2])
