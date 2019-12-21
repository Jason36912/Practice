import pandas as pd

def maxlinenum(df):
    #end = df.index.max()+1
    end = df.shape[0]
    return end

leavetype = 'CK'
label = 1
# leavetype = 'WKB'
# label = 2
# leavetype = 'DWB'
# label = 3
# leavetype = 'BYK'
# label = 4

#variety = '04'  #01,02,03,04中浙，9优，中早，秀水
# # filename = ['H:/BYK/Spectra/',fold, '/averspectra- ', str(H1), '-', str(H2), '.csv']  #这种结果是list
# filename = 'F:/数据处理/原始分散数据/' + leavetype + 'avg'+variety + '.csv'
# # filename = 'H:/BYK/Spectra/02/averspectra-1-3.csv'
# df = pd.read_csv(filename,header=None)  #注意header=None,不然丢失一行
# end = maxlinenum(df)
#
# df['Label'] = [label for _ in range(end) ]
# df.to_csv('F:/数据处理/singleVariety/'+variety+'Labeled'+'.csv', mode='a', header=False,index=None)

################################20191216修正
fold = '01'  #01,02,03,04中浙，9优，中早，秀水
#kmeannum = ['1','2','3','4','5']  list 不能直接用于路径
leavetype =['CK','WKB','DWB','BYK']
label = [1,2,3,4]
for a,b in zip(leavetype,label):
    for i in range(1,6,1):
        filename = 'F:/数据处理/singleVariety/kmeans/' +fold+'/'+ a +'/'+ str(i) + '.csv'
        # filename = 'H:/BYK/Spectra/02/averspectra-1-3.csv'
        df = pd.read_csv(filename,header=None)  #注意header=None,不然丢失一行
        end = maxlinenum(df)

        df['Label'] = [b for _ in range(end)]
        df.to_csv('F:/数据处理/singleVariety/kmeans/' +fold+'/'+ a +'/'+ str(i)  +'Labeled'+'.csv', mode='a', header=False,index=None)