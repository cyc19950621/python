import time
import math
import os
import sys
import os, os.path,shutil
import codecs 
import EMRdef
import re
import pandas as pd
emrtxts = EMRdef.txttq(u'D:\DeepLearning ER\EHRzhzd5')#txt目录提取
emrtxt2s = EMRdef.txttq(u'D:\DeepLearning ER\EHRsex')
ryzd = []
for emrtxt in emrtxts:
    f = open(emrtxt,'r',errors="ignore")#中文加入errors
    emrpath = os.path.basename(emrtxt)
    emrpath = os.path.splitext(emrpath)[0]#提取目录 
    lines=f.readlines()
    lines = ''.join(lines)
    lines = re.sub(' ','',lines)
    lines
    for emrtxt2 in emrtxt2s:
        f2 = open(emrtxt2,'r',errors="ignore")#中文加入errors
        emrpath2 = os.path.basename(emrtxt2)
        emrpath2 = os.path.splitext(emrpath2)[0]#提取目录 
        lines2 = f2.readlines()
        lines2 = ''.join(lines2)
        if emrpath == emrpath2:
            lines.append(lines2)
    ryzd.append(lines)        