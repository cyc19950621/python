import re
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings("ignore")
#导入数据
train_data = pd.read_csv(r'z:\\train.csv')
#总体数据信息
train_data.info()
