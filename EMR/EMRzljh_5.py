#-*- coding: UTF-8 -*- 
#本文件用于提取给药方式
import os
import EMRdef
import re
b = open('D:\python\EMR\gyfs.txt','r',errors="ignore")
emrtxts = EMRdef.txttq(u'D:\DeepLearning ER\EHR4')#txt目录提取
pattern = r',|;|\'|`|\[|\]|<|>|\?|"|\{|\}|!|@|#|\$|%|\^|&|=|，|。|：|；|‘|’|【|】|（|）|·|！|、|…'#清除标点
brl = b.readlines()
for emrtxt in emrtxts:
    f = open(emrtxt,'r',errors="ignore")#中文加入errors
    emrpath = os.path.basename(emrtxt)
    emrpath = os.path.splitext(emrpath)[0]#提取目录
    test_out = []
    adult=[]
    adult_c=[]
    for al in f.readlines():
        al = re.sub('\n','',al)
        for bl in brl:
            bl = re.sub('\n','',bl)
            if al.find(bl) > -1:
                adult.append(al+'\n')#进行给药方式关键字判定
            for i in adult :
                if not i in adult_c:
                    adult_c.append(i)
                    adult_cstr = "".join(adult_c)#转成str
                    EMRdef.text_create(r'D:\DeepLearning ER\EHR5','.txt',emrpath,adult_cstr)


