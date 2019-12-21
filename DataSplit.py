import pandas as pd

def maxlinenum(df):
    #end = df.index.max()+1
    end = df.shape[0]
    return end

file = ['1','2','3','4']
for H1 in file:

    #filename = ['H:/BYK/Spectra/',fold, '/averspectra- ', str(H1), '-', str(H2), '.csv']  #这种结果是list
    filename = 'E:/kmeans/'+H1+'.csv'
    #filename = 'H:/BYK/Spectra/02/averspectra-1-3.csv'
    df = pd.read_csv(filename,header=None)
    end = maxlinenum(df)
    num = end//3*2
    df_train = df.iloc[0:num,:]
    df_train.to_csv('E:/kmeans/' + '/Split/' + 'trainingset.csv', mode='a', header=False, index=None)
    df_prediction = df.iloc[num:,:]
    df_prediction.to_csv('E:/kmeans/'+'/Split/'+'predset.csv', mode='a', header=False,index=None)
