import pandas as pd 
import  numpy as np 
train_data=pd.read_csv(r'C:\Users\Administrator\Desktop\taitanic\train.csv')      #读取文件titanic_train数据集
test_data = pd.read_csv(r'C:\Users\Administrator\Desktop\taitanic\test.csv')
sum_data = train_data.append(test_data)
psg_out_id = test_data['PassengerId']

#回归森林预测年龄
from sklearn.ensemble import RandomForestRegressor
#choose training data to predict age
age_df = sum_data[['Age','Parch', 'SibSp', 'Pclass']]
age_df_notnull = age_df.loc[(sum_data['Age'].notnull())]
age_df_isnull = age_df.loc[(sum_data['Age'].isnull())]
X = age_df_notnull.values[:,1:]
Y = age_df_notnull.values[:,0]
# use RandomForestRegression to train data
RFR = RandomForestRegressor(n_estimators=1000, n_jobs=-1)
RFR.fit(X,Y)
predictAges = RFR.predict(age_df_isnull.values[:,1:])
sum_data.loc[sum_data['Age'].isnull(), ['Age']]= predictAges

#性别替换
sum_data.loc[sum_data['Sex']=='male','Sex'] = 0
sum_data.loc[sum_data['Sex']=='female','Sex'] = 1
#上船位置
sum_data['Embarked'] = sum_data['Embarked'].fillna('S')
sum_data.loc[sum_data['Embarked'] == 'S','Embarked'] = 0
sum_data.loc[sum_data['Embarked'] == 'C','Embarked'] = 1
sum_data.loc[sum_data['Embarked'] == 'Q','Embarked'] = 2
#票
sum_data['Fare'] = sum_data[['Fare']].fillna(sum_data.groupby('Pclass').transform(np.mean))
#年龄归一化
from sklearn import preprocessing
assert np.size(sum_data['Age']) == 1309
# StandardScaler will subtract the mean from each value then scale to the unit variance
scaler = preprocessing.StandardScaler()
sum_data['Age_scaled'] = scaler.fit_transform(sum_data['Age'].values.reshape(-1, 1))
assert np.size(sum_data['Fare']) == 1309
scaler = preprocessing.StandardScaler()
sum_data['Fare_scaled'] = scaler.fit_transform(sum_data['Fare'].values.reshape(-1, 1))
#随机森林决策树
from sklearn import model_selection
from sklearn.model_selection import KFold
from sklearn.ensemble import RandomForestClassifier
#两组数据分开
traindata =sum_data[:891]
testdata = sum_data[891:]
#这里后面的samples不要少写一个“s”
#n_estimators是决策树的个数，min_samples_split是根据属性划分节点时，每个划分最少的样本数。min_samples_leaf:叶子节点最少的样本数。

UseFlag = traindata['Survived'].values
UseFeature = traindata[['Pclass','Sex','Age','SibSp','Parch','Fare','Embarked']].values
rf = RandomForestClassifier(random_state=1,n_estimators=80,min_samples_split=5,min_samples_leaf=2)
rf.fit(UseFeature,UseFlag)#进行模型的训练  

temp = rf.predict(UseFeature)
TestFeature = testdata[['Pclass','Sex','Age','SibSp','Parch','Fare','Embarked']].values
temp = rf.predict(TestFeature)
testdata['Survived'] = temp

outdata = testdata[['PassengerId','Survived']]#提取出需要的列

outdata.to_csv(r"C:\Users\Administrator\Desktop\taitanic\RF3.csv",index=False,header=True)#保存数据集
#模型评价
# pd.DataFrame({"columns":list(UseFeature.columns)[1:], "coef":list(temp)})