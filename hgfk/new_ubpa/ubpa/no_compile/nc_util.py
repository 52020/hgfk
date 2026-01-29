import time


# TODO: no-compile
# TODO: "%d"在编译时报错不支持
def get_current_datetime():
    """
    获得当前日期时间（保留3位微秒）
    :return:
    """
    ct = time.time()
    local_time = time.localtime(ct)
    data_head = time.strftime("%Y-%m-%d %H:%M:%S", local_time)
    data_secs = (ct - int(ct)) * 1000
    time_stamp = "%s,%03d" % (data_head, data_secs)
    return time_stamp


def get_rpa_time():
    """
    获得当前日期时间（保留3位微秒）  可用于文件命名
    :return:  20201030135958969
    """
    ct = time.time()
    local_time = time.localtime(ct)
    data_head = time.strftime("%Y%m%d%H%M%S", local_time)
    data_secs = (ct - int(ct)) * 1000
    time_stamp = "%s%03d" % (data_head, data_secs)
    return time_stamp
