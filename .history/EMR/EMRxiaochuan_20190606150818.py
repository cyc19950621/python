#-*- coding: UTF-8 -*- 

#本文件用于提取目标目录中的所有txt，并提取关键词所在行到指定目录，
# 并提取关键词新建文件，关键词 主诉
import os
import sys
import os, os.path,shutil
import codecs 
import EMRdef
import re

#关键词提取 关键词为诊疗计划
emrtxts = EMRdef.txttq(u'D:\DeepLearning ER\EHR')#txt目录提取
pattern2 = r'。|：|、|，'#根据标点分词
zljhs = []
for emrtxt in emrtxts:
    f = open(emrtxt,'r',errors="ignore")#中文加入errors
    emrtxt = os.path.basename(emrtxt)
    emrtxt_str = re.findall(r'(^.+?)\_',emrtxt)#提取ID
    emrtxt = "".join(emrtxt_str)#转成str
    a_out = f.readlines()
    #txtp=txtp.decode('utf-8')
    for line in a_out:
        line = re.sub(' ','',line)#删除空格
        if line.find (u'诊断：') >-1:
                f2_out = "".join(a_out)#转成str
                EMRdef.text_create(r'D:\DeepLearning ER\EHRxiaochuan','.txt' ,emrtxt,f2_out)#导出
            #zljhs.append(emrtxt+':'+line)
#EMRdef.text_save('D:\python\EMR\zljh.txt',zljhs)'''
'''------------------------------------------------------------------------------------------------------------'''
