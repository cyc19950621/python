
import pandas as pd 
import  numpy as np 
import re
import matplotlib.pyplot as plt
train_data=pd.read_csv(r'C:\Users\Administrator\Desktop\taitanic\train.csv')      #读取文件titanic_train数据集
test_data = pd.read_csv(r'C:\Users\Administrator\Desktop\taitanic\test.csv')
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

title_dummies_df = pd.get_dummies(sum_data['Title'], prefix=sum_data[['Title']].columns[0])
sum_data = pd.concat([sum_data, title_dummies_df], axis=1)
train_data =sum_data[:891]
train_data[['Title','Survived']].groupby(['Title']).mean().plot.bar()
plt.show()

sum_data.loc[sum_data['Pclass'] == 1,'Pclass'] = 0
sum_data.loc[sum_data['Pclass'] == 2,'Pclass'] = 1
sum_data.loc[sum_data['Pclass'] == 3,'Pclass'] = 2
print(sum_data['Pclass'] )

UseFlag = traindata['Survived'].values
UseFeature = traindata[['Sex','Title','Age','FAF','Embarked','Cabin','Fare']].values
rf = RandomForestClassifier(random_state=1,n_estimators=100,min_samples_split=6,min_samples_leaf=3)
rf.fit(UseFeature,UseFlag)#进行模型的训练  

temp = rf.predict(UseFeature)
TestFeature = testdata[['Sex','Title','Age','FAF','Embarked','Cabin','Fare']].values
temp = rf.predict(TestFeature)
testdata['Survived'] = temp

outdata = testdata[['PassengerId','Survived']]#提取出需要的列

outdata.to_csv(r"C:\Users\Administrator\Desktop\taitanic\RF4.csv",index=False,header=True)#保存数据集
#模型评价
# pd.DataFrame({"columns":list(UseFeature.columns)[1:], "coef":list(temp)})

