#-*- coding: UTF-8 -*- 

import re
import EMRdef
pattern = r',|;|\'|`|\[|\]|<|>|\?|"|\{|\}|!|@|#|\$|%|\^|&|=|，|。|；|‘|’|【|】|·|！|…'#清除标点
f = open('D:\python\EMR\zljh.txt','r',errors="ignore")
f_end = re.split(pattern, f.read())
EMRdef.text_save('D:\python\EMR\zljhfc.txt',f_end)