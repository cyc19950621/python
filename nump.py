import jieba.posseg as pseg
words = pseg.cut("我爱北京天安门")
list1=[]
for word, flag in words:
     list1.append('%s %s' % (word, flag))
print(list1)