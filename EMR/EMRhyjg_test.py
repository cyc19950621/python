#-*- coding: UTF-8 -*- 

#本文件用于提取目标目录中的所有txt，并提取关键词所在行到指定目录，
# 并提取关键词新建文件，关键词 诊疗过程
import time
import math
import os
import sys
import os, os.path,shutil
import codecs 
import EMRdef
import re

#关键词提取 关键词为诊疗计划
string = '呼吸总阻抗（Z5）'
a=EMRdef.tq_bnum(string)
print (a)