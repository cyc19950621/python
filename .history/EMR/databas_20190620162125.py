# -*- coding:utf-8 -*-
import re
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
warnings.filterwarnings("ignore")
#导入数据
data = pd.read_csv(r'D:\DeepLearning ER\00.csv')
#总体数据信息
data.info()
#data[['SEX','AGE']].groupby(['AGE']).count().plot.bar()#船舱与生存的关系


#df.plot(kind='bar', stacked=True)

g=sns.countplot('AGE',hue='SEX',data=data)
plt.title(u"入院年龄与性别状况")
plt.xlabel(u"年龄段") 
plt.ylabel(u"人数")
grouped_values = data.groupby("AGE").sum().reset_index()

plt.show()
