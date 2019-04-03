import re
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings("ignore")
#导入数据
train_data = pd.read_csv(r'C:\Users\Administrator\Desktop\taitanic\train.csv')
test_data = pd.read_csv(r'C:\Users\Administrator\Desktop\taitanic\test.csv')
#总体数据信息
train_data.info()
test_data.info()
sum_data = train_data.append(test_data)
psg_out_id = test_data['PassengerId']
#train_data['Cabin'] = train_data.Cabin.fillna('U0') # 空余上船位置定义
'''
#随机森林填充年龄
from sklearn.ensemble import RandomForestRegressor
#choose training data to predict age
age_df = train_data[['Age','Survived','Fare', 'Parch', 'SibSp', 'Pclass']]
age_df_notnull = age_df.loc[(train_data['Age'].notnull())]
age_df_isnull = age_df.loc[(train_data['Age'].isnull())]
X = age_df_notnull.values[:,1:]
Y = age_df_notnull.values[:,0]
# use RandomForestRegression to train data
RFR = RandomForestRegressor(n_estimators=1000, n_jobs=-1)
RFR.fit(X,Y)
predictAges = RFR.predict(age_df_isnull.values[:,1:])
train_data.loc[train_data['Age'].isnull(), ['Age']]= predictAges
'''

train_data['Survived'].value_counts().plot.pie(autopct='%0.9f%%') #总体生存比例

#绘图 plt.show()
print(train_data.groupby(['Sex','Survived'])['Survived'].count())#性别和生存关系
print(train_data.groupby(['Sex','Pclass','Survived'])['Survived'].count())#船舱，性别与生存的关系


train_data[['Sex','Survived']].groupby(['Sex']).mean().plot.bar()#作图
train_data[['Pclass','Survived']].groupby(['Pclass']).mean().plot.bar()#船舱与生存的关系
train_data[['Sex','Pclass','Survived']].groupby(['Pclass','Sex']).mean().plot.bar()#船舱，性别与生存的关系作图


#年龄与生存的关系
'''
#其次看一下仓位因素
fig = plt.figure()
Us =train_data.Pclass[train_data.Survived == 0].value_counts()
S = train_data.Pclass[train_data.Survived == 1].value_counts()
df = pd.DataFrame({'Survived':S, 'Unsurvived':Us})
df.plot(kind='bar', stacked=True)
plt.title("The rescue of each passenger level ")
plt.xlabel("Level") 
plt.ylabel("Number of people") 
plt.xticks(rotation = 0)
'''
#仓位与年龄的关系
Us =train_data.Age[train_data.Survived == 0].value_counts()
S = train_data.Age[train_data.Survived == 1].value_counts()
df = pd.DataFrame({'Survived':S, 'Unsurvived':Us})
df.plot(kind='bar', stacked=True)
plt.title("Age to Survrive ")
plt.xlabel("Age") 
plt.ylabel("Number of people") 
plt.xticks(rotation = 0)

#港口与生存的关系

sns.countplot('Embarked',hue='Survived',data=train_data)
plt.title('Embarked and Survived')
#回归森林预测年龄
from sklearn.ensemble import RandomForestRegressor
#choose training data to predict age
age_df = sum_data[['Age','Title','Parch', 'SibSp','Pclass']]
age_df_notnull = age_df.loc[(sum_data['Age'].notnull())]
age_df_isnull = age_df.loc[(sum_data['Age'].isnull())]
X = age_df_notnull.values[:,1:]
Y = age_df_notnull.values[:,0]
# use RandomForestRegression to train data
RFR = RandomForestRegressor(n_estimators=1000, n_jobs=-1)
RFR.fit(X,Y)
predictAges = RFR.predict(age_df_isnull.values[:,1:])
sum_data.loc[sum_data['Age'].isnull(), ['Age']]= predictAges

#年龄分组
bins = [0, 12, 18, 65, 100]
sum_data['Age_group'] =sum_data['Age']
sum_data.loc[sum_data['Age_group'] >60,'Age_group'] = -4
sum_data.loc[sum_data['Age_group'] >30,'Age_group'] = -3
sum_data.loc[sum_data['Age_group'] >18,'Age_group'] = -2
sum_data.loc[sum_data['Age_group'] >0,'Age_group'] = 1
sum_data.loc[sum_data['Age_group'] ==-2,'Age_group'] = 2
sum_data.loc[sum_data['Age_group'] ==-3,'Age_group'] = 3
sum_data.loc[sum_data['Age_group'] ==-4,'Age_group'] = 4
pd.concat([sum_data,sum_data['Age_group']])
#亲友人数和生存的关系
n,ax=plt.subplots(1,2,figsize=(18,8))
train_data[['Parch','Survived']].groupby(['Parch']).mean().plot.bar(ax=ax[0])
ax[0].set_title('Parch and Survived')
train_data[['SibSp','Survived']].groupby(['SibSp']).mean().plot.bar(ax=ax[1])
ax[1].set_title('SibSp and Survived')
#称呼与生存
sum_data = train_data.append(test_data)
sum_data['Title'] = sum_data['Name'].map(lambda x: re.compile(", (.*?)\.").findall(x)[0])
title_Dict = {}
title_Dict.update(dict.fromkeys(['Capt', 'Col', 'Major', 'Dr', 'Rev'], 'Officer'))
title_Dict.update(dict.fromkeys(['Don', 'the Countess', 'Dona', 'Lady'], 'Royalty'))
title_Dict.update(dict.fromkeys(['Mme', 'Ms', 'Mrs','Mlle', 'Miss'], 'Mrs'))
title_Dict.update(dict.fromkeys(['Master','Mr', 'Sir'], 'Mr'))
title_Dict.update(dict.fromkeys(['Jonkheer'], 'Master'))
sum_data['Title'] = sum_data['Title'].map(title_Dict)

sum_data['Title'] = pd.factorize(sum_data['Title'])[0]
'''
title_dummies_df = pd.get_dummies(sum_data['Title'], prefix=sum_data[['Title']].columns[0])
sum_data = pd.concat([sum_data, title_dummies_df], axis=1)'''

sum_data['Cabin'].loc[(sum_data['Cabin'].notnull())] = 1
sum_data['Cabin'].loc[(sum_data['Cabin'].isnull())] = 0

train_data =sum_data[:891]
train_data[['Title','Survived']].groupby(['Title']).mean().plot.bar()
train_data[['Cabin','Survived']].groupby(['Cabin']).mean().plot.bar()#作图
plt.show()

