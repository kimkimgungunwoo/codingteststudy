#발상은 잘 했는데 2차원 배열 다루는 디테일이 차이가 있네

import sys
input=sys.stdin.readline
N,M=map(int,input().split())
nslist=[[0]*(N+1)]
slist=[[0]*(N+1) for x in range(N+1)]
anslist=[]
for i in range(N):
    nslist.append(([0]+[int (x) for x in input().split()]))

for i in range(1,N+1):
    for j in range(1,N+1):
        slist[i][j]=slist[i][j-1]+slist[i-1][j]-slist[i-1][j-1]+nslist[i][j]
        
for i in range(M):
    x1,y1,x2,y2=map(int,input().split())
    ans=slist[x2][y2]+slist[x1-1][y1-1]-slist[x1-1][y2]-slist[x2][y1-1]
    anslist.append(ans)
for i in range(M):
    print(anslist[i])