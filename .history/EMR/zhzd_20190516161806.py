#-*- coding: UTF-8 -*- 

#
#提取最后诊断之后的内容 并进入下一步处理
import time
import math
import os
import sys
import os, os.path,shutil
import codecs 
import EMRdef
import re
emrtxts = EMRdef.txttq(u'D:\DeepLearning ER\EHR-all')#txt目录提取
for emrtxt in emrtxts:
    f = open(emrtxt,'r',errors="ignore")#中文加入errors
    emrtxt = os.path.basename(emrtxt)
    emrtxt_str = re.findall(r'(^.+?)\_',emrtxt)#提取ID
    emrtxt = "".join(emrtxt_str)#转成str
    pattern = r',|.|，|。|;|；'#清除标点
    #txtp=txtp.decode('utf-8')
    temp=f.readlines()
    tem_del = []
    for line in temp:
        tem_del.append(line)
        if line.find (u'最后诊断'|'') >-1:
            break
    temp = list(set(temp)-set(tem_del))
    line = '\n'.join(temp)
    EMRdef.text_create(r'D:\DeepLearning ER\EHRzhzd','.txt' ,emrtxt,line)