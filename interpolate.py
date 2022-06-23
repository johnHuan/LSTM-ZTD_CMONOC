# -*- coding: utf-8 -*-
# @Time    : 2021/9/21 16:00
# @Author  : Zhang Huan
# @Email   : johnhuan@whu.edu.cn
# QQ       : 248404941
# @File    : interpolate.py

import numpy as np
import pandas as pd
from scipy.interpolate import griddata

if __name__ == '__main__':
    grid_name = 'china1_1'
    method = 'nearest'
    source_blh_rms_path = 'H:/lutaiwang/source_data/lstm/预报精度统计.csv'
    source_grid____path = 'H:/lutaiwang/grid/' + grid_name + '.grd'
    target_grid____path = "H:/lutaiwang/" + grid_name + '_' + method + ".csv"
    dataframe = pd.read_csv(source_blh_rms_path, usecols=['station', 'l', 'b', 'h', 'rms'])
    rms = dataframe['rms'].values  # 实际的RMS值
    # stations = dataframe[['l', 'b', 'h']].values  # 实际点坐标
    stations = dataframe[['l', 'b']].values  # 实际点坐标

    # point_grid = np.array([[0.0, 0.0, 0.0], [0.4, 0.4, 0.4], [0.8, 0.8, 0.8], [1.0, 1.0, 1.0]])  # 需要被插值出来的网格点坐标
    grid = pd.read_csv(source_grid____path, sep=' ')
    # grid = pd.read_csv(source_grid____path, usecols=['ld', 'bd', 'b', 'l', 'h'])
    l = grid.iloc[:, 0] / 60
    b = grid.iloc[:, 1] / 60
    h = grid.iloc[:, 2]
    # grid_lbh = pd.DataFrame({'l': l, 'b': b, 'h': h})
    grid_lbh = pd.DataFrame({'l': l, 'b': b})

    g_v = grid_lbh.values
    # point_grid = grid[['ld', 'bd', 'b']].values

    # nearest, linear, cubic
    # grid_rms = griddata(stations, rms, g_v, method='nearest')  # 插值计算，计算出网格点的RMS值
    """
        method: nearest, linear, cubic
        rescale ： bool，可选。在执行插值之前，重新缩放指向单位立方体。如果某些输入维度具有不可比较的单位并且相差很多个数量级，则这非常有用。
        fill_value ： float，可选。用于填充输入点凸包外部的请求点的值。如果未提供，则默认为nan。此选项对“最近”方法无效。
    """
    # grid_rms = griddata(stations, rms, g_v, method='linear', rescale=False, fill_value=0.9)  # 插值计算，计算出网格点的RMS值
    grid_rms = griddata(stations, rms, g_v, method=method)  # 插值计算，计算出网格点的RMS值
    grid_lbh['rms'] = grid_rms
    grid_lbh.to_csv(target_grid____path)
