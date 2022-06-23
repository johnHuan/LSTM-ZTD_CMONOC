# -*- coding: utf-8 -*-
# @Time    : 2021/12/8 22:52
# @Author  : Zhang Huan
# @Email   : johnhuan@whu.edu.cn
# QQ       : 248404941
# @File    : demo.py
if __name__ == '__main__':
    pi_o = 6
    pi_c = 5
    pi_e = 4
    cita = 1.5
    rou = 0.9
    delta = 0.5
    G = 0.1  # 自变量
    yita_o = 3
    yita_c = 2
    yita_e = 1
    miu_1 = 1.2
    miu_2 = 1.1
    miu_3 = 1
    lambda_1 = 2
    lambda_2 = 1.8
    lambda_3 = 1.6
    V_zN = (pi_o + pi_c + pi_e) * cita * G / (rou + delta) + \
           pi_o * (2 * pi_c + 2 * pi_e + pi_o) * (miu_1 + (cita * lambda_1) / (rou + delta)) ** 2 / (2 * rou * yita_o) + \
           pi_c * (2 * pi_o + 2 * pi_c + pi_c) * (miu_2 + (cita * lambda_2) / (rou + delta)) ** 2 / 2 * rou * yita_c + \
           pi_e * (2 * pi_o + 2 * pi_c + pi_e) * (miu_3 + (cita * lambda_3) / (rou + delta)) ** 2 / (2 * rou * yita_e)

    V_zO = (pi_o + pi_c + pi_e) * cita * G / (rou + delta) + \
           pi_o * (2 * pi_c + 2 * pi_e + pi_o) * (miu_1 + (cita * lambda_1) / (rou + delta)) ** 2 / (2 * rou * yita_o) + \
           (4 * pi_o ** 2 + 8 * pi_o * pi_c + 3 * pi_c ** 2 + 4 * pi_o * pi_e + 2 * pi_c * pi_e) * (
                   miu_2 + cita * lambda_2 / (rou + cita)) / (8 * rou * yita_c) + \
           (4 * pi_o ** 2 + 8 * pi_o * pi_e + 3 * pi_e ** 2 + 4 * pi_o * pi_c + 2 * pi_c * pi_e) * (
                   miu_3 + cita * lambda_3 / (rou + cita)) / (8 * rou * yita_e)

    V_zC = (pi_o + pi_c + pi_e) * cita * G / (rou + delta) + \
           (pi_o + pi_c + pi_e) ** 2 * (pi_o + pi_c + pi_e) ** 2 * (miu_1 + cita * lambda_1 / (rou + delta)) ** 2 / (
                   2 * rou * yita_o) + \
           (pi_o + pi_c + pi_e) ** 2 * (pi_o + pi_c + pi_e) ** 2 * (miu_2 + cita * lambda_2 / (rou + delta)) ** 2 / (
                   2 * rou * yita_c) + \
           (pi_o + pi_c + pi_e) ** 2 * (pi_o + pi_c + pi_e) ** 2 * (miu_3 + cita * lambda_3 / (rou + delta)) ** 2 / (
                   2 * rou * yita_e)

    print("V_zN: " + str(V_zN))
    print("=-----------------------")
    print("V_zO: " + str(V_zO))
    print("=-----------------------")
    print("V_zC: " + str(V_zC))
