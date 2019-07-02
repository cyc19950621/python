import time
import math
import os
import sys
import os, os.path,shutil
import codecs 
import EMRdef
import re
import pandas as pd
emrtxts = EMRdef.txttq(u'D:\DeepLearning ER\EHRzhzd2')#txt目录提取
dis = open(r'C:\Users\Administrator\Desktop\JBML.txt',errors='ignore')
ds=dis.readlines()
ds_cs = []
for line in ds:
    line = re.sub('\n','',line)
    ds_cs.append(line)
for emrtxt in emrtxts:
    out = []
    f = open(emrtxt,'r',errors="ignore")#中文加入errors
    emrpath = os.path.basename(emrtxt)
    emrpath = os.path.splitext(emrpath)[0]#提取目录 
    lines = f.readlines()
    for line in lines:
        line = re.sub('\n','',line)
        line = re.sub(r'急性|慢性','',line)
        for ds_c in ds_cs:
            ds_c = re.sub(r'急性|慢性','',ds_c)
            ds_c = re.sub(r'阻塞性肺疾病','慢性阻塞性肺疾病',ds_c)
            if set(line) == set(ds_c):
                out.append(ds_c)
            elif EMRdef.SBS(line,ds_c)>0.6  and EMRdef.SBS(line,ds_c) <1:
                out.append(ds_c)
        out=EMRdef.delre(out)
        output = '\n'.join(out)
    EMRdef.text_create(r'D:\DeepLearning ER\EHRzhzd3','.txt',emrpath,output)
    


