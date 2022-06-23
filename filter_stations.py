# -*- coding: utf-8 -*-
# @Time    : 2021/7/25 10:14
# @Author  : Zhang Huan
# @Email   : johnhuan@whu.edu.cn
# QQ       : 248404941
# @File    : filter_stations.py
import os
import matplotlib
from matplotlib import pyplot as plt

import pandas as pd

matplotlib.use('Agg')

'''
将大于rate的数据存储到对应的rate目录下，
把data保存在rate目录下的data目录下，把周期图画到fig下，
不满足要求的放到bad下
rate:
    well
        fig
        data
    bad
        fig
        data
'''


def switch2dir(rate, how, dataframe, station, target_dir):
    plt.plot(dataframe['year_doy'], dataframe['knn'], 'g.', label="knn")
    plt.plot(dataframe['year_doy'], dataframe['ztd'], 'b*-', label="ztd")
    plt.plot(dataframe['year_doy'], dataframe['period_model'], 'm-', label="period", linewidth=2)
    plt.title('ztd data at Seasonal model without correct residual' + str(station))
    plt.xlabel('time serial(year)')
    plt.ylabel('ztd(m)')
    plt.legend()
    plt.savefig(target_dir + str(rate) + '/' + how + '/fig/' + station + ".png")
    plt.close()
    dataframe.to_csv(target_dir + str(rate) + '/' + how + '/data/' + station)



if __name__ == '__main__':
    base_dir = 'E:/lutaiwang/source_data/gpt2/data/'
    target_dir = 'E:/lutaiwang/source_data/gpt2/missing_rate/'
    stations = os.listdir(base_dir)
    for station in stations:
        station_path = base_dir + station
        dataframe = pd.read_csv(station_path)
        count_missing = dataframe['ztd'].isna().sum()
        count_all = dataframe.shape[0]
        missing_rate = count_missing / count_all
        if missing_rate > 0.10:  # 大于10%
            switch2dir(10, 'bad', dataframe, station, target_dir)
        else:
            switch2dir(10, 'well', dataframe, station, target_dir)
        if missing_rate > 0.15:
            switch2dir(15, 'bad', dataframe, station, target_dir)
        else:
            switch2dir(15, 'well', dataframe, station, target_dir)
        if missing_rate > 0.20:
            switch2dir(20, 'bad', dataframe, station, target_dir)
        else:
            switch2dir(20, 'well', dataframe, station, target_dir)
        if missing_rate > 0.25:
            switch2dir(25, 'bad', dataframe, station, target_dir)
        else:
            switch2dir(25, 'well', dataframe, station, target_dir)
        if missing_rate > 0.30:
            switch2dir(30, 'bad', dataframe, station, target_dir)
        else:
            switch2dir(30, 'well', dataframe, station, target_dir)
