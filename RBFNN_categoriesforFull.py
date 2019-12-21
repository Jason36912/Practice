import pandas as pd
import numpy as np

for H1 in range(1,6,1):  #
        OPtype = 'Full' # 基于全谱的RBFNN
        # filename = ['H:/BYK/Spectra/',fold, '/averspectra- ', str(H1), '-', str(H2), '.csv']  #这种结果是list
        filename = 'F:/RBFNN_whichcategory/prediction/basedFullSpectrum/pretrain/RBFNN-' + OPtype + str(H1) + '.csv'  # 训练样本的预测标签文件夹
        #filename = 'F:/RBFNN_whichcategory/prediction/basedFullSpectrum/RBFNN-' + OPtype + str(H1) + '.csv' # test样本的预测标签文件夹
        df = pd.read_csv(filename, header=None)
        category = []
        result = pd.DataFrame()
        maxcol = df.shape[1]  # 读取最大列数
        for i in range(maxcol):
                a = np.argmax(df.iloc[:, i])  # 判断该列中最大行，并返回行号
                n = a + 1  # a的范围0123， +1即代表事先约定的标签1234
                category.append(n)
        result = result.append(category)  # 将列表转dataframe, 便于存储
        settype = 'Cal' # set的类型，calibration/ prediction
        result.to_csv('F:/RBFNN_whichcategory/prediction/basedFullSpectrum/' + OPtype + str(H1) +settype+ 'result' + '.csv', index=None,header=None)