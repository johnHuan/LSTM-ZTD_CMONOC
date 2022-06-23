# -*- coding: utf-8 -*-
# @Time    : 2021/7/19 17:54
# @Author  : Zhang Huan
# @Email   : johnhuan@whu.edu.cn
# QQ       : 248404941
# @File    : tell_2013_2018.py

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os

if __name__ == '__main__':
    source_data_dir = "H:/lutaiwang/source_data/stations_data/"
    target_data_dir = "H:/lutaiwang/source_data/ztd_13_18/"
    stations = os.listdir(source_data_dir)
    for station in stations:
        station_path = source_data_dir + station
        target_path = target_data_dir + station
        df = pd.read_csv(station_path, names=["year", "doy", "hod", "ztd"])
        filtered_data = df.loc[df['year'] >= 2013, ["year", "doy", "hod", "ztd"]]
        filtered_data.to_csv(target_path, index=None)

