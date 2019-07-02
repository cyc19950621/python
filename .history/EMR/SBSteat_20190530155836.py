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
from pyDatalog import pyDatalog

pyDatalog.create_atoms( 'N, N1, X, Y, X0, X1, X2, X3, X4, X5, X6, X7' )
pyDatalog.create_atoms( 'ok, queens, next_queen, pred, pred2' )

size = 8
ok( X1, N, X2 ) <= ( X1 != X2 ) & ( X1 != X2 + N ) & ( X1 != X2 - N )

pred( N, N1 )  <= ( N > 1 ) & ( N1 == N - 1 )
queens( 1, X ) <= ( X1._in( range( size ) ) ) & ( X1 == X[0] )
queens( N, X ) <= pred( N, N1 ) & queens( N1, X[:-1] ) & next_queen( N, X )

pred2( N, N1 )   <= ( N > 2 ) & ( N1 == N - 1 )
next_queen( 2, X ) <= ( X1._in( range( 8 ) ) ) & ok( X[0], 1, X1 ) & ( X1 == X[1] )
next_queen( N, X ) <= pred2( N, N1 ) & next_queen( N1, X[1:] ) & ok( X[0], N1, X[-1] ) 

print( queens( size, ( X0, X1, X2, X3, X4, X5, X6, X7 ) ) )


