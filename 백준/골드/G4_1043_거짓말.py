import sys

def Union(A,B):
    A=find(A)
    B=find(B)
    if A!=B:
        geust_list[B]=A

def find(A):
    if A==geust_list[A]:
        return A
    else:
        return find(geust_list[A])

input=sys.stdin.readline
N,M=map(int,input().split())
truemanlist=list(map(int,input().split()))
geust_list=[x for x in range(N+1)]
truemanlist.pop(0)
answer=0
field=[]
if truemanlist:
    for i in range(0,len(truemanlist)):
        Union(truemanlist[0],truemanlist[i])
    
    for i in range(M):
        field.append(list(map(int,input().split())))
        field[i].pop(0)
        for j in (field[i]):
            if find(j)==truemanlist[0]:
                Union(j,field[i][0])
            else:
                Union(field[i][0],j)
    for i in range(M):
        if find(field[i][0])!=truemanlist[0]:
            answer+=1
    print(answer)           
else:
    for i in range(M):
        input()
    print(M)