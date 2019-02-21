#-*- coding: UTF-8 -*- 
import os
import EMRdef
import string
import re
 '''本文件用于数据清洗，生成文件基于所用药物分划段落'''
 
emrtxts = EMRdef.txttq(r'D:\DeepLearning ER\EHR3')#txt目录提取
pattern = r',|;|\'|`|\[|\]|<|>|\?|"|\{|\}|!|@|#|\$|%|\^|&|=|，|。|：|；|‘|’|【|】|（|）|\( |\) |·|！|、|…'#清除标点
test_out = []
for emrtxt in emrtxts:
    f = open(emrtxt,'r',errors="ignore")#中文加入errors
    emrpath = os.path.basename(emrtxt)
    emrpath = os.path.splitext(emrpath)[0]#提取目录
    f_start = "".join(f.readlines())#转成str
    f_start = re.sub(r'\n', ' ', f_start)
    f_start = re.sub(r'\'', ' ', f_start)
    f_start = re.sub(r' ', '\n', f_start)
    f_end = re.split(pattern, f_start)
    f_end = "\n".join(f_end)#转成str                   
    EMRdef.text_create(r'D:\DeepLearning ER\EHR4','.txt',emrpath,f_end)