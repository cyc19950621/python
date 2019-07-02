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
zljhs = []
for emrtxt in emrtxts:
    f = open(emrtxt,'r',errors="ignore")#中文加入errors
    emrtxt = os.path.basename(emrtxt)
    emrtxt_str = re.findall(r'(^.+?)\_',emrtxt)#提取ID
    emrtxt = "".join(emrtxt_str)#转成str
    pattern = r',|.|，|。|;|；'#清除标点
    #txtp=txtp.decode('utf-8')
    for line in f.readlines():
        line = re.sub(' ','',line)#删除空格
        if line.find (u'入院诊断：',0,6) >-1:
                line = re.sub(r'h|H', '小时', line)#小时替换成中文      
                line = re.sub(r'入院诊断：', '', line)#删除入院诊断字样
                line_deldl = re.split(r'；|。|\n',line)#根据标点
                line_deld = ''.join(line_deldl)      
                line_out = re.sub(r'\d+、',',',line_deld)
                line_output = re.split(',',line_out)
                line = '\n'.join(line_output)
                line = re.sub(r'\n','',line)
                EMRdef.text_create(r'D:\DeepLearning ER\EHRryzd','.txt' ,emrtxt,line)#导出带有诊疗计划的文件和诊疗计划
            #zljhs.append(emrtxt+':'+line)
#EMRdef.text_save('D:\python\EMR\zljh.txt',zljhs)
