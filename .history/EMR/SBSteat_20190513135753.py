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

x='双眼动脉硬化性视网膜病变'
a=StrToList(x)
y='双眼动脉硬化性视网膜发病'
b=StrToList(y)
c=SBS(a,b)
print(c)
