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

x='双眼病变'
a=StrToList(x)
y='双眼发病'
b=StrToList(y)
c=SBS(a,b)
print(c)

import dowhy
from dowhy.do_why import CausalModel
import dowhy.datasets

# Load some sample data
data = dowhy.datasets.linear_dataset(
    beta=10,
    num_common_causes=5,
    num_instruments=2,
    num_samples=10000,
    treatment_is_binary=True)
    
