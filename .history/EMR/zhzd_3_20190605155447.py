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


