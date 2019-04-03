import pandas              
import numpy as np                  
train_data=pandas.read_csv(r'C:\Users\Administrator\Desktop\taitanic\train.csv')      #读取文件titanic_train数据集
test_data = pandas.read_csv(r'C:\Users\Administrator\Desktop\taitanic\test.csv')
#通过随机森林补充年龄

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
train_data.loc[train_data['Age'].isnull(), ['Age']] = predictAges

#众数补充港口

combined_train_test = train_data
#combined_train_test['Embarked'].fillna(combined_train_test['Embarked'].mode().iloc[0], inplace=True)
'''------------------------------------------------------------------------------------------------------------------------------'''

combined_train_test['Fare'] = combined_train_test[['Fare']].fillna(combined_train_test.groupby('Pclass').transform(np.mean))
train_data = combined_train_test 

combined_train_test = test_data
#combined_train_test['Embarked'].fillna(combined_train_test['Embarked'].mode().iloc[0], inplace=True)
'''------------------------------------------------------------------------------------------------------------------------------'''

combined_train_test['Fare'] = combined_train_test[['Fare']].fillna(combined_train_test.groupby('Pclass').transform(np.mean))
test_data = combined_train_test 


#loc是通过行标签索引行数据，iloc是通过行号获取行数据， ix是结合前两种的混合索引
#注意loc后面加的是中括号，不是小括号
train_data.loc[train_data['Sex']=='male','Sex']=0
train_data.loc[train_data['Sex']=='female','Sex']=1
test_data.loc[test_data['Sex']=='male','Sex']=0
test_data.loc[test_data['Sex']=='female','Sex']=1

train_data['Embarked']=train_data['Embarked'].fillna('S')
train_data.loc[train_data['Embarked']=='S','Embarked']=0
train_data.loc[train_data['Embarked']=='C','Embarked']=1
train_data.loc[train_data['Embarked']=='Q','Embarked']=2

test_data['Embarked']=test_data['Embarked'].fillna('S')
test_data.loc[test_data['Embarked']=='S','Embarked']=0
test_data.loc[test_data['Embarked']=='C','Embarked']=1
test_data.loc[test_data['Embarked']=='Q','Embarked']=2


'''
#这里用的是逻辑回归的算法方式
from sklearn import model_selection
from sklearn.linear_model import LogisticRegression
#Initialize our algorithm
predictors=['Pclass','Sex','Age','SibSp','Parch','Fare','Embarked']
alg=LogisticRegression(random_state=3)
#Compute the accuracy score for all the cross validation folds.(much simpler than what we did before!)
scores=model_selection.cross_val_score(alg,train_data[predictors],train_data['Survived'],cv=2)
#Take the mean of the scores(because we have one for each fold)
print(scores.mean())
'''

#以下用的是随机森林的算法方式
from sklearn import model_selection
from sklearn.model_selection import KFold
from sklearn.ensemble import RandomForestClassifier

predictors=['Pclass','Sex','Age','SibSp','Parch','Fare','Embarked']
traindata = train_data
testdata = test_data
#这里后面的samples不要少写一个“s”
#n_estimators是决策树的个数，min_samples_split是根据属性划分节点时，每个划分最少的样本数。min_samples_leaf:叶子节点最少的样本数。

UseFlag = traindata['Survived'].values
UseFeature = traindata[['Pclass','Sex','Age','SibSp','Parch','Fare','Embarked']].values
rf=RandomForestClassifier(random_state=1,n_estimators=100,min_samples_split=5,min_samples_leaf=2)
rf.fit(UseFeature,UseFlag)#进行模型的训练  
temp = rf.predict(UseFeature)
#print(temp)

testdata.Age[testdata.Age.isnull()] = 30
testdata.Fare[testdata.Fare.isnull()]=35
TestFeature = testdata[['Pclass','Sex','Age','SibSp','Parch','Fare','Embarked']].values

temp = rf.predict(TestFeature)
testdata['Survived'] = temp
outdata = testdata[['PassengerId','Survived']]#提取出需要的列
outdata.to_csv(r"C:\Users\Administrator\Desktop\taitanic\RF1.csv",index=False,header=True)#保存数据集
