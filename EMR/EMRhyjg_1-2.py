#-*- coding: UTF-8 -*- 

#本文件用于提取目标目录中的所有txt，并提取关键词所在行到指定目录，
# 并提取关键词新建文件，关键词 诊疗过程
import time
import math
import os
import sys
import os, os.path,shutil
import codecs 
import EMRdef
import re

#关键词提取 关键词为诊疗计划
emrtxts = EMRdef.txttq(u'D:\DeepLearning ER\EHR')#txt目录提取
zljhs = []
for emrtxt in emrtxts:
    f = open(emrtxt,'r',errors="ignore")#中文加入errors
    emrtxt = os.path.basename(emrtxt)
    emrtxt_str = re.findall(r'(^.+?)\_',emrtxt)#提取ID
    emrtxt = "".join(emrtxt_str)#转成str
    #txtp=txtp.decode('utf-8')
    for line in f.readlines():
        line = re.sub(' ','',line)#删除空格
        if line.find (u'诊疗过程：',0,6) >-1:
                line = re.sub(r'小时|H', 'h', line)
                EMRdef.text_create(r'D:\DeepLearning ER\EHRzlgc','.txt' ,emrtxt,line)#导出带有诊疗计划的文件和诊疗计划
            #zljhs.append(emrtxt+':'+line)
#EMRdef.text_save('D:\python\EMR\zljh.txt',zljhs)'''
'''------------------------------------------------------------------------------------------------------------'''

#根据句号分词
emrtxt2s = EMRdef.txttq(u'D:\DeepLearning ER\EHRzlgc')#txt目录提取
pattern2 = r'。'#根据标点分词
for emrtxt2 in emrtxt2s:
    f2 = open(emrtxt2,'r',errors="ignore")#中文加入errors
    f2_end = re.split(pattern2, f2.read())
    f2_out = "\n".join(f2_end)#转成str
    emrpath2 = os.path.basename(emrtxt2)
    emrpath2 = os.path.splitext(emrpath2)[0]
    EMRdef.text_create(u'D:\DeepLearning ER\EHRzlgc2','.txt',emrpath2,f2_out)
#EMRdef.text_save(emrtxt,f_end)'''
'''----------------------------------------------------------------------------------------------------------------------------'''
