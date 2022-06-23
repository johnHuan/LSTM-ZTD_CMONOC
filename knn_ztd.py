# -*- coding: utf-8 -*-
# @Time    : 2021/7/24 15:33
# @Author  : Zhang Huan
# @Email   : johnhuan@whu.edu.cn
# QQ       : 248404941
# @File    : knn_ztd.py
import os

import pandas as pd
from sklearn import neighbors

if __name__ == '__main__':

    base_dir = 'H:/lutaiwang/source_data/make_interpolate_data_gap/'
    target_dir = 'H:/lutaiwang/source_data/knn_ztd/'
    stations = os.listdir(base_dir)
    for station in stations:
        dataframe_xy = pd.read_csv(base_dir + station)
        dataframe_T = dataframe_xy
        dataframe_continued = dataframe_xy.dropna(axis=0, how='any')
        X = dataframe_continued['ymfh'].values.reshape(dataframe_continued.shape[0], 1)
        y = dataframe_continued['ztd'].values
        T = dataframe_T['ymfh'].values.reshape(dataframe_T.shape[0], 1)
        n_neighbors = 24 * 30
        knn = neighbors.KNeighborsRegressor(n_neighbors, weights='distance')
        y_ = knn.fit(X, y).predict(T)
        df_ty = pd.DataFrame({'T': T.reshape(1, -1)[0], 'y': y_})
        dataframe_T['knn'] = df_ty['y']
        dataframe_T.to_csv(target_dir + station)
        # plt.scatter(dataframe_T.iloc[:, 0], dataframe_T['ztd'], c='purple',
        #             s=20,  # 设置半径
        #             linewidths=1,  # 设置边框的线宽
        #             label='original')
        # plt.plot(dataframe_T.iloc[:, 0], dataframe_T['knn'], c='g', label='knn')
        # plt.axis('tight')
        # plt.legend()
        # plt.title("KNeighborsRegressor")
        # plt.show()
