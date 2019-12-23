import pandas as pd

leavetype = ['CK','WKB','DWB','BYK']
for H1 in leavetype:
        #filename = ['H:/BYK/Spectra/',fold, '/averspectra- ', str(H1), '-', str(H2), '.csv']  #这种结果是list
        filename = 'F:/数据处理/混合样本/'+str(H1)+'Labeled'+'.csv'
        #filename = 'H:/BYK/Spectra/02/averspectra-1-3.csv'
        df = pd.read_csv(filename,header=None)
        df.to_csv('F:/数据处理/混合样本/'+'LabeledMerge'+'.csv', mode='a', header=False,index=None)
