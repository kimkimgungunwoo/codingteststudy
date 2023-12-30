import sys
input=sys.stdin.readline
N,M=map(int,input().split())
anslist=[]
plist=[x for x in range(N+1)]

def find(A):
    if A==plist[A]:
        return A    
    else:
        plist[A]=find(plist[A])
        
        return plist[A]
def union(A,B):
    A=find(A)
    B=find(B)
    if A!=B:
        plist[B]=A

def chsame(A,B):
    if find(A)==find(B):
        return True
    return False

for i in range(M):
    Q,A,B=map(int,input().split())
    if Q==0:
        union(A,B)
    else:
        if chsame(A,B):
            anslist.append("YES")
        else:
            anslist.append("NO")
for i in anslist:
    print(i)