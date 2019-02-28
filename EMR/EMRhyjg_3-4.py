#根据词典提取
#-*- coding: UTF-8 -*- 
#本文件用于根据指标参数提取所有指标
import os
import EMRdef
import re
#根据句号分词

emrtxt2s = EMRdef.txttq(u'D:\DeepLearning ER\EHRzlgc2')#txt目录提取
pattern2 = r'、|；|：|、|:|，'#根据标点分词
for emrtxt2 in emrtxt2s:
    f2 = open(emrtxt2,'r',errors="ignore")#中文加入errors
    f2_end = re.split(pattern2, f2.read())
    f2_out = "\n".join(f2_end)#转成str
    emrpath2 = os.path.basename(emrtxt2)
    emrpath2 = os.path.splitext(emrpath2)[0]
    EMRdef.text_create(u'D:\DeepLearning ER\EHRzlgc3','.txt',emrpath2,f2_out)
#EMRdef.text_save(emrtxt,f_end)

'''----------------------------------------------------------------------------------------------------------------------------------------------'''

#根据化验指标提取段落
b = open('D:\python\EMR\hyzb.txt','r',errors="ignore")
emrtxts = EMRdef.txttq(u'D:\DeepLearning ER\EHRzlgc3')#txt目录提取
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
                    EMRdef.text_create(r'D:\DeepLearning ER\EHRzlgc4','.txt',emrpath,adult_cstr)
