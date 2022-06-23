# -*- coding: utf-8 -*-
# @Time    : 2021/12/8 15:34
# @Author  : Zhang Huan
# @Email   : johnhuan@whu.edu.cn
# QQ       : 248404941
# @File    : decode.py
import numpy as np
import pandas as pd
import statsmodels.api as sm
from matplotlib import pyplot as plt
import scipy.stats as stats

if __name__ == '__main__':
    # base_dir = 'F:/ImplDoctor/marchineLearning/lutaiwang/source_data/knn_ztd/'
    # station = 'BJSH.csv'
    # base_dir = 'F:/global_temperature/data/'
    base_dir = 'F:/ImplDoctor/marchineLearning/lutaiwang/source_data/lstm/result_data/'
    # station = '89_116.5.csv'
    # station = '39.75_116.5.csv'
    station = 'BJGB.csv'
    # df = pd.read_csv(base_dir + station, usecols=['doy_hours', 'doy_t', 'ymfh', 'ztd', 'knn'])
    df = pd.read_csv(base_dir + station, usecols=['predict', 'test'])
    # df = df[0:8762]
    df = df.dropna()
    cov = stats.pearsonr(df['predict'].values, df['test'].values)
    # cov = np.cov(df.values, rowvar=True)
    # div = np.sqrt(np.var(df['t2m_c'].values) * np.var(df['surface_pressure'].values))
    print(cov)
    print(np.cov(df, rowvar=False))
    # res = sm.tsa.seasonal_decompose(df['knn'].values, freq=8764)
    res = sm.tsa.seasonal_decompose(df['t2m_c'].values, period=8762)
    res.plot()
    plt.show()
