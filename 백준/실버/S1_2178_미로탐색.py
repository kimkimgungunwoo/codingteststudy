
import sys
from collections import *

def BFS(i,j):
    ansque=deque()
    ansque.append((i,j))
    visited[i][j]==True
    while ansque:
        now=ansque.popleft()
        for k in range(4):
            nowx=now[1]+dx[k]
            nowy=now[0]+dy[k]
            if nowx>=0 and nowy>=0 and nowx<M and nowy<N:
                if visited[nowy][nowx] ==False and inplist[nowy][nowx]==1:
                    visited[nowy][nowx]=True
                    inplist[nowy][nowx]=inplist[now[0]][now[1]]+1
                    ansque.append((nowy,nowx))
                
                    
    
    


input=sys.stdin.readline
N,M=map(int,input().split())
ansque=deque()
dx=[0,1,0,-1]
dy=[1,0,-1,0]
inplist=[[0]*M for _ in range(N)]
visited=[[False]*M for _ in range(N)]
for i in range(N):
    inp=input()
    for j in range(M):
        inplist[i][j]=int(inp[j])
BFS(0,0)
print(inplist[N-1][M-1])