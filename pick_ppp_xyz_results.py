# -*- coding: utf-8 -*-
# @Time    : 2021/8/22 17:33
# @Author  : Zhang Huan
# @Email   : johnhuan@whu.edu.cn
# QQ       : 248404941
# @File    : pick_ppp_xyz_results.py
import os


def get_last_line(filename):
    """
    get last line of a file
    :param filename: file name
    :return: last line or None for empty file
    """
    try:
        filesize = os.path.getsize(filename)
        if filesize == 0:
            return None
        else:
            with open(filename, 'rb') as fp:  # to use seek from end, must use mode 'rb'
                offset = -8  # initialize offset
                while -offset < filesize:  # offset cannot exceed file size
                    fp.seek(offset, 2)  # read # offset chars from eof(represent by number '2')
                    lines = fp.readlines()  # read from fp to eof
                    if len(lines) >= 2:  # if contains at least 2 lines
                        return lines[-1]  # then last line is totally included
                    else:
                        offset *= 2  # enlarge offset
                fp.seek(0)
                lines = fp.readlines()
                return lines[-1]
    except FileNotFoundError:
        print(filename + ' not found!')
        return None


if __name__ == '__main__':
    baseDir = 'H:/lutaiwang/定位试验/conventional_PPP_Results/'
    # 找到定位结果文件
    target_dir = 'H:/lutaiwang/lutaiwang_positions.txt'
    stations = os.listdir(baseDir)
    try:
        for station in stations:
            path = baseDir + station + '/' + station + '0580.pos'
            line = get_last_line(path)
            x = '%.4f' % float(line[23:42].lstrip().rstrip())
            y = '%.4f' % float(line[43:60].lstrip().rstrip())
            z = '%.4f' % float(line[61:76].lstrip().rstrip())
            each_line = "{0:>14}{1:>14}{2:>14}{3:>5}".format(x, y, z, station)
            print(station+ '---'+each_line)

            with open(target_dir, 'a+', encoding='utf-8', newline='') as f:
                f.write(each_line + '\n')
    except Exception as ex:
        print(str(ex))
