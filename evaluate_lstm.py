# -*- coding: utf-8 -*-
# @Time    : 2021/8/19 11:41
# @Author  : Zhang Huan
# @Email   : johnhuan@whu.edu.cn
# QQ       : 248404941
# @File    : evaluate_lstm.py
import os
import numpy as np
import pandas as pd
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error


def assess(path):
    dataframe = pd.read_csv(path, usecols=['ymfh', 'knn', 'lstm_predict'])
    y1, y2 = dataframe['knn'], dataframe['lstm_predict']
    mae = mean_absolute_error(y1, y2)
    rmse = np.sqrt(mean_squared_error(y1, y2))
    bias = np.average(y1 - y2)
    std = np.sqrt(np.average((y1 - y2 - bias) ** 2))
    print(str.format("std:{}, bias:{}, mae: {}, rmse: {}", std, bias, mae, rmse))
    return bias, mae, std, rmse


if __name__ == '__main__':
    base_dir = "H:/lutaiwang/source_data/lstm/product/"
    dest_dir = "H:/lutaiwang/source_data/lstm/预报精度统计.csv"
    stations = os.listdir(base_dir)
    biases, maes, stds, rmses = [], [], [], []
    j = 0
    for station in stations:
        bias, mae, std, rmse = assess(base_dir + station)
        biases.append(bias*100)
        maes.append(mae*100)
        stds.append(std*100)
        rmses.append(rmse*100)
        j += 1
        print(j)
    data = pd.DataFrame({
        'station': stations,
        'bias': biases,
        'mae': maes,
        'std': stds,
        'rms': rmses
    })
    data.to_csv(dest_dir)
