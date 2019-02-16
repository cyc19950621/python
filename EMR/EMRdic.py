#-*- coding: UTF-8 -*- 
#通过两次清洗，清除
import os
import EMRdef
import string
import re
f = open('D:\python\EMR\drug.txt','r',errors="ignore")
drugdic = []
for line in f.readlines():
    a = re.sub(r'[A-Za-z0-9]|/d+' ,'',line)#删除字母和标点
    a = a.replace(' ',' \n')
    a = re.sub('（.*?）', '', a)
    a = re.sub(r' ' ,'',a)#删除空格
    drugdic.append(a)
dicdeln=[]
for deln in drugdic:
    deln = re.sub(r',|（）|画\n|一\n|二\n|三\n|四\n|五\n|六\n|七\n|八\n|九\n|十\n|十一\n|十二\n|十三\n|十四\n|十五\n|十六\n|十七\n|十八\n|十九\n|二十\n|二十一\n|-' ,'',deln)#删除
    deln = re.sub(r' ' ,'',deln)#删除空格
    dicdeln.append(deln)
#print(dicdeln)
dicdeln = [x.strip() for x in dicdeln if x.strip()!='']#清除空白换行符

EMRdef.dic_save('D:\python\EMR\drugdic.txt',dicdeln)#输出生成文件1
g = open('D:\python\EMR\drugdic.txt','r',errors="ignore")#二次清洗
delnts = g.readlines()
tcs=[]
for tc in delnts:
    tc = re.sub(r',|,|;|\'|`|\[|\]|<|>|\?|"|\{|\}|!|@|#|\$|%|\^|&|=|，|。|；|‘|’|【|】|·|！|…|（）|画\n|一\n|二\n|三\n|四\n|五\n|六\n|七\n|八\n|九\n|十\n|十一\n|十二\n|十三\n|十四\n|十五\n|十六\n|十七\n|十八\n|十九\n|二十\n|二十一|-' ,'',tc)#删除
    tc = re.sub(r' ' ,'',tc)#删除空格
    tc=tc.strip('（')
    tc=tc.strip('）')
    tcs.append(tc)
tcs = [yx.strip() for yx in tcs if yx.strip()!='']#清除空白换行符
EMRdef.dic_save('D:\python\EMR\drugdicdeln.txt',tcs)