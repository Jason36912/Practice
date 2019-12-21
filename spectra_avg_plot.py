import pandas as pd


leavetype = 'DWB'
# filename = ['H:/BYK/Spectra/',fold, '/averspectra- ', str(H1), '-', str(H2), '.csv']  #这种结果是list
filename = 'F:/数据处理/混合样本/' + leavetype + 'avg' + '.csv'
# filename = 'H:/BYK/Spectra/02/averspectra-1-3.csv'
df = pd.read_csv(filename)
avg = df.mean(axis=0) # 按列求平均，垂直向下
avg.to_csv('F:/数据处理/混合样本/' + leavetype + 'avgforplot' + '.csv', header=False, index=None)
df = None