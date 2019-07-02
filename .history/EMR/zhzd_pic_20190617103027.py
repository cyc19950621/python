import time
import math
import os
import sys
import os, os.path,shutil
import codecs 
import EMRdef
import re
import pandas as pd
emrtxts = EMRdef.txttq(u'D:\DeepLearning ER\EHRzhzd4')#txt目录提取
for emrtxt in emrtxts:
    f = open(emrtxt,'r',errors="ignore")#中文加入errors
    emrpath = os.path.basename(emrtxt)
    emrpath = os.path.splitext(emrpath)[0]#提取目录 
    lines=f.readlines()
    if len(lines) > 1:
        lines = '\n'.join(lines)
        output = re.sub('\n','',lines)
        output = ''.join(lines)
        EMRdef.text_create(r'D:\DeepLearning ER\EHRzhzd5','.txt',emrpath,output)