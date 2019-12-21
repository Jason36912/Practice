import pandas as pd
import math

def maxlinenum(df):
    #end = df.index.max()+1
    end = df.shape[0]
    return end


#variety = ['01','02','03','04']
variety = '04'
file = ['1','2','3','4','5']
for H1 in file:

    #filename = ['H:/BYK/Spectra/',fold, '/averspectra- ', str(H1), '-', str(H2), '.csv']  #这种结果是list
    filename = 'F:/数据处理/singleVariety/kmeans/'+ variety+'/'+H1+'.csv'
    #filename = 'H:/BYK/Spectra/02/averspectra-1-3.csv'
    df = pd.read_csv(filename,header=None)
    end = maxlinenum(df)
    #num = end//3*2
    #num = round(end // 3 * 2)
    #num = math.ceil(end // 3 * 2)
    #num = math.ceil(end // 3 * 2) + 1
    #num = round(end // 3 * 2) + 1
    num = math.floor(end // 3 * 2) + 1
    #df_train = df.iloc[0:num-1,:]
    df_train = df.iloc[0:num, :]  # 序号从0 到num - 1的数据被取出
    df_train.to_csv('F:/数据处理/singleVariety/kmeans/'+ variety+'/'+ 'trainingset.csv', mode='a', header=None, index=None)
    df_prediction = df.iloc[num:,:]  # 这里需要与上面的num保持一致，否则会丢失一条数据！！！！
    df_prediction.to_csv('F:/数据处理/singleVariety/kmeans/'+ variety+'/'+'predset.csv', mode='a', header=None,index=None)