import time
import math
import os
import sys
import os, os.path,shutil
import codecs 
import EMRdef
import re
import pandas as pd
emrtxts = EMRdef.txttq(u'D:\DeepLearning ER\EHRzhzd')#txt目录提取
ryzd=[] 
for emrtxt in emrtxts:
    f = open(emrtxt,'r',errors="ignore")#中文加入errors
    emrpath = os.path.basename(emrtxt)
    emrpath = os.path.splitext(emrpath)[0]#提取目录 
    pattern =r'\s*\d+、+\s?(.*)'
    c=re.compile(pattern)
    output=[] 
    
    for line in f.readlines():
        line1=line.strip('\n')
        line2 = ''.join(line1)
        line2 = line2.strip( )
        line3=c.findall(line2)
        line3=''.join(line3)
        line4 = str(line3)
        out = line4
        if out.find('肺')>-1 or out.find('呼吸')>-1 or out.find('气管')>-1 or out.find('呼吸')>-1 \
        or out.find('筛窦')>-1 or out.find('上额窦')>-1 or out.find('胸腔')>-1 or out.find('鼻')>-1 \
        or out.find('蝶窦')>-1  or out.find('蝶窦')>-1 or out.find('扁桃体')>-1 or out.find('气胸')>-1 \
        or out.find('上颌窦')>-1 or out.find('咽')>-1 or out.find('喉')>-1:
            out= re.sub(r'右侧|两侧|双侧|左侧|急性发作|急性|右|左|双','',out)
            out = re.sub(r'肺肺','肺',out)
            output.append(out)
            output=EMRdef.delre(output)
            #output1='\n'.join(output)
            #EMRdef.text_create(r'D:\DeepLearning ER\EHRzhzd2','.txt',emrpath,output1)
    ryzd.append(output)

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

def dealResult(rules):#对规则处理
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

if __name__ == '__main__':    
    supportRate = 0.003
    confidenceRate = 0.2
    itemsets = dict(oaf.frequent_itemsets(ryzd, supportRate))
    rules = oaf.association_rules(itemsets, confidenceRate)
    rules = list(rules)
    regularNum = len(rules)
    printRules = dealRules(rules)
    result = list(oaf.rules_stats(rules, itemsets, len(ryzd)))   #下面这个函数改变了rules，把rules用完了！
    printResult = dealResult(result)
    
#################################################
# 下面将结果保存成excel格式的文件    
    dfToSave = ResultDFToSave(result)
    saveRegularName = str(supportRate)+'支持度_'+str(confidenceRate)+'置信度_产生了'+str(regularNum)+'条规则'+'.xlsx'
    dfToSave.to_excel(r'C:\Users\Administrator\Desktop\2.xlsx')

#######################################################
# 下面是根据不同置信度和关联度得到关联规则数目
    listTable = []
    supportRate = 0.001
    confidenceRate = 0.1
    for i in range(9):
        support = supportRate*(i+1)
        listS = []
        for j in range(9):
            confidence = confidenceRate*(j+1)
            itemsets = dict(oaf.frequent_itemsets(ryzd, support))
            rules = list(oaf.association_rules(itemsets, confidence))
            listS.append(len(rules))
        listTable.append(listS)    
    dfList = pd.DataFrame(listTable,index = [supportRate*(i+1) for i in range(9)],columns=[confidenceRate*(i+1) for i in range(9)])
    dfList.to_excel(r'C:\Users\Administrator\Desktop\outlunwen.xlsx')
