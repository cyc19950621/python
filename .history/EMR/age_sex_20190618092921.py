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
        if line=='男':
            out.append(line)
        elif line=='女':
            out.append(line)
        if line.find('岁')>-1:
            line = re.sub('岁','',line)
            lien = ''.join(line)
            out.append(line)
            break
    output = ' '.join(out)
    EMRdef.text_create(r'D:\DeepLearning ER\EHRbase','.txt' ,emrtxt,output)
        