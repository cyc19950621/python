import time
import math
import os
import sys
import os, os.path,shutil
import codecs 
import EMRdef
import re

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

x='干活'
a=StrToList(x)
b=['干','了']
c=SBS(a,b)
print(c)
