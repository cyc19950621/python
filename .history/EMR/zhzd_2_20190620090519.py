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
ryzd=[] 
for emrtxt in emrtxts:
    f = open(emrtxt,'r',errors="ignore")#中文加入errors
    emrpath = os.path.basename(emrtxt)
    emrpath = os.path.splitext(emrpath)[0]#提取目录 
    pattern =r'\s*\d+、+\s?(.*)'
    c=re.compile(pattern)
    output=[]
    line_re = []
    for line in f.readlines():
        line1=line.strip('\n')
        line2 = ''.join(line1)
        line2 = line2.strip( )
        line3=c.findall(line2)
        line3=''.join(line3)
        line4 = str(line3)
        line = line4
        line=re.sub('\n','',line)
        line=re.sub(' ','',line)
        line = re.sub(r'\?|？', '',line)
        line = re.sub(r'\,|\.|；','',line)
        out = line
        out= re.sub(r'右侧|两侧|双侧|左侧|右|左|双','',out)
        out = re.sub(r'肺肺','肺',out)
        out = re.sub('（.*?）', '', out)
        out = re.sub(r'很高危|极高危', '', out)
        line = out
        line_re.append(line)
        while '' in line_re:
            line_re.remove('')
        output=EMRdef.delre(line_re)
        output1='\n'.join(output)
        EMRdef.text_create(r'D:\DeepLearning ER\EHRzhzd2','.txt',emrpath,output1)
 