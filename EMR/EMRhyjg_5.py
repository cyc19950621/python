#-*- coding: UTF-8 -*- 
#根据给药方式和剂量剂型分词
import os
import EMRdef
import string
import re
 
emrtxts = EMRdef.txttq(r'D:\DeepLearning ER\EHRzlgc4')#txt目录提取
#pattern = r',|;|\*|`|\[|\]|<|>|\?|"|\{|\}|!|@|#|\$|%|\^|&|=|，|。|：|；|‘|’|\+|\-|【|】| \)|\( |（|）|·|！|、|…'#清除标点
c = open('D:\python\EMR\hyxm.txt','r',errors="ignore")#给药剂量词典
crl = c.readlines()
test_out = []
for emrtxt in emrtxts:
    f = open(emrtxt,'r',errors="ignore")#中文加入errors
    emrpath = os.path.basename(emrtxt)
    emrpath = os.path.splitext(emrpath)[0]#提取目录
    f_end=[]
    for f_start in f.readlines():
       
        for cl in crl:
            cl = re.sub('\n','',cl)
            if f_start.find(cl) > -1: #先进行剂量判断然后根据给药特点分词
                f_start2=EMRdef.rre(f_start,cl,cl+'*',1)
                f_end.append(f_start2)
                f_end = EMRdef.delre(f_end)
                #f_end = re.split(pattern, f_start2)
    f_end = "".join(f_end)#转成str                
    EMRdef.text_create(r'D:\DeepLearning ER\EHRzlgc5','.txt',emrpath,f_end)