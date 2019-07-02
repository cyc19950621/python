#-*- coding: UTF-8 -*- 

import re
import EMRdef
import os, os.path,shutil
emrtxts = EMRdef.txttq(u'D:\DeepLearning ER\EHR1')#txt目录提取
pattern = r',|;|\'|`|\[|\]|<|>|\?|"|\{|\}|!|@|#|\$|\^|&|=|，|。|：|；|‘|’|【|】|·|！|、|…'#根据标点分词
for emrtxt in emrtxts:
    f = open(emrtxt,'r',errors="ignore")#中文加入errors
    
    f_end = re.split(pattern, f.read())
    f_out = "\n".join(f_end)#转成str
    emrpath = os.path.basename(emrtxt)
    emrpath = os.path.splitext(emrpath)[0]
    EMRdef.text_create(u'D:\DeepLearning ER\EHR2','.txt',emrpath,f_out)
#EMRdef.text_save(emrtxt,f_end)