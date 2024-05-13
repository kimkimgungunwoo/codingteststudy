import sys
input=sys.stdin.readline
N,M,V=map(int,input().split())
DfsVisit=[False]*(N+1)
Bfsvisit=[False]*(N+1)
field=[[] for x in range(N+1)]
Dfsstack=[]
Dfsvisitlist=[]
Bfsqueue=[]
Bfsvisitlist=[]

def BFS(i):
    Bfsqueue.append(i)
    Bfsvisit[i]=True
    Bfsvisitlist.append(i)
    while Bfsqueue:
        node=Bfsqueue.pop(0)
        for j in field[node]:
            if not Bfsvisit[j]:
                Bfsvisit[j]=True
                Bfsqueue.append(j)
                Bfsvisitlist.append(j)  
def Dfs(i):
    DfsVisit[i]=True
    Dfsvisitlist.append(i)
    for j in field[i]:
        if not DfsVisit[j]:
            Dfs(j)   
    
    
for i in range(M):
    s,e=map(int,input().split())
    field[s].append(e)
    field[e].append(s)
for i in range(1,N+1):
    field[i].sort()
Dfs(V)
BFS(V)
print(*Dfsvisitlist)
print(*Bfsvisitlist)

        