import datetime
import os

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import load_model

matplotlib.use('Agg')


# 定义显示函数
def plot_predictions(output_path, station, predict_ztd, test_set):
    """
    test_result: 测试真实值
    predict_result: 预测值
    """
    # 预测值剔除系统差
    predict_ztd_no_system_bias = []
    arr_test_mean = np.mean(test_set)
    arr_predict_mean = np.mean(predict_ztd)
    system_error = arr_test_mean - arr_predict_mean
    for i in predict_ztd:
        predict_ztd_no_system_bias.append(i[0] + system_error)
    plt.plot(test_set, color='orange', label='original ZPD')
    plt.plot(predict_ztd_no_system_bias, color='green', label='LSTM')
    plt.title('LSTM model trained ZPD data at ' + station)
    plt.xlabel('doy')
    plt.ylabel('ZPD')
    plt.legend()  # 给图加图例
    img = output_path + 'fig/' + station + '_' + str(system_error) + ".png"
    plt.savefig(img)
    plt.close()


def save_data(output_path, station, predict_ztd, test_set):
    predict_ztd_no_system_bias = []
    arr_test_mean = np.mean(test_set)
    arr_predict_mean = np.mean(predict_ztd)
    system_error = arr_test_mean - arr_predict_mean
    for i in predict_ztd:
        predict_ztd_no_system_bias.append(i[0] + system_error)
    test_set = np.array(test_set).reshape(1, -1)[0]
    dataframe = pd.DataFrame({"predict": predict_ztd_no_system_bias, "test": test_set})
    dest_path = output_path + 'result_data/' + station
    print("save to :" + dest_path)
    dataframe.to_csv(dest_path)


def predict(source_path, source_filename, output_path, num):
    filename = source_path + source_filename
    dataset = pd.read_csv(filename, usecols=['year_doy', 'r_k_p'])
    total = dataset.shape[0]
    flag_index = total - num
    train_set = dataset[0:flag_index].iloc[:, 1:2].values
    test_set = dataset[flag_index:].iloc[:, 1:2].values
    sc = MinMaxScaler(feature_range=[0, 1])
    sc.fit_transform(train_set)
    model_path = output_path + 'WUHN.csv_ztd.h5'
    model = load_model(model_path)
    print(model.summary())
    dataset_total = dataset['r_k_p'][:]
    step = each_day_num * 30
    epoch = step
    inputs = dataset_total[len(dataset_total) - len(test_set) - epoch:].values
    inputs = inputs.reshape(-1, 1)
    inputs = sc.transform(inputs)
    x_test = []
    for i in range(epoch, inputs.shape[0]):
        x_test.append(inputs[i - epoch:i, 0])
    x_test = np.array(x_test)
    x_test = np.reshape(x_test, (x_test.shape[0], x_test.shape[1], 1))
    predict_test = model.predict(x_test)
    predict_ztd = sc.inverse_transform(predict_test)
    plot_predictions(output_path, station, predict_ztd, test_set)
    save_data(output_path, station, predict_ztd, test_set)


if __name__ == '__main__':
    data_path = "H:/lutaiwang/source_data/residuals/"
    output_path = "H:/lutaiwang/source_data/lstm/"
    station = "WUHN.csv"
    stations = os.listdir(data_path)
    stations.sort()
    for station in stations:
        predict_days = 60
        each_day_num = 24
        predict_num = predict_days * each_day_num
        start_lstm_inner = datetime.datetime.now()
        predict(data_path, station, output_path, predict_num)
        end = datetime.datetime.now()
        print("cost time: " + str(end - start_lstm_inner))
