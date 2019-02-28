#-*- coding: UTF-8 -*- 
#本文件用于提取给药方式
import os
import EMRdef
import re
pattern = r',|;|\'|`|\[|\]|<|>|\?|"|\{|\}|!|@|#|\$|\^|&|=|，|。|：|；|‘|’|【|】|·|！|、|…'#根据标点分词
b = open('D:\python\EMR\967ywml.txt','r',errors="ignore")
brl = b.readlines()
adult = []
adult_c = []
for bl in brl:
    bl = re.sub('\n','',bl)
    bl = re.sub('','',bl)
    adult.append(bl)
adult_c = EMRdef.delre(adult)
EMRdef.text_save(u'D:\python\EMR\967yw.txt',adult_c)