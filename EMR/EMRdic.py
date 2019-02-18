#-*- coding: UTF-8 -*- 
#本文件用于提取给药方式
import os
import EMRdef
import re
b = open('D:\python\EMR\drugdic.txt','r',errors="ignore")
brl = b.readlines()
adult=[]
adult_c=[]
for bl in brl:
    bl = re.sub('\n','',bl)
    bl = re.sub('','',bl)
    adult.append(bl)
def deleteDuplicatedElementFromList3(listA):
    #return list(set(listA))
    return sorted(set(listA), key = listA.index)
adult_c=deleteDuplicatedElementFromList3(adult)
EMRdef.text_save(u'D:\python\EMR\ywml.txt',adult_c)