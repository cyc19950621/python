#-*- coding: UTF-8 -*- 

#本文件用于数据清洗
import time
import math
import os
import sys
import os, os.path,shutil
import codecs 
import EMRdef
import re
emrtxts = EMRdef.txttq(u'D:\DeepLearning ER\EHRryzd')#txt目录提取
hxjb = open(r'D:\python\EMR\hxjbml.txt',errors="ignore")#呼吸疾病目录
hxjbdic = hxjb.readlines()#读行
line_out = []
for emrtxt in emrtxts:
    f = open(emrtxt,'r',errors="ignore")#中文加入errors
    emrpath = os.path.basename(emrtxt)
    emrpath = os.path.splitext(emrpath)[0]
    for line in f.readlines():
            line = re.sub('\n','',line)
            line = re.sub(r'(.+?)肺炎','肺炎',line)#替换所有的肺炎
            for hxjbc in hxjbdic:#检索每个词
                hxjbc = re.sub('\n','',hxjbc)
                if line.find(hxjbc) >-1:
                    line_out.append(line)
line_output = EMRdef.delre(line_out)
from sklearn.feature_extraction.text import  CountVectorizer, TfidfTransformer

wordList=line_output#必须变成列表个是才能输入下面的向量化函数
count_vect = CountVectorizer(min_df=1,analyzer ='word')  # 并且设置了停用词表为列表stopWord，即在向量化时去掉停用词不统计，词至少在1个文档中出现过
words_vec = count_vect.fit_transform(wordList)
print(words_vec.toarray())#得到分词的系数矩阵
#print(words_vec.todense())
vec1=pd.DataFrame(words_vec.toarray())
print(count_vect.get_feature_names())#获得上面稀疏矩阵的列索引，即特征的名字（就是分词）