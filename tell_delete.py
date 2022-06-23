#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   tell_delete.py    
@Contact :   johnhuan@whu.edu.cn
@QQ      :   248404941
@License :   (C)Copyright WHU SGG `ZhangHuan`

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2021/7/26 11:28   张桓        1.0         None
"""
import os
import pandas as pd

if __name__ == '__main__':
    missing_data_base_dir = "E:/lutaiwang/source_data/gpt2/missing_rate/10/bad/data/"
    original_data_path = "E:/lutaiwang/source_data/gpt2/原始数据.csv"
    target_dir = "E:/lutaiwang/source_data/gpt2/"
    stations = os.listdir(missing_data_base_dir)
    dataframe = pd.read_csv(original_data_path, header=None)
    deleted = pd.DataFrame(columns=[0, 1, 2, 3])
    for station in stations:
        s = station[:-4]
        dt = dataframe[dataframe[0] == s]
        deleted = deleted.append(dt, ignore_index=True)
    deleted.to_csv(target_dir + 'deleted.csv')
    kept = pd.concat([dataframe, deleted]).drop_duplicates(keep=False)
    kept.to_csv(target_dir + 'kept.csv')
