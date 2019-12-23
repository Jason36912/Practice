import pandas as pd
import numpy as np

def maxlinenum(df):
    #end = df.index.max()+1
    end = df.shape[0]
    return end

file = ['01','02','03','04']  #水稻品种
leavetype = ['CK','WKB','DWB','BYK']  #病害品种
for H1 in file:
    for ty in leavetype:
        for i in range(1,6,1):
            filename = 'F:/数据处理/singleVariety/Kmeans/' + '/'+H1+ '/' +ty+ '/'+str(i)+'Labeled' + '.csv'
            df = pd.read_csv(filename, header=None)
            end = maxlinenum(df)
            third = round(end / 3 * 2)  # 每个label取三分之二作为训练集
            df_train = df.iloc[0:third, :]
            df_train.to_csv('F:/数据处理/singleVariety/Kmeans/' + '/'+H1+ '/' + 'trainingset.csv', mode='a', header=False, index=None)
            df_prediction = df.iloc[third:, :]
            df_prediction.to_csv('F:/数据处理/singleVariety/Kmeans/' +'/' + H1+ '/'+ 'predset.csv', mode='a', header=False, index=None)