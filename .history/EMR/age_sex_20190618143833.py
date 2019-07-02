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
    out2= []
    for line in f.readlines():
        line = re.sub(' ','' ,line)
        line = re.sub('\n','' ,line)
        line = ''.join(line)
        if line=='男' or line=='男性':
            out.append('M')
        elif line =='女' or  line=='女性':
            out.append('W')
    output = ' '.join(out)
    break
    for line2 in f.readlines(): 
        if line2.find('岁')>-1:
            line2 = re.sub('岁','',line)
            line = ''.join(line)
            out2.append(line)
            break
            '''
            se = int(line)
            if se <=20:
                a = 'Child'
            elif se <=40:
                a = 'Younth'
            elif se <= 60:
                a = 'Mid'
            else:
                a= 'old'
            out.append(a)'''
        output2 = ' '.join(out)
        EMRdef.text_create(r'D:\DeepLearning ER\EHRage','.txt' ,emrtxt,output2)
        