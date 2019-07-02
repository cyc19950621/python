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
        for ds_c in ds_cs:
            if set(line) == set(ds_c):
                out.append(ds_c)
            elif EMRdef.SBSSBS(line,dic)>0.8  and SBS(line,dic) <1:


