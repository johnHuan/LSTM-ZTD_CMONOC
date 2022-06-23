#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   resample_igs_data.py    
@Contact :   johnhuan@whu.edu.cn
@QQ      :   248404941
@License :   (C)Copyright WHU SGG `ZhangHuan`

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2021/8/6 15:55   张桓        1.0         None
"""
import os
import pandas as pd

if __name__ == '__main__':
    base_dir = "E:/lutaiwang/source_data/igs_外符合精度验证/data/IGS/axiulary/"
    dest_dir = "E:/lutaiwang/source_data/igs_外符合精度验证/data/IGS/ztd/"
    stations = os.listdir(base_dir)
    for station in stations:
        dataframe = pd.read_csv(base_dir + station, header=None)
        # df_mots[(df_mots['time'] < 25320) & (df_mots['time'] >= 25270)]
        df = dataframe[(dataframe[1] == '00_00')]
        df.to_csv(dest_dir + station)
