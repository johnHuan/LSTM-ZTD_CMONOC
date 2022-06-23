#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   evaluate_gpt.py    
@Contact :   johnhuan@whu.edu.cn
@QQ      :   248404941
@License :   (C)Copyright WHU SGG `ZhangHuan`

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2021/8/6 21:30   张桓        1.0         None
"""
import os
import numpy as np
import pandas as pd
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error


def assess(path):
    dataframe = pd.read_csv(path, usecols=['ymfh', 'knn', 'period_model'])
    y1, y2 = dataframe['knn'], dataframe['period_model']
    mae = mean_absolute_error(y1, y2)
    rmse = np.sqrt(mean_squared_error(y1, y2))
    bias = np.average(y1 - y2)
    std = np.sqrt(np.average((y1 - y2 - bias) ** 2))
    print(str.format("std:{}, bias:{}, mae: {}, rmse: {}", std, bias, mae, rmse))
    return bias, mae, std, rmse


if __name__ == '__main__':
    base_dir = "G:/资料/ImplDoctor/marchineLearning/lutaiwang/source_data/residuals/"
    dest_dir = "G:/资料/ImplDoctor/marchineLearning/lutaiwang/source_data/gpt2/内符合精度.csv"
    stations = os.listdir(base_dir)
    data_set = []
    j = 0
    for station in stations:
        bias, mae, std, rmse = assess(base_dir + station)
        data_set.append([station[:-4], bias, mae, std, rmse])
        j += 1
        print(j)
    data = pd.DataFrame(data_set)
    data.to_csv(dest_dir)
