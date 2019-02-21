#-*- coding: UTF-8 -*- 
#根据给药方式和剂量剂型分词
import os
import EMRdef
import string
import re
 
emrtxts = EMRdef.txttq(r'D:\DeepLearning ER\EHR5')#txt目录提取
pattern = r',|;|\*|`|\[|\]|<|>|\?|"|\{|\}|!|@|#|\$|%|\^|&|=|，|。|：|；|‘|’|\+|\-|【|】| \)|\( |（|）|·|！|、|…'#清除标点
b = open('D:\python\EMR\gy.txt','r',errors="ignore")#给药剂量加剂型加给药方式词典
brl = b.readlines()
c = open('D:\python\EMR\gyfs.txt','r',errors="ignore")#给药剂量词典
crl = c.readlines()
test_out = []
for emrtxt in emrtxts:
    f = open(emrtxt,'r',errors="ignore")#中文加入errors
    emrpath = os.path.basename(emrtxt)
    emrpath = os.path.splitext(emrpath)[0]#提取目录
    f_start = "".join(f.readlines())#转成str
    f_start = re.sub(r'\n', ' ', f_start)#删除尾部换行符
    f_start = re.sub(r' ', '\n', f_start)
    f_start = re.sub(r'\)\n','',f_start)#删除尾部括号
    f_start = re.sub(r'\)',')*',f_start)
    for cl in crl:
        cl = re.sub('\n','',cl)
        if f_start.find(cl) > -1: #先进行剂量判断然后根据给药特点分词
                f_start2 =f_start
                for bl in brl:
                        bl = re.sub('\n','',bl)
                        f_start2 = re.sub(bl,bl + '*', f_start2)
                        f_end = re.split(pattern, f_start2)
                        f_end = " ".join(f_end)#转成str                   
                        EMRdef.text_create(r'D:\DeepLearning ER\EHR6','.txt',emrpath,f_end)