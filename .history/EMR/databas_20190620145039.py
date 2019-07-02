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