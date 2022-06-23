import os

import pandas as pd

if __name__ == '__main__':
    ztd_basedir = 'F:/lutaiwang/source_data/lstm/product/'
    target_dir = 'F:/lutaiwang/定位实验/period_ztds/'
    epoches = pd.date_range(start="20180107", end="20180301", freq="30s").array
    epoches = pd.DataFrame(epoches)[:-1][0]
    stations = os.listdir(ztd_basedir)
    for station_file in stations:
        station = station_file[:-4]
        station_path = ztd_basedir + station_file
        original_ztd_list = pd.read_csv(station_path, usecols=['ymfh', 'period_model'])
        original_ztd_list = original_ztd_list[167: 1439]
        ztd = []
        doy_t = []
        t = []
        zhd = []
        zwd = []
        ztd_rms = []
        for s in range(0, len(original_ztd_list)):  # original_ztd_list-> len: 1272    1272*120=152640=len(epoches)
            for l in range(s * 120, s * 120 + 120):
                doy_t.append(original_ztd_list.values[s][0])
                ele = '%.4f' % original_ztd_list.values[s][1]
                ztd.append(ele)
                dd = str(pd.DatetimeIndex([epoches.values[l]])[0])
                ele_t_t = dd + ".000"
                t.append(ele_t_t)
                zwd = "0.0033"
                zhd = "0.0033"
                ztd_rms = "0.0033"
        dataframe = pd.DataFrame({'t': t, 'ztd': ztd, 'ztd_rms': ztd_rms, 'zhd': zhd, 'zwd': zwd, 'doy_t': doy_t})
        dataframe.to_csv(target_dir + 'all.csv', index=False, header=False)
        span = 2880
        size = dataframe.shape[0]
        for index, row in dataframe.iterrows():
            doy = row['doy_t'][5:8]
            filepath = target_dir + '/stations/' + str(station).lower() + doy + '0.pos.trp'
            each_line = "{0:<10}{1:>10}{2:>10}{3:>10}{4:>10}".format(row['t'].replace('-', '/'), row['ztd'], row['zwd'],
                                                                     row['zhd'], row['ztd_rms'])
            with open(filepath, 'a+', encoding='utf-8', newline='') as f:
                f.write(each_line + '\n')
