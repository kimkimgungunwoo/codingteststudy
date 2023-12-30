

import sys
input=sys.stdin.readline
N,M=map(int,input().split())
nodes=[[]for i in range(N+1)]
answer=False
visited=[False]*(N+1)

def DFS(v,depth):
    global answer
    if depth==5:
        answer=True
        return

    visited[v]=True
    for i in nodes[v]:
        if not visited[i]:
            DFS(i,depth+1)
    visited[v]=False

for _ in range(M):
    s,e=map(int,input().split())
    nodes[s].append(e)
    nodes[e].append(s)

for i in range(N):
    DFS(i,1)
    if answer:
        print(1)
        break
    
if not answer:
    print(0)
    