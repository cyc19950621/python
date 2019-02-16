#-*- coding: UTF-8 -*- 
import os
import EMRdef
import re

a = open('D:\python\EMR\zljhfc.txt','r',errors="ignore")
b = open('D:\python\EMR\drugdicdeln.txt','r',errors="ignore")
arl = a.readlines()
brl = b.readlines()
adult=[]
for bl in brl:
    bl=re.sub('\n','',bl)
    for al in arl:
        al = re.sub('\n','',al)
        if al.find(bl) > -1:
            adult.append(al)
adult2= list(set(adult))
EMRdef.text_save(r'D:\python\EMR\ult.txt',adult2)

