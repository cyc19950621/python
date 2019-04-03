import pandas as pd 
import  numpy as np 
import re
import matplotlib.pyplot as plt
import seaborn as sns
train_data=pd.read_csv(r'C:\Users\Administrator\Desktop\taitanic\train.csv')      #读取文件titanic_train数据集
test_data = pd.read_csv(r'C:\Users\Administrator\Desktop\taitanic\test.csv')
sum_data = train_data.append(test_data)
psg_out_id = test_data['PassengerId']

##名字开头
sum_data['Title'] = sum_data['Name'].map(lambda x: re.compile(", (.*?)\.").findall(x)[0])
title_Dict = {}
title_Dict.update(dict.fromkeys(['Capt', 'Col', 'Major', 'Dr', 'Rev'], 'Officer'))
title_Dict.update(dict.fromkeys(['Don', 'the Countess', 'Dona', 'Lady'], 'Royalty'))
title_Dict.update(dict.fromkeys(['Mme', 'Ms', 'Mrs','Mlle', 'Miss'], 'Mrs'))
title_Dict.update(dict.fromkeys(['Master','Mr', 'Sir'], 'Mr'))
title_Dict.update(dict.fromkeys(['Jonkheer'], 'Master'))
sum_data['Title'] = sum_data['Title'].map(title_Dict)
sum_data['Title'] = pd.factorize(sum_data['Title'])[0]

#亲友
sum_data['FAF']= sum_data['SibSp'] + sum_data['Parch']
pd.concat([sum_data,sum_data['FAF']])
#性别替换
sum_data.loc[sum_data['Sex']=='male','Sex'] = 0
sum_data.loc[sum_data['Sex']=='female','Sex'] = 1
#上船位置
sum_data['Embarked'] = sum_data['Embarked'].fillna('S')
sum_data.loc[sum_data['Embarked'] == 'S','Embarked'] =0
sum_data.loc[sum_data['Embarked'] == 'C','Embarked'] = 1
sum_data.loc[sum_data['Embarked'] == 'Q','Embarked'] = 1
#船舱
sum_data['Cabin'].loc[(sum_data['Cabin'].notnull())] = 1
sum_data['Cabin'].loc[(sum_data['Cabin'].isnull())] = 0
#票
sum_data['Fare'] = sum_data[['Fare']].fillna(sum_data.groupby('Pclass').transform(np.mean))

#等级

sum_data.loc[sum_data['Pclass'] == 1,'Pclass'] = 1
sum_data.loc[sum_data['Pclass'] == 2,'Pclass'] = 0
sum_data.loc[sum_data['Pclass'] == 3,'Pclass'] = -1

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
sum_data.loc[sum_data['Age_group']  > 65,'Age_group'] = -4
sum_data.loc[sum_data['Age_group'] >30,'Age_group'] = -3
sum_data.loc[sum_data['Age_group'] >15,'Age_group'] = -2
sum_data.loc[sum_data['Age_group'] >0,'Age_group'] = 1
sum_data.loc[sum_data['Age_group'] ==-2,'Age_group'] = 0
sum_data.loc[sum_data['Age_group'] ==-3,'Age_group'] = 0
sum_data.loc[sum_data['Age_group'] ==-4,'Age_group'] = -1
pd.concat([sum_data,sum_data['Age_group']])
#年龄归一化
from sklearn import preprocessing
assert np.size(sum_data['Age']) == 1309
# StandardScaler will subtract the mean from each value then scale to the unit variance
scaler = preprocessing.StandardScaler()
sum_data['Age_scaled'] = scaler.fit_transform(sum_data['Age'].values.reshape(-1,1))
assert np.size(sum_data['Fare']) == 1309
scaler = preprocessing.StandardScaler()
sum_data['Fare_scaled'] = scaler.fit_transform(sum_data['Fare'].values.reshape(-1,1))


#随机森林决策树
from sklearn import model_selection
from sklearn.model_selection import KFold
from sklearn.ensemble import RandomForestClassifier
#两组数据分开
traindata =sum_data[:891]
testdata = sum_data[891:]
#这里后面的samples不要少写一个“s”
#n_estimators是决策树的个数，min_samples_split是根据属性划分节点时，每个划分最少的样本数。min_samples_leaf:叶子节点最少的样本数。
#predictors = ['Sex','Title','Age','Embarked','FAF','Age_group','Cabin','Fare']
#predictors = ['Sex','Title','Age','Age_group','FAF','Embarked','Pclass','Cabin','Fare']
#predictors = ['Sex','Title','Age_scaled','Age_group','FAF','Embarked','Cabin','Fare_scaled']
#predictors =['Sex','Cabin',Age_group','Title','FAF','Embarked','Fare_scaled']
#['Pclass', 'Age','AgeCat','SibSp', 'Parch', 'Fare', 'Embarked', 'TicketId', 'CabinNum', 'Title','Cabin','FareCat', 'FamlSize','FamilySurv','Sex']
predictors = ['Pclass','Age','Age_scaled','Age_group','SibSp', 'Parch','Fare','Embarked','Title','Cabin','FAF','Sex']
from sklearn import model_selection
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score

#max_depth = 5, min_samples_split = 4, n_estimators = 500, random_state = 20, n_jobs = -1
alg = RandomForestClassifier(max_depth = 5, min_samples_split = 10, n_estimators = 500, random_state = 20, n_jobs = -1)
scores = cross_val_score(alg,traindata[predictors],traindata["Survived"],cv=12)
print(scores)
print(scores.mean())
'''
Correlation = pd.DataFrame(traindata[['Embarked', 'Sex', 'Title', 'Age_group', 'FAF','Fare', 'Pclass',  'Age', 'Cabin','SibSp','Parch','Survived']])
colormap = plt.cm.viridis
plt.figure(figsize=(14,12))
plt.title('Pearson Correlation of Features', y=1.05, size=15)
sns.heatmap(Correlation.astype(float).corr(),linewidths=0.1,vmax=1.0, square=True, cmap=colormap, linecolor='white', annot=True)
plt.show()
'''

