#-*- coding: UTF-8 -*- 
import os
import glob
import sys

#以下函数用于提取rxr文件名
def txttq(dirname):
   filter=[".txt"] #设置过滤后的文件类型 当然可以设置多个类型
   result = []#所有的文件
   for maindir, subdir, file_name_list in os.walk(dirname):# print("1:",maindir) #当前主目录#print("2:",subdir) #当前主目录下的所有目录# print("3:",file_name_list)  #当前主目录下的所有文件
      for filename in file_name_list:
         apath = os.path.join(maindir, filename)#合并成一个完整路径
         ext = os.path.splitext(apath)[1]  # 获取文件后缀 [0]获取的是除了文件名以外的内容
         if ext in filter:
            result.append(apath)
   return result
#print(txttq("D:\DeepLearning ER"))

#以下函数用于导出列表到文件
def text_save(filename, data):#filename为写入CSV文件的路径，data为要写入数据列表.
    file = open(filename,'a')
    for i in range(len(data)):
        s = str(data[i]).replace('[','').replace(']','')#去除[],这两行按数据不同，可以选择
        s = s+'\n'   #去除单引号，逗号，每行末尾追加换行符
        file.write(s)
    file.close()

#以下函数用于列表导出
def dic_save(filename, data):#filename为写入CSV文件的路径，data为要写入数据列表.
    file = open(filename,'a')
    for i in range(len(data)):
        s = str(data[i]).replace('[','').replace(']','')#去除[],这两行按数据不同，可以选择
        s = s+'\n'   #去除单引号，逗号，每行末尾追加换行符
        file.write(s)
    file.close()

    #以下函数用于数据清洗
from string import punctuation 
import re
import jieba
def dicclean(x):#cut words and delete punctuation
   x=re.sub(r'[A-Za-z0-9]|/d+','',x)#delet numbers and letters


# 创建一个txt文件，文件名为mytxtfile,并向文件写入msg
def text_create(path,form,name, msg):#路径 格式 名称 内容（str）
    #desktop_path = "D:\DeepLearning ER\EHRC\ "  # 新创建的txt文件的存放路径
    full_path = path +'\/' + name + form # 也可以创建一个.doc的word文档
    file = open(full_path, 'w')
    file.write(msg) 


#提取数字前内容
def tq_bnum(string):
   p= re.compile(r'(.*?)[0-9]',re.S)
   return re.findall(p, string)

#删除列表中的重复
def delre(listA):
    #return list(set(listA))
    return sorted(set(listA), key = listA.index)