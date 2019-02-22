#根据词典提取
#-*- coding: UTF-8 -*- 
#本文件用于根据指标参数提取所有指标
import os
import EMRdef
import re
#根据句号分词

'''emrtxt2s = EMRdef.txttq(u'D:\DeepLearning ER\EHRzlgc2')#txt目录提取
pattern2 = r'、|；|：|、|:|，'#根据标点分词
for emrtxt2 in emrtxt2s:
    f2 = open(emrtxt2,'r',errors="ignore")#中文加入errors
    f2_end = re.split(pattern2, f2.read())
    f2_out = "\n".join(f2_end)#转成str
    emrpath2 = os.path.basename(emrtxt2)
    emrpath2 = os.path.splitext(emrpath2)[0]
    EMRdef.text_create(u'D:\DeepLearning ER\EHRzlgc3','.txt',emrpath2,f2_out)'''
#EMRdef.text_save(emrtxt,f_end)'''


'''----------------------------------------------------------------------------------------------------------------------------------------------'''
emrtxts = EMRdef.txttq(u'D:\DeepLearning ER\EHRzlgc3')#txt目录提取
a_out = []
pattern = r',|;|\'|`|\[|\]|<|>|\?|"|\{|\}|!|@|#|\$|%|\^|&|=|，|。|：|；|‘|’|【|】|（|）|·|！|\*|\/|…'#清除标点
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

 

