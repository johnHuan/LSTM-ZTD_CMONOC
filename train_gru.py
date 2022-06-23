import datetime

import matplotlib

matplotlib.use('Agg')
import matplotlib.pyplot as plt

import numpy as np
import pandas as pd
from tensorflow.keras.layers import Dense, GRU, Dropout
from tensorflow.keras.models import Sequential
from sklearn.preprocessing import MinMaxScaler


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
    dataframe_pred = pd.DataFrame(predict_ztd_no_system_bias)
    dataframe_pred.to_csv(output_path + "predict/" + station + '.csv')
    dataframe_test = pd.DataFrame(test_set)
    dataframe_test.to_csv(output_path + "test/" + station + '.csv')


# 载入数据
'''
start_year: 训练样本起始年份
end_year: 训练样本终止年份
month: 从训练样本终止后，继续往后预测多少个月
'''


def train(source_path, source_filename, output_path, 预测的数据量):
    filename = source_path + source_filename
    # grid = source_filename[:-4]
    dataset = pd.read_csv(filename, usecols=['year_doy', 'r_k_p'])
    # predict_period = month * 30 * 4
    total = dataset.shape[0]
    flag_index = total - 预测的数据量
    # 训练集合测试集的数据
    train_set = dataset[0:flag_index].iloc[:, 1:2].values
    test_set = dataset[flag_index:].iloc[:, 1:2].values
    # 正则化(归一化): 将每一维的特征映射到指定的区间：【0,1】
    sc = MinMaxScaler(feature_range=[0, 1])
    train_set_scaled = sc.fit_transform(train_set)

    # 创建序列数据集（训练和测试）
    # 训练步长  （=  month * 30 day * 4 epoch） 作为 `时间步` 为一个样本， 1个输出

    step = 每天多少个数据 * 30
    x_train, y_train = [], []
    for train_time_step in range(step, train_set.shape[0]):  # 训练`时间步`
        x_train.append(train_set_scaled[train_time_step - step:train_time_step, 0])
        y_train.append(train_set_scaled[train_time_step, 0])
    x_train, y_train = np.array(x_train), np.array(y_train)  # np类型变换

    # LSTM的输入：（samples, sequence_length, features）
    y_train = y_train.reshape(-1, 1)
    x_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1], 1))
    # 搭建LSTM网络模型， 进行训练和预测
    # LSTM 第一层
    model = Sequential()
    model.add(GRU(step, return_sequences=True, input_shape=(x_train.shape[1], x_train.shape[2])))
    model.add(Dropout(0.01))
    model.add(GRU(step, return_sequences=True))

    model.add(Dropout(0.01))
    model.add(GRU(step))
    model.add(Dropout(0.01))
    model.add(Dense(units=1))
    model.compile(optimizer='rmsprop', loss='mse')
    print(model.summary())
    dataset_total = dataset['r_k_p'][:]
    # 获取输入数据
    epoch = step
    # 获取输入数据
    inputs = dataset_total[len(dataset_total) - len(test_set) - epoch:].values
    # 归一化
    inputs = inputs.reshape(-1, 1)
    inputs = sc.transform(inputs)
    # 准备测试集x_test ， 进行预测
    x_test = []
    for i in range(epoch, inputs.shape[0]):
        x_test.append(inputs[i - epoch:i, 0])
    x_test = np.array(x_test)
    x_test = np.reshape(x_test, (x_test.shape[0], x_test.shape[1], 1))
    # 模型训练
    model.fit(x_train, y_train, epochs=10, batch_size=40)
    model.save(output_path + station + '_ztd.h5')
    predict_test = model.predict(x_test)
    predict_ztd = sc.inverse_transform(predict_test)
    plot_predictions(output_path, station, predict_ztd, test_set)
    save_data(output_path, station, predict_ztd, test_set)


if __name__ == '__main__':
    data_path = "H:/lutaiwang/source_data/residuals/"
    output_path = "H:/lutaiwang/source_data/gru/"
    station = "WUHN.csv"
    try:
        预测多少天 = 60
        每天多少个数据 = 24
        预测的数据量 = 预测多少天 * 每天多少个数据
        start_lstm_inner = datetime.datetime.now()
        train(data_path, station, output_path, 预测的数据量)
        end = datetime.datetime.now()
        print("耗时： " + str(end - start_lstm_inner))
    except Exception as ex:
        print(station + " station lstm model train exception: " + str(ex))



