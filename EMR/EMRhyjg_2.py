#根据词典提取
#-*- coding: UTF-8 -*- 
#本文件用于根据指标参数提取所有指标
import os
import EMRdef
import re

b = open('D:\python\EMR\hyzb.txt','r',errors="ignore")
emrtxts = EMRdef.txttq(u'D:\DeepLearning ER\EHRzlgc2')#txt目录提取
brl = b.readlines()
test_out = []
for emrtxt in emrtxts:
    f = open(emrtxt,'r',errors="ignore")#中文加入errors
    emrpath = os.path.basename(emrtxt)
    emrpath = os.path.splitext(emrpath)[0]#提取目录
    adult = []
    adult_c = []
    for al in f.readlines():
        al = re.sub('\n','',al)
        for bl in brl:
            bl = re.sub('\n','',bl)
            if bl == '':
                adult = []
            else:
                if al.find(bl) > -1:
                    adult.append(al+'\n')#进行给药方式关键字判定
                for i in adult :
                    if not i in adult_c:
                        adult_c.append(i)
                        adult_cstr = "".join(adult_c)#转成str
                        EMRdef.text_create(r'D:\DeepLearning ER\EHRzlgc3','.txt',emrpath,adult_cstr)                    
#EMRdef.text_save(u'D:\python\EMR\967ywml.txt',test_out)
