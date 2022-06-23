# -*- coding: utf-8 -*-
# @Time    : 2021/7/20 10:38
# @Author  : Zhang Huan
# @Email   : johnhuan@whu.edu.cn
# QQ       : 248404941
# @File    : all_date.py
import os

import pandas as pd

import time_utils


def getYMDH(di):
    epochs, doy_hours, doy_ts = [], [], []
    for index, row in di.iterrows():
        time_str = str(row[0])
        year = int(time_str[0:4])
        month = int(time_str[5:7])
        day = int(time_str[8:10])
        hour = time_str[11:13]
        doy = time_utils.get_day_of_year(year, month, day)
        doy_t = doy + int(hour) / 24
        doy_hour = str(doy) + '.' + hour
        epoch = str(year) + '_' + str(doy).zfill(3) + '_' + str(hour).zfill(2)
        doy_ts.append(doy_t)
        doy_hours.append(doy_hour)
        epochs.append(epoch)
    return pd.DataFrame({'epoch': epochs, 'doy_hours': doy_hours, 'doy_t': doy_ts})


def get_epochs(dataframe):
    epochs, ztds, = [], []
    for index, row in dataframe.iterrows():
        year = int(row['year'])
        doy = int(row['doy'])
        hod = int(row['hod'])
        ztd = row['ztd']
        epoch = str(year) + '_' + str(doy).zfill(3) + '_' + str(hod).zfill(2)
        epochs.append(epoch)
        ztds.append(ztd)
    return pd.DataFrame({'epoch': epochs, 'ztd': ztds})


if __name__ == '__main__':
    source_dir = 'H:/lutaiwang/source_data/ztd_13_18/'
    dest_dir = "H:/lutaiwang/source_data/make_interpolate_data_gap/"
    date_index = pd.date_range(start="20130101", end="20180301", freq="1h")
    di = pd.DataFrame(date_index)
    stations = os.listdir(source_dir)
    for station in stations:
        df_time_total = getYMDH(di)
        station_path = source_dir + station
        dataframe = pd.read_csv(station_path)
        df_ztd = get_epochs(dataframe)
        df_ztd = df_ztd.set_index('epoch')
        df_time_total = df_time_total.set_index('epoch')
        df_ztd.insert(1, 'ymfh', pd.Series(df_ztd.index).values)
        df_time_total.insert(2, 'ymfh', pd.Series(df_time_total.index).values)
        res = pd.merge(df_time_total, df_ztd, how="left")
        print(date_index)
        res.to_csv(dest_dir + station)
