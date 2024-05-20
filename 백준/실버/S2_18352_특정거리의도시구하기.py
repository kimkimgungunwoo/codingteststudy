
import sys
input=sys.stdin.readline     

def BFS(i):
    visited[i]=0
    que=[]
    anss=[]
    que.append(i)
    while que:
        n=que.pop(0)
        if visited[n]>K:
            break
        for j in lst[n]:
            if visited[j]==-1:
                visited[j]=visited[n]+1
                if visited[j]==K:
                    anss.append(j)
                que.append(j)
    return sorted(anss)

    
    
anslist=[] 

N,M,K,X=map(int,input().split())

lst=[[] for i in range(N+1)]
visited=[-1]*(N+1)
for i in range(M):
    a,b=map(int,input().split())
    lst[a].append(b)
vlst=BFS(X)
for i in range(len(vlst)):
    if vlst[i]==K:
        anslist.append(vlst[i])
if len(vlst)==0:
    print(-1)
else:
    for i in vlst:
        print(i)