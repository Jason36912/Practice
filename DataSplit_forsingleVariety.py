import pandas as pd
import numpy as np

file = ['01','02','03','04']
for H1 in file:
    filename = 'F:/数据处理/singleVariety/' + H1 + 'Labeled' + '.csv'
    # filename = 'H:/BYK/Spectra/02/averspectra-1-3.csv'
    df = pd.read_csv(filename, header=None)
    a1 = df[(df.iloc[:, 350] == 1)].shape[0]
    a2 = df[(df.iloc[:, 350] == 2)].shape[0]
    a3 = df[(df.iloc[:, 350] == 3)].shape[0]
    a4 = df[(df.iloc[:, 350] == 4)].shape[0]

    a = a1 + a2   #Label2的最大序号
    b = a1 + a2 + a3     #Label3的最大序号
    c = df.shape[0]      #Label4的最大序号
    begin = [0, a1 + 1, a + 1, b + 1]  #各个label的最小序号
    end = [a1, a, b, c]

    for i, j in zip(begin, end):
        third = (j - i) // 3 * 2  # 每个label取三分之二作为训练集
        third_ = i + third
        df_train = df.iloc[i:third_, :]
        df_train.to_csv('F:/数据处理/singleVariety/' + '/Split/'+H1 + 'trainingset.csv', mode='a', header=False, index=None)
        df_prediction = df.iloc[third_+1:j, :]
        df_prediction.to_csv('F:/数据处理/singleVariety/' + '/Split/' +H1+ 'predset.csv', mode='a', header=False, index=None)