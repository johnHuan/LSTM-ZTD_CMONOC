# -*- coding: utf-8 -*-
# @Time    : 2021/8/5 17:23:35
# @Author  : Zhang Huan
# @Email   : johnhuan@whu.edu.cn
# QQ       : 248404941
# @File    : knn_ztd.py
import os

import pandas as pd

if __name__ == '__main__':

    base_dir = 'H:/lutaiwang/source_data/gpt2/missing_rate/10/well/data/'
    target_dir = 'H:/lutaiwang/source_data/residuals/'
    stations = os.listdir(base_dir)
    for station in stations:
        dataframe = pd.read_csv(base_dir + station)
        dataframe['r_k_p'] = dataframe['knn'] - dataframe['period_model']
        dataframe.to_csv(target_dir + station)
