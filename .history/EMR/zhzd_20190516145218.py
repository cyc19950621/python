#-*- coding: UTF-8 -*- 

#本文件用于提取目标目录中的所有txt，并提取关键词所在行到指定目录，并提取关键词新建文件
import time
import math
import os
import sys
import os, os.path,shutil
import codecs 
import EMRdef
import re
emrtxts = EMRdef.txttq(u'D:\DeepLearning ER\EHR')#txt目录提取
for emrtxt in emrtxts:
    f = open(emrtxt,'r',errors="ignore")#中文加入errors
    emrtxt = os.path.basename(emrtxt)
    emrtxt_str = re.findall(r'(^.+?)\_',emrtxt)#提取ID
    emrtxt = "".join(emrtxt_str)#转成str
    pattern = r',|.|，|。|;|；'#清除标点
    #txtp=txtp.decode('utf-8')
    temp=f.readlines()
    for line in temp:
        line = re.sub(' ','',line)#删除空格
        while True:
            temp.remove(line)
            if line.find (u'入院诊断：',0,6) >-1:
                break
    print(temp)