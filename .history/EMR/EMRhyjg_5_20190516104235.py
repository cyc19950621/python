#-*- coding: UTF-8 -*- 
#根据给药方式和剂量剂型分词
import os
import EMRdef
import string
import re
 
emrtxts = EMRdef.txttq(r'D:\DeepLearning ER\EHRzlgc4')#txt目录提取
#pattern = r',|;|\*|`|\[|\]|<|>|\?|"|\{|\}|!|@|#|\$|%|\^|&|=|，|。|：|；|‘|’|\+|\-|【|】| \)|\( |（|）|·|！|、|…'#清除标点
pattern = r',|;|\'|`|\[|\]|<|>|\?|"|\{|\}|!|@|#|\$|%|\^|&|=|＞|，|。|：|＜|；|‘|’|【|】|（|）|·|！|\*|\/|…'#清除标点
hyjg=[]
for emrtxt in emrtxts:
    f = open(emrtxt,'r',errors="ignore")#中文加入errors
    emrpath = os.path.basename(emrtxt)
    emrpath = os.path.splitext(emrpath)[0]#提取目录
    f_end=[]
    for line in f.readlines():
        c = line
        line = re.sub(' ','',line)#删除空格
        line = re.sub('\.','',line)#删除.
        line = re.sub('×','',line)#删除.
        a=EMRdef.tq_bnum(line)
        a_end = "".join(a)#转成str   
        a_end = re.split(pattern,a_end)
        a_end = "".join(a_end)#转成str  
        a_end = re.sub(' ','',a_end)#删除空格   
        a_end = "".join(a_end)#转成str  
        if a_end == '':
            a_end = 1
        else:
            acb = EMRdef.rre( c, a_end , a_end + ':',1)
                #f_end = re.split(pattern, f_start2)
            f_end.append(acb)
            hyjg.append(f_end)#生成化验结果集
            #f_out = "".join(f_end)#转成str                
    #EMRdef.text_create(r'D:\DeepLearning ER\EHRzlgc5','.txt',emrpath,f_out)

