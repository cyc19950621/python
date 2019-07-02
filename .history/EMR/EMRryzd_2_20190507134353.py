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
ryzd=[]
for emrtxt in emrtxts:
    f = open(emrtxt,'r',errors="ignore")#中文加入errors
    emrpath = os.path.basename(emrtxt)
    emrpath = os.path.splitext(emrpath)[0]
    line_out = []
    for line in f.readlines():
            line = re.sub('\n','',line)
            line = re.sub(r'(.+?)肺炎','肺炎',line)#替换所有的肺炎
            for hxjbc in hxjbdic:#检索每个词
                hxjbc = re.sub('\n','',hxjbc)
                if line.find(hxjbc) >-1:
                    line_out.append(line)
            line_output = EMRdef.delre(line_out)
            ryzd.append(line_out)
            #line = '\n'.join(line_output)
            #EMRdef.text_create(r'D:\DeepLearning ER\EHRryzd2','.txt' ,emrpath,line)

import orangecontrib.associate.fpgrowth as oaf
often=dict(oaf.frequent_itemsets(ryzd, .01))#生成频繁度

rules = oaf.association_rules(often, .01, frozenset({'肺炎', '双肺间质纤维化'})  #这里设置置信度frozenset({'肺炎'})
rules = list(rules)

print(rules)