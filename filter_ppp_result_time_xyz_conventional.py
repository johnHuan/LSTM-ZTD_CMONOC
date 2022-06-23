
import os
import pandas as pd
base_path = 'F:/lutaiwang/定位实验/ppp_results/conventional/'
target_path = 'F:/lutaiwang/定位实验/ppp_results/time_xyz_conventional/'
files = os.listdir(base_path)
for file in files:
    file_path = base_path + file
    file_contents = open(file_path)
    times, x, y, z = [], [], [],[]
    for line in file_contents:
        if line.startswith('%'):
            continue
        times.append(line[0:23])
        x.append(float(line[27:40]))
        y.append(float(line[45:57]))
        z.append(float(line[61:74].lstrip().rstrip()))        
    file_contents.close()
    dataframe = pd.DataFrame({'time': times, 'x': x, 'y': y, 'z':z})
    dataframe.to_csv(target_path+file[:7]+'.csv', index=False)




