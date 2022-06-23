# -*- coding: utf-8 -*-
# @Time    : 2021/8/23 10:02
# @Author  : Zhang Huan
# @Email   : johnhuan@whu.edu.cn
# QQ       : 248404941
# @File    : tell_result_0.pos.lstmztd.py
import os
import shutil


def search_ppp_results_files(each_station_path, target_path):    
    for file in os.listdir(each_station_path):
        if file.endswith('0.pos'):  # 搜索以 0.pos 结尾的文件            
            shutil.copy(each_station_path + file, target_path)


if __name__ == '__main__':
    basepath = 'H:/lutaiwang/定位试验/ppp_lstmztd_PPP_Results/PPP Results/'
    target_path = 'F:/lutaiwang/定位实验/ppp_results/lstmztd/'
    stations = os.listdir(basepath)
    for station in stations:
        print(station)
        source_path = basepath + station+'/'
        search_ppp_results_files(source_path, target_path)
