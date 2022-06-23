# -*- coding: utf-8 -*-
# @Time    : 2021/9/21 16:00
# @Author  : Zhang Huan
# @Email   : johnhuan@whu.edu.cn
# QQ       : 248404941
# @File    : interpolate.py

import numpy as np
import pandas as pd
from scipy.interpolate import griddata, LinearNDInterpolator
from scipy import interpolate

if __name__ == '__main__':
    grid_name = 'china5_5'
    source_blh_rms_path = 'H:/lutaiwang/source_data/lstm/预报精度统计.csv'
    source_grid____path = 'H:/lutaiwang/grid/' + grid_name + '.grd'
    target_grid____path = "H:/lutaiwang/linear_" + grid_name + ".csv"
    dataframe = pd.read_csv(source_blh_rms_path, usecols=['station', 'l', 'b', 'h', 'rms'])
    l_station = dataframe['l'].values  # 实际的经度
    b_station = dataframe['b'].values  # 实际的纬度
    h_station = dataframe['h'].values  # 实际的纬度
    rms_station = dataframe['rms'].values  # 实际的RMS值
    # kind : {'linear', 'cubic', 'quintic'}, optional
    LinearNDInterpolator((l_station, b_station, h_station), rms_station)
    newfunc = interpolate.interp2d(l_station, b_station, rms_station, kind='quintic')
    grid = pd.read_csv(source_grid____path, sep=' ')
    l_grid = grid.iloc[:, 0] / 60
    b_grid = grid.iloc[:, 1] / 60
    h_grid = grid.iloc[:, 2]
    grid_lbh = pd.DataFrame({'l': l_grid, 'b': b_grid, 'h': h_grid})
    rms_grid = newfunc(l_grid, b_grid)
    grid_lbh['rms'] = rms_grid
    grid_lbh.to_csv(target_grid____path)



