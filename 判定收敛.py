import os

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

doys = []
def judge(df, idx):
    result = df[idx:]['x'].apply(lambda temp: abs(temp)) < 0.1
    return False not in np.array(result)


def save(path, station_doy):
    plt.subplot(311)
    plt.plot(dataframe['epoch'], dataframe['x'])
    plt.tight_layout()
    plt.xticks([])
    plt.ylabel('y E')
    plt.subplot(312)
    plt.plot(dataframe['epoch'], dataframe['y'])
    plt.tight_layout()
    plt.ylabel('x N')
    plt.xticks([])
    plt.subplot(313)
    plt.plot(dataframe['epoch'], dataframe['z'])
    df_new = dataframe[dataframe.index % 10 == 0]
    plt.xticks(df_new['epoch'], rotation=40)
    plt.ylabel('z U')
    plt.xlabel(station + ' station E N U error')
    plt.tight_layout()
    plt.savefig(path + 'fig/' + station_doy + '.png')
    dataframe.to_csv(path + 'csv/' + station_doy + '.csv')


def search_ppp_results_files(each_station_path):
    ppp_results_files = []
    for file in os.listdir(each_station_path):
        if file.endswith('0.pos'):  # 搜索以 0.pos 结尾的文件
            ppp_results_files.append(file)
    return ppp_results_files


if __name__ == '__main__':
    baseDir = 'H:/lutaiwang/定位试验/conventional_PPP_Results/'
    # 找到定位结果文件
    target_dir = 'H/lutaiwang/定位试验/ppp_solution_results/conventional/'
    index = 0
    epoches = []
    xs = []
    ys = []
    zs = []
    stations = os.listdir(baseDir)
    # 遍历站
    for station in stations:
        # 遍历每站下每天的数据
        each_station_path = baseDir + station + '/'
        each_station_ppp_files = search_ppp_results_files(each_station_path)
        for each_doy_file in each_station_ppp_files:
            each_doy_file_path = baseDir + station + '/' + each_doy_file
            for line in open(each_doy_file_path):
                if index == 253:  # + 240:  # 读取1h的数据
                    break
                index = index + 1
                if line.startswith('%'):
                    continue
                epoch = line[11:19]
                x = float(line[28:40])
                y = float(line[45:57])
                z = float(line[63:74])
                epoches.append(epoch)
                xs.append(x)
                ys.append(y)
                zs.append(z)
            mean_x = np.average(xs)
            mean_y = np.average(ys)
            mean_z = np.average(zs)
            dataframe = pd.DataFrame(
                {'epoch': epoches, 'x': np.array(xs) - mean_x, 'y': np.array(ys) - mean_y, 'z': np.array(zs) - mean_z})
            flag = ''
            # 查找收敛时间
            for index, row in dataframe.iterrows():
                if judge(dataframe, index):
                    flag = row['epoch'].replace(':', '_')
                    save(target_dir, each_doy_file[:-5])
                    break
                else:
                    continue

            for doy in doy:
                for hour in doy.hour:
                    assert isinstance(hour, object)
                    np.sin(hour)*np.cos(hour)

