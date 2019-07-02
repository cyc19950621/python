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
    for line in f.readlines():
        if line.find('男')>-1:
            out.append('男')
        elif line.find('女')>-1:
            out.append('女')
        if line.find('岁')>-1:
            line = re.sub('岁','',line)
            lien = ''.join(line)
            out.append(line)
        output = ''.join(out)
        EMRdef.text_create(r'D:\DeepLearning ER\EHRzhzd','.txt' ,emrtxt,output)
        