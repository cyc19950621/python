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
                        if line.find(u'医保首程传输') > -1:
                    break
        if line.find (u'诊断依据：',0,6) >-1:
                line = re.sub(r'h|H', '小时', line)#小时替换成中文      
                line = re.sub(r'诊断依据：', '', line)#删除入院诊断字样
                line_deldl = re.split(r'。',line)#根据标点分行
                line_deld = '\n'.join(line_deldl)      #转成str格式
                line_out = re.sub(r'\d+、|\d+）、|\d+\)、','',line_deld) #删除序号
                line_output = re.split('\n',line_out)
                line = '\n'.join(line_output)

                EMRdef.text_create(r'D:\DeepLearning ER\EHRzdyj','.txt' ,emrtxt,line)#导出带有诊疗计划的文件和诊疗计划
            #zljhs.append(emrtxt+':'+line)
#EMRdef.text_save('D:\python\EMR\zljh.txt',zljhs)
