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
        return len(set(A)&set(B))/len(set(A)+set(B))
a=[1,2,3,4]
b=[0,3]
c=SBS(a,b)
print(c)
