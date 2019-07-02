import time
import math
import os
import sys
import os, os.path,shutil
import codecs 
import EMRdef
import re
emrtxts = EMRdef.txttq(u'D:\DeepLearning ER\EHRryzd')#txt目录提取
emrtxt2s = EMRdef.txttq(r'D:\DeepLearning ER\EHRzlgc4')#txt目录提取
for emrtxt in emrtxts:
    emrpath = os.path.basename(emrtxt)
    emrpath = os.path.splitext(emrpath)[0]
    for emrtxt2 in emrtxt2s:
        emrpath2 = os.path.basename(emrtxt2)
        emrpath2 = os.path.splitext(emrpath2)[0]
        if emrpath == emrpath2:
            f = open(emrtxt,'r',errors="ignore")#中文加入errors
            f2 = open(emrtxt2,'r',errors="ignore")#中文加入errors
            a=f.readlines()
            b=f2.readlines()
            c=a+b
            print(c)            