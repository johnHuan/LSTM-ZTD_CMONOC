# -*- coding: utf-8 -*-
# @Time    : 2021/9/21 16:00
# @Author  : Zhang Huan
# @Email   : johnhuan@whu.edu.cn
# QQ       : 248404941
# @File    : interpolate.py

import numpy as np
from scipy.interpolate import griddata


def func(x, y, z):
    return x * (1 - x) * np.cos(4 * np.pi * x) * (np.sin(4 * np.pi * y ** 2) ** 2) * z


if __name__ == '__main__':

    points = np.random.rand(10, 3)  # 实际点坐标
    values = func(points[:, 0], points[:, 1], points[:, 2])  # 实际点的值



    point_grid = np.array([[0.0, 0.0, 0.0], [0.4, 0.4, 0.4], [0.8, 0.8, 0.8], [1.0, 1.0, 1.0]])  # 网格点坐标
    # nearest, linear, cubic
    grid_z0 = griddata(points, values, point_grid, method='nearest')  # 插值计算，计算出网格点的值
    print(grid_z0)

