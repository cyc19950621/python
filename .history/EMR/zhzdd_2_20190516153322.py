import time
import math
import os
import sys
import os, os.path,shutil
import codecs 
import EMRdef
import re
emrtxts = EMRdef.txttq(u'D:\DeepLearning ER\EHRzhzd')#txt目录提取
for emrtxt in emrtxts:
    f = open(emrtxt,'r',errors="ignore")#中文加入errors
    emrpath = os.path.basename(emrtxt)
    emrpath = os.path.splitext(emrpath)[0]#提取目录 
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
        out=EMRdef.delre(out)
        line = ''.join(out)
        EMRdef.text_create(r'D:\DeepLearning ER\EHRzhzd2','.txt',emrpath,line)