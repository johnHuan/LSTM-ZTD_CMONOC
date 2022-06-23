#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   knn_ztd_精度验证.py    
@Contact :   johnhuan@whu.edu.cn
@QQ      :   248404941
@License :   (C)Copyright WHU SGG `ZhangHuan`

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2021/8/4 21:52   张桓        1.0         None
"""
import os

import pandas as pd
from sklearn import neighbors

if __name__ == '__main__':
    base_dir = 'H:/lutaiwang/source_data/knn_验证精度/AHBB.csv'
    target_dir = 'H:/lutaiwang/source_data/knn_验证精度/_AHBB.csv'
    dataframe_xy = pd.read_csv(base_dir)
    dataframe_T = dataframe_xy
    dataframe_continued = dataframe_xy.dropna(axis=0, how='any')
    X = dataframe_continued['ymfh'].values.reshape(dataframe_continued.shape[0], 1)
    y = dataframe_continued['ztd'].values
    T = dataframe_T['ymfh'].values.reshape(dataframe_T.shape[0], 1)
    n_neighbors = 24 * 20
    knn = neighbors.KNeighborsRegressor(n_neighbors, weights='distance')
    y_ = knn.fit(X, y).predict(T)
    df_ty = pd.DataFrame({'T': T.reshape(1, -1)[0], 'y': y_})
    dataframe_T['knn'] = df_ty['y']
    dataframe_T.to_csv(target_dir)
