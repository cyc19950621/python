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
    pattern =r'\s*\d+、+\s?(.*)'
    c=re.compile(pattern)
    output=[]  
    for line in f.readlines():
        line1=line.strip('\n')
        line2 = ''.join(line1)
        line2 = line2.strip( )
        line3=c.findall(line2)
        line3=''.join(line3)
        line4 = str(line3)
        out = line4
        if out.find('肺')>-1 or out.find('呼吸')>-1 or out.find('气管')>-1 or out.find('呼吸')>-1 \
        or out.find('筛窦')>-1 or out.find('上额窦')>-1 or out.find('胸腔')>-1 or out.find('鼻')>-1 \
        or out.find('蝶窦')>-1  or out.find('蝶窦')>-1 or out.find('扁桃体')>-1 or out.find('气胸')>-1 \
        or out.find('上颌窦')>-1 or out.find('咽')>-1 or out.find('喉')>-1:
            out= re.sub()
            output.append(out)
            output=EMRdef.delre(output)
            output1='\n'.join(output)
            EMRdef.text_create(r'D:\DeepLearning ER\EHRzhzd2','.txt',emrpath,output1)