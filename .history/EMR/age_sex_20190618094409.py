# -*- coding:utf-8 -*-
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
    out = []
    for line in f.readlines():
        if line.find(r'男')>-1:
            out.append('M')
        elif line.find(r'女')>-1:
            out.append('W')
        if line.find('岁')>-1:
            line = re.sub('岁','',line)
            line = ''.join(line)
            se = int(line)
            if se <=20:
                a = 'Child'
            elif se <=40:
                a = 'Younth'
            elif se <= 60:
                a = 'Mid'
            else:
                a= 'old'
            out.append(a)
    output = ' '.join(out)
    EMRdef.text_create(r'D:\DeepLearning ER\EHRbase','.txt' ,emrtxt,output)
        