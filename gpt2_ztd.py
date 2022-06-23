# -*- coding: utf-8 -*-
# @Time    : 2021/7/24 17:22
# @Author  : Zhang Huan
# @Email   : johnhuan@whu.edu.cn
# QQ       : 248404941
# @File    : gpt2_ztd.py
import os

import matplotlib
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

matplotlib.use('Agg')

if __name__ == '__main__':
    base_dir = 'H:/lutaiwang/source_data/knn_ztd/'
    target_dir = 'H:/lutaiwang/source_data/gpt2/'
    stations = os.listdir(base_dir)
    for station in stations:
        c_unit, c0, c1, c2, c3, c4, = [], [], [], [], [], []
        path = base_dir + station
        dataframe = pd.read_csv(path, usecols=['doy_hours', 'doy_t', 'ymfh', 'ztd', 'knn'])
        for e in dataframe['ymfh']:
            year = e[0:4]
            doy = e[5:8]
            hour = e[9:11]
            epoch = float(year) + float(doy) / 366.25 + float(hour) / 24 / 366.25
            c_unit.append(1)
            c0.append(epoch)
            c1.append(np.cos(2 * np.pi * epoch))
            c2.append(np.sin(2 * np.pi * epoch))
            c3.append(np.cos(4 * np.pi * epoch))
            c4.append(np.sin(4 * np.pi * epoch))
        C = np.transpose(np.array([c_unit, c0, c1, c2, c3, c4]))
        CT = np.transpose(C)
        CTC = np.dot(CT, C)
        CTC_n = np.linalg.inv(CTC)
        CTC_n_CT = np.dot(CTC_n, CT)
        A = np.dot(CTC_n_CT, dataframe['knn'])
        period_model = np.dot(A, CT)
        dataframe['period_model'] = period_model
        dataframe['year_doy'] = c0
        dataframe['residual'] = dataframe['ztd'] - dataframe['period_model']
        dataframe.to_csv(target_dir + 'data/' + station)
        plt.plot(dataframe['year_doy'], dataframe['knn'], 'g.', label="knn")
        plt.plot(dataframe['year_doy'], dataframe['ztd'], 'b*-', label="ztd")
        plt.plot(dataframe['year_doy'], dataframe['period_model'], 'm-', label="period", linewidth=2)
        plt.title('ztd data at Seasonal model without correct residual' + str(station))
        plt.xlabel('time serial(year)')
        plt.ylabel('ztd(m)')
        plt.legend()  # 给图加图例
        plt.savefig(target_dir + 'fig/period_model/' + station + ".png")
        plt.close()
        plt.plot(dataframe['year_doy'], dataframe['residual'], color='#ed7d31',
                 label="ztd residual at Seasonal model ", linewidth=2)
        plt.title('ztd residual at Seasonal model ' + station)
        plt.xlabel('time serial(year)')
        plt.ylabel('residual(cm)')
        plt.legend()  # 给图加图例
        plt.savefig(target_dir + 'fig/residual_serial/' + station + ".png")
        plt.close()
