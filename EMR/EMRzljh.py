#-*- coding: UTF-8 -*- 

#本文件用于提取目标目录中的所有txt，并提取关键词所在行到指定文件
import time
import math
import os
import sys
import os, os.path,shutil
import codecs 
import EMRdef
import re

emrtxts = EMRdef.txttq(u'D:\DeepLearning ER')#txt目录提取
zljhs = []
for emrtxt in emrtxts:
    #txtp=txtp.decode('utf-8')
    f = open(emrtxt,'r',errors="ignore")#中文加入errors
    for line in f.readlines():
        if line.find (u'诊疗计划') >-1:
            line = re.sub(' ','',line)#删除空格
            zljhs.append(emrtxt+line)
           # print(line)



EMRdef.text_save('D:\python\EMR\zljh.txt',zljhs)
