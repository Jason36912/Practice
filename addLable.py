import pandas as pd

def maxlinenum(df):
    #end = df.index.max()+1
    end = df.shape[0]
    return end

# leavetype = 'CK'
# lable = 1
# leavetype = 'WKB'
# lable = 2
# leavetype = 'DWB'
# lable = 3
leavetype = 'BYK'
lable = 4
# filename = ['H:/BYK/Spectra/',fold, '/averspectra- ', str(H1), '-', str(H2), '.csv']  #这种结果是list
filename = 'F:/数据处理/混合样本/' + leavetype + 'avg' + '.csv'
# filename = 'H:/BYK/Spectra/02/averspectra-1-3.csv'
df = pd.read_csv(filename,header=None)  #注意header=None,不然丢失一行
end = maxlinenum(df)
df['Label'] = [lable for _ in range(end) ]
df.to_csv('F:/数据处理/混合样本/'+leavetype+'Labeled'+'.csv', mode='a', header=False,index=None)

