#-*- coding: UTF-8 -*- 
#本文件用于提取给药方式
import os
import EMRdef
import re
b = open('D:\python\EMR\ywml.txt','r',errors="ignore")
emrtxts = EMRdef.txttq(u'D:\DeepLearning ER\EHR6')#txt目录提取
pattern = r',|;|\*|`|\[|\]|<|>|\?|"|\{|\}|!|@|#|\$|%|\^|&|=|，|。|：|；|‘|’|【|】|（|）|·|！|、|…'#清除标点
brla = b.readlines()
brl = [i for i in brla if i != '']
for emrtxt in emrtxts:
    f = open(emrtxt,'r',errors="ignore")#中文加入errors
    emrpath = os.path.basename(emrtxt)
    emrpath = os.path.splitext(emrpath)[0]#提取目录
    f_start = "".join(f.readlines())#转成str
    f_start = re.sub(r'\n', ' ', f_start)#删除尾部换行符
    f_start = re.sub(r' ', '\n', f_start)
    f_start = re.sub(r'\)\n','',f_start)#删除尾部括号
    f_start = re.sub(r'\)',')*',f_start)
    for bl in brl:
        bl = re.sub('\n','',bl)
        f_start = re.sub(bl,bl + '*', f_start)
        f_end = re.split(pattern, f_start)
        f_end = "  ".join(f_end)#转成str                   
        EMRdef.text_create(r'D:\DeepLearning ER\EHR7','.txt',emrpath,f_end)