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

    elif A in B or B in A:
        return 1

a=[1,2,3,4]
b=[1,3]
c=SBS(a,b)
print(c)
