# -*- coding: utf-8 -*-
# author: cy
# date: 2021/11/17
# aim: 提供给C端数值处理
import pandas as pd
import sys


def test_check_format(time_str="", time_format=""):
    df = pd.DataFrame({"test": [time_str]})
    try:
        df["test"] = pd.to_datetime(df["test"], format=time_format)
        print("true")
        return True
    except Exception as e:
        print(e)
        return False


if __name__ == '__main__':
    test_check_format(time_str=sys.argv[1], time_format=sys.argv[2])
