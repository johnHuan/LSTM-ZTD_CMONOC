# -*- coding: utf-8 -*-
# @Time    : 2021/8/23 9:51
# @Author  : Zhang Huan
# @Email   : johnhuan@whu.edu.cn
# QQ       : 248404941
# @File    : tell_result_files.py
import os
import shutil


def search_ppp_results_files(each_station_path, target_path):
    ppp_results_files = []
    for file in os.listdir(each_station_path):
        if file.endswith('0.pos'):  # 搜索以 0.pos 结尾的文件
            shutil.copy(each_station_path + file, target_path)


if __name__ == '__main__':
    basepath = 'H:/lutaiwang/定位试验/ppp_conventional_PPP_Results/'
    target_path = 'F:/lutaiwang/定位实验/ppp_results/conventional/'
    stations = os.listdir(basepath)
    for station in stations:
        source_path = basepath + station+'/'
        search_ppp_results_files(source_path, target_path)
