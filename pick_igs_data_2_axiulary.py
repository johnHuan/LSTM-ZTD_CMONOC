#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   pick_igs_data_2_axiulary.py
@Contact :   johnhuan@whu.edu.cn
@QQ      :   248404941
@License :   (C)Copyright WHU SGG `ZhangHuan`

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2021/8/6 15:12   张桓        1.0         None
"""
import os
from datetime import datetime


def ymd_to_doy(time):
    """
    年月日到doy的转换
    :param time:   yyyy.mm.dd eg: 2020.01.01, 2020.12.31
    :return: 年积日
    """
    fmt = '%Y.%m.%d'
    dt = datetime.strptime(time, fmt)
    tt = dt.timetuple()
    return tt.tm_year * 1000 + tt.tm_yday


def doy_to_ymd(time):
    """
    年积日到年月日之间的转换
    :param time:年年积日  eg: 2020001， 2020365
    :return: 年/月/日
    """
    dt = datetime.strptime(time, '%Y%j').date()
    fmt = '%Y/%m/%d'
    return dt.strftime(fmt)


if __name__ == '__main__':
    stations = ['bjfs', 'chan', 'urum', 'lhaz']
    base_dir = "E:/lutaiwang/source_data/igs_外符合精度验证/data/IGS/source_data/"
    dest_dir = "E:/lutaiwang/source_data/igs_外符合精度验证/data/IGS/axiulary/"
    for station in stations:
        files = os.listdir(base_dir + station)
        dest_file = open(dest_dir + station + '.csv', 'a')
        for file in files:
            try:
                content = open(base_dir + station + '/' + file, 'r')
                for empty_line in range(0, 61):
                    s = content.readline()
                line = content.readline()
                while line.startswith(' '):
                    year = '20' + line[6:8]
                    doy = line[9:12]
                    second = int(line[13:18])
                    m, s = divmod(second, 60)
                    h, m = divmod(m, 60)
                    epoch_date = doy_to_ymd(year + doy)
                    ymd_hms = "{0} {1:02d}:{2:02d}:{3:02d}".format(epoch_date, h, m, s)
                    min_sec = "{0:02d}_{1:02d}".format(m, s)
                    zpd = line[19:25]
                    doy_decimal = float(int(doy) + second / 60 / 60 / 24)
                    # arr = [ymd_hms, doy, str(second), str(doy_decimal), zpd]
                    arr = [ymd_hms, min_sec, str(float(zpd) / 1000)]
                    dest_file.write(','.join(arr) + '\n')
                    dest_file.flush()
                    line = content.readline()
            except Exception as ex:
                print("异常" + ex)
        dest_file.close()
