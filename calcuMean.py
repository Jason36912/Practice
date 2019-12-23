import pandas as pd

variety = '04'  ##水稻品种
diseasetype = ['CK','WKB','DWB','BYK']

filename = 'F:/数据处理/原始分散数据/'+'CK'+'avg'+variety+'.csv'
objectfile = 'E:/EXPERIMENT/SGmethod/'+variety+'mean.csv'

for ty in diseasetype:
    filename = 'F:/数据处理/原始分散数据/'+ty+'avg'+variety+'.csv'
    df = pd.read_csv(filename,header=None)
    df_mean = df.mean(axis=0) #按列求平均
    df_mean_t = pd.DataFrame(df_mean).T #实现转置为行，否则存储为了一列
    df_mean_t.to_csv(objectfile,mode='a', header=False, index=None)