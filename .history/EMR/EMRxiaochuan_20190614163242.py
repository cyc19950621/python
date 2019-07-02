#-*- coding: UTF-8 -*- 

import re
import EMRdef
import os, os.path,shutil
emrtxts = EMRdef.txttq(u'D:\DeepLearning ER\EHR1')#txt目录提取
pattern = r',|;|\'|`|\[|\]|<|>|\?|"|\{|\}|!|@|#|\$|\^|&|=|，|。|：|；|‘|’|【|】|·|！|、|…'#根据标点分词
for emrtxt in emrtxts:
    f = open(emrtxt,'r',errors="ignore")#中文加入errors
    emrpath = os.path.basename(emrtxt)
    emrpath = os.path.splitext(emrpath)[0]
    f_out = f.readlines()
    for line in f_out:
        if line.find('都保')>-1 or line.find('舒利迭')>-1 or line.find('布地奈德')>-1 or line.find('沙美特罗卡松粉吸入剂')>-1:
            f_out = ''.join(f_out)
            EMRdef.text_create(u'D:\DeepLearning ER\EHRxiaochuan','.txt',emrpath,f_out)
#EMRdef.text_save(emrtxt,f_end)