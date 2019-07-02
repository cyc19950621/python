# -*- coding:utf-8 -*-
import re
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings("ignore")
#导入数据
data = pd.read_csv(r'D:\DeepLearning ER\sex_age.csv')
#总体数据信息
data.info()
#data[['SEX','AGE']].groupby(['AGE']).count().plot.bar()#船舱与生存的关系
sns.countplot('AGE',hue='SEX',data=data)
plt.title(u"入院年龄与性别状况")
plt.xlabel(u"年龄段") 
plt.ylabel(u"人数")
plt.show()

df=pd.DataFrame({u'男性':SEX_, u'女性':Survived_0})
df.plot(kind='bar', stacked=True)
plt.title(u"各登录港口乘客的获救情况")
plt.xlabel(u"登录港口") 
plt.ylabel(u"人数") 
