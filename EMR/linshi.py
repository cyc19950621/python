#-*- coding: UTF-8 -*- 
#根据给药方式和剂量剂型分词
import os
import EMRdef
import string
import re

pattern = r',|;|\*|`|\[|\]|<|>|\?|"|\{|\}|!|@|#|\$|%|\^|&|=|，|。|：|；|‘|’|\+|\-|【|】| \)|\( |（|）|·|！|、|…'#清除标点
c = open(r'C:\Users\Administrator\Desktop\quanbu.txt','r',errors="ignore")#给药剂量加剂型加给药方式词典
b = open(r'C:\Users\Administrator\Desktop\tc.txt','r',errors="ignore")#给药剂量词典
crl = c.readlines()
brl = b.readlines()
test_out = []
for cl in crl:
    cl = re.sub('\n','',cl)
    for bl in brl:
        bl = re.sub('\n','',bl)
        if cl ==bl:
            test_out.append(cl)
adult_a = EMRdef.delre(test_out)
EMRdef.text_save(r'C:\Users\Administrator\Desktop\output.txt',adult_a)