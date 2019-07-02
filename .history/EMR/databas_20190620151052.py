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