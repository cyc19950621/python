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
emrtxts = EMRdef.txttq(u'D:\DeepLearning ER\EHR-all')#txt目录提取
pattern2 = r'。|：|，|；'#根据标点分词
for emrtxt in emrtxts:
    f = open(emrtxt,'r',errors="ignore")#中文加入errors
    emrtxt = os.path.basename(emrtxt)
    emrtxt_str = re.findall(r'(^.+?)\_',emrtxt)#提取ID
    emrtxt = "".join(emrtxt_str)#转成str 
    out=[]  
    for line in f.readlines():
        if '1、'  in line:
            str11 = str(line.split('、'))
            out.append(str11)
        if '2、'  in line:
            str12 = str(line.split('、'))
            out.append(str12)
        if '3、'  in line:
            str13 = str(line.split('、'))
            out.append(str13)
        if '4、' in line:
            str14 = str(line.split('、'))
            out.append(str14)
        if '5、' in line:
            str15 = str(line.split('、'))
            out.append(str15)
        if '6、' in line:
            str16 = str(line.split('、'))
            out.append(str16)
        if '7、' in line:
            str17 = str(line.split('、'))
            out.append(str17)
        if '8、' in line:
            str18 = str(line.split('、'))
            out.append(str18)
        if '9、' in line:
            str19 = str(line.split('、'))
            out.append(str19)
        if '10、' in line:
            str20 = str(line.split('、'))
            out.append(str20)
    print(out)