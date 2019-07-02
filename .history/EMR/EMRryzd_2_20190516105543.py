#-*- coding: UTF-8 -*- 

#本文件用于数据清洗
import time
import math
import os
import sys
import os, os.path,shutil
import codecs 
import EMRdef
import re
import pandas as pd
emrtxts = EMRdef.txttq(u'D:\DeepLearning ER\EHRryzd')#txt目录提取
hxjb = open(r'D:\python\EMR\hxjbml.txt',errors="ignore")#呼吸疾病目录
hxjbdic = hxjb.readlines()#读行
ryzd=[]
for emrtxt in emrtxts:
    f = open(emrtxt,'r',errors="ignore")#中文加入errors
    emrpath = os.path.basename(emrtxt)
    emrpath = os.path.splitext(emrpath)[0]
    line_out = []
    for line in f.readlines():
            line = re.sub('\n','',line)
            line = re.sub(r'(.+?)肺炎','肺炎',line)#替换所有的肺炎
            for hxjbc in hxjbdic:#检索每个词
                hxjbc = re.sub('\n','',hxjbc)
                if line.find(hxjbc) >-1:
                    line_out.append(line)
            line_output = EMRdef.delre(line_out)
            ryzd.append(line_out)
            #line = '\n'.join(line_output)
            #EMRdef.text_create(r'D:\DeepLearning ER\EHRryzd2','.txt' ,emrpath,line)

#导入关联规则
import orangecontrib.associate.fpgrowth as oaf


def dealRules(rules):
    returnRules = []
    for i in rules:
        temStr = '';
        for j in i[0]:   #处理第一个frozenset
            temStr = temStr+j+'&'
        temStr = temStr[:-1]
        temStr = temStr + ' ==> '
        for j in i[1]:
            temStr = temStr+j+'&'
        temStr = temStr[:-1]
        temStr = temStr + ';' +'\t'+str(i[2])+ ';' +'\t'+str(i[3])
#        print(temStr)
        returnRules.append(temStr)
    return returnRules

def dealResult(rules):
    returnRules = []
    for i in rules:
        temStr = '';
        for j in i[0]:   #处理第一个frozenset
            temStr = temStr+j+'&'
        temStr = temStr[:-1]
        temStr = temStr + ' ==> '
        for j in i[1]:
            temStr = temStr+j+'&'
        temStr = temStr[:-1]
        temStr = temStr + ';' +'\t'+str(i[2])+ ';' +'\t'+str(i[3])+ ';' +'\t'+str(i[4])+ ';' +'\t'+str(i[5])+ ';' +'\t'+str(i[6])+ ';' +'\t'+str(i[7])
#        print(temStr)
        returnRules.append(temStr)
    return returnRules

def ResultDFToSave(rules):   #根据Qrange3关联分析生成的规则得到并返回对于的DataFrame数据结构的函数
    returnRules = []
    for i in rules:
        temList = []
        temStr = '';
        for j in i[0]:   #处理第一个frozenset
            temStr = temStr + str(j) + '&'
        temStr = temStr[:-1]
        temStr = temStr + ' ==> '
        for j in i[1]:
            temStr = temStr + str(j) + '&'
        temStr = temStr[:-1]
        temList.append(temStr); temList.append(i[2]); temList.append(i[3]); temList.append(i[4])
        temList.append(i[5]); temList.append(i[6]); temList.append(i[7])
        returnRules.append(temList)
    return pd.DataFrame(returnRules,columns=('规则','项集出现数目','置信度','覆盖度','力度','提升度','利用度'))

often=dict(oaf.frequent_itemsets(ryzd, .02))
rules = oaf.association_rules(often, .5)   #这里设置置信度
rules = list(rules)
regularNum = len(rules)
printRules = dealRules(rules)
result = list(oaf.rules_stats(rules,often, len(ryzd)))   #下面这个函数改变了rules，把rules用完了！
printResult = dealResult(result)

dfToSave = ResultDFToSave(result)
saveRegularName = str(0.02)+'支持度_'+str(0.05)+'置信度_产生了'+str(regularNum)+'条规则'+'.xlsx'
dfToSave.to_excel(saveRegularName)