def SBS(A,B):
    if A==0 or B ==0:
        return 0

    elif set(A)<=set(B) or set(B)<=set(A):
        return 1
    else:
        return len(set(A)&set(B)) /len(set(A)|set(B))

def StrToList(A):
    C=[]
    for i in A:
        C.append(i)
    return C
import re

f = open('D:\DeepLearning ER\Z1006014.txt','r',errors='ignore')
g =  open(r'C:\Users\Administrator\Desktop\ICD-10.txt','r',errors='ignore')
line_re=[]
lines = f.readlines()
dics=g.readlines()
for dic in disc:
    dic=re.sub('\n','')

for line in lines:
    line=re.sub('\n','',line)
    line=re.sub(' ','',line)
    line = re.sub(r'\?|？', '',line)
    line = re.sub(r'\,|\.|；','',line)
    line_re.append(line)
while '' in line_re:
    line_re.remove('')
for line in line_re:


