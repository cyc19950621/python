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
sum_data.loc[sum_data['Embarked'] == 'S','Embarked'] = 0
sum_data.loc[sum_data['Embarked'] == 'C','Embarked'] = 1
sum_data.loc[sum_data['Embarked'] == 'Q','Embarked'] = 2
#船舱
sum_data['Cabin'].loc[(sum_data['Cabin'].notnull())] = 1
sum_data['Cabin'].loc[(sum_data['Cabin'].isnull())] = 0
#票
sum_data['Fare'] = sum_data[['Fare']].fillna(sum_data.groupby('Pclass').transform(np.mean))
#等级

sum_data.loc[sum_data['Pclass'] == 1,'Pclass'] = 0
sum_data.loc[sum_data['Pclass'] == 2,'Pclass'] = 0
sum_data.loc[sum_data['Pclass'] == 3,'Pclass'] = 2
#sum_data.loc[sum_data['Pclass'] == 4,'Pclass'] = 3

#回归森林预测年龄
from sklearn.ensemble import RandomForestRegressor
#choose training data to predict age
age_df = sum_data[['Age','Title','Parch', 'SibSp', 'Pclass']]
age_df_notnull = age_df.loc[(sum_data['Age'].notnull())]
age_df_isnull = age_df.loc[(sum_data['Age'].isnull())]
X = age_df_notnull.values[:,1:]
Y = age_df_notnull.values[:,0]
# use RandomForestRegression to train data
RFR = RandomForestRegressor(n_estimators=1000, n_jobs=-1)
RFR.fit(X,Y)
predictAges = RFR.predict(age_df_isnull.values[:,1:])
sum_data.loc[sum_data['Age'].isnull(), ['Age']]= predictAges

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



from sklearn import model_selection
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score
#predictors = [ 'FAF','SibSp',  'Age','Embarked','Fare','Cabin', 'Pclass','Sex', 'Title']     0.811
#predictors = [ 'FAF', 'Age','Embarked','Fare','Cabin', 'Pclass','Sex', 'Title']                  0.818
#predictors = [ 'FAF','SibSp',  'Age','Embarked','Fare','Cabin','Sex', 'Title']                   0.816
#predictors = ['Sex', 'Title', 'FAF','SibSp',  'Age','Embarked','Fare','Cabin', 'Pclass']     0.817
#predictors = ['Sex', 'Title', 'FAF','SibSp','Embarked','Fare','Cabin', 'Pclass']                0.804
#predictors = ['Sex', 'Title', 'FAF',  'Age','Embarked','Fare','Cabin', 'Pclass']                 0.817
#predictors = ['Sex', 'Title', 'FAF', 'Age','Embarked','Fare','Cabin']                                0.811
#predictors = ['Sex', 'Age', 'Title', 'FAF','Embarked','Fare','Cabin', 'Pclass']                  0.816
#predictors = ['Sex', 'Title', 'FAF','Cabin',  'Age','Embarked','Fare', 'Pclass']                 0.814
#predictors = ['Sex', 'Pclass', 'Title', 'FAF',  'Age','Embarked','Fare','Cabin']                 0.814
#predictors = [ 'Pclass','Sex',  'Age','Cabin','Title']                                                         0.795
#predictors =['Sex','Title','Age','FAF', 'Pclass','Embarked','Cabin','Fare']                      0.819
#predictors =['Sex','Title','Age','FAF', 'Pclass','Embarked','Cabin','Fare','Parch']          0.821     
predictors =['Sex','Title','Age','FAF', 'Pclass','Embarked','Cabin','Fare','Parch']            #0.825 16 1 |0.824 16 2| 0.826 6 2|0.828 |5 2 |4 2 |5 3|0.830 10 1|0.83170  9 1|0.83168 8 2|0.8328 9 2 
alg = RandomForestClassifier(random_state=1,n_estimators = 100,min_samples_split=6,min_samples_leaf=2)
scores = cross_val_score(alg,traindata[predictors],traindata["Survived"],cv=10)
print(scores)
print(scores.mean())
'''
Correlation = pd.DataFrame(traindata[['Embarked', 'Sex', 'Title',  'FAF','Fare', 'Pclass',  'Age', 'Cabin','SibSp','Parch','Survived']])
colormap = plt.cm.viridis
plt.figure(figsize=(14,12))
plt.title('Pearson Correlation of Features', y=1.05, size=15)
sns.heatmap(Correlation.astype(float).corr(),linewidths=0.1,vmax=1.0, square=True, cmap=colormap, linecolor='white', annot=True)
plt.show()
'''