import time
import math
import os
import sys
import os, os.path,shutil
import codecs 
import EMRdef
import re
import pandas as pd
emrtxts = EMRdef.txttq(u'D:\DeepLearning ER\EHRzhzd')#txt目录提取
dis = open(r'C:\Users\Administrator\Desktop\ICD-10.txt',errors='ignore')
ds=dis.readlines()
ds_c = []
for line in ds:
    line = re.sub('\n','',line)
    ds_cs.append(line)
ryzd=[] 
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
        out= re.sub(r'右侧|两侧|双侧|左侧|右|左|双','',out)
        out = re.sub(r'肺肺','肺',out)
        out = re.sub('（.*?）', '', out)
        for ds in ds_cs:
            if EMRdef.SBS(out,ds) > 0.8:

                output.append(out)
                output=EMRdef.delre(output)
            output1='\n'.join(output)
            EMRdef.text_create(r'D:\DeepLearning ER\EHRzhzd2','.txt',emrpath,output1)

