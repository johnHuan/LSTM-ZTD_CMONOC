# -*- coding: utf-8 -*-
# @Time    : 2021/8/19 11:17
# @Author  : Zhang Huan
# @Email   : johnhuan@whu.edu.cn
# QQ       : 248404941
# @File    : add2get_lstm_product.py
import os

import pandas as pd

if __name__ == '__main__':
    gpt2_dir = "H:/lutaiwang/source_data/residuals/"
    lstm_pred_dir = "H:/lutaiwang/source_data/lstm/result_data/"
    target_dir = "H:/lutaiwang/source_data/lstm/product/"
    stations = os.listdir(gpt2_dir)
    for station in stations:
        source_path = gpt2_dir + station
        predict_path = lstm_pred_dir + station
        target_path = target_dir + station
        source_dataframe = pd.read_csv(source_path,
                                       usecols=['ymfh', 'doy_t', 'doy_hours', 'ztd', 'knn', 'period_model', 'year_doy',
                                                'residual', 'r_k_p'])
        predict_dataframe = pd.read_csv(predict_path, usecols=['predict', 'test'])
        target_dataframe = source_dataframe[source_dataframe.shape[0] - predict_dataframe.shape[0]:]
        target_dataframe = target_dataframe.reset_index(drop=True)
        target_dataframe['lstm_test'] = predict_dataframe['test']
        target_dataframe['lstm_predict'] = predict_dataframe['predict'] + target_dataframe['period_model']
        target_dataframe.to_csv(target_path)
