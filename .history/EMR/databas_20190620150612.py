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
def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        plt.text(rect.get_x()+rect.get_width()/2.-0.2, 1.03*height, '%s' % float(height))

--------------------- 
作者：水之魂2018 
来源：CSDN 
原文：https://blog.csdn.net/weixin_40198632/article/details/78858663 
版权声明：本文为博主原创文章，转载请附上博文链接！
sns.countplot('AGE',hue='SEX',data=data)
plt.show()