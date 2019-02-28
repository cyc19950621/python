#-*- coding: UTF-8 -*- 

#本文件用于提取目标目录中的所有txt，并提取关键词所在行到指定目录，
# 并提取关键词新建文件，关键词 诊疗过程
import time
import math
import os
import sys
import os, os.path,shutil
import codecs 
import EMRdef
import re

emrtxts = EMRdef.txttq(u'D:\DeepLearning ER\EHRzlgc4')#txt目录提取
a_out = []
pattern = r',|;|\'|`|\[|\]|<|>|\?|"|\{|\}|!|@|#|\$|%|\^|&|=|＞|，|。|：|＜|；|‘|’|【|】|（|）|·|！|\*|\/|…'#清除标点
for emrtxt in emrtxts:
    f = open(emrtxt,'r',errors="ignore")#中文加入errors
    emrtxt = os.path.basename(emrtxt)
    emrtxt_str = re.findall(r'(^.+?)\_',emrtxt)#提取ID
    emrtxt = "".join(emrtxt_str)#转成str
    #txtp=txtp.decode('utf-8')
    for line in f.readlines():
        line = re.sub(' ','',line)#删除空格
        line = re.sub('\.','',line)#删除.
        line = re.sub('×','',line)#删除.
        a=EMRdef.tq_bnum(line)
        a_end = "".join(a)#转成str   
        a_end = re.split(pattern,a_end)
        a_end = "".join(a_end)#转成str  
        a_end = re.sub(' ','',a_end)#删除空格
        a_out.append(a_end)
adult_a = EMRdef.delre(a_out)
EMRdef.text_save('D:\python\EMR\hyxm.txt',adult_a)