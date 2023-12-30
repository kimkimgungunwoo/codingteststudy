import sys
from collections import deque
input=sys.stdin.readline
N,L=map(int,input().split())
inplist=list(map(int,input().split()))
ansque=deque()
ansque.append((0,inplist[0]))
print(ansque[0][1],end=" ")
for i in range(1,N):
    if i-ansque[0][0]>=L:
        ansque.popleft()
    while len(ansque)!=0 and ansque[-1][1]>inplist[i]:
        ansque.pop()
    ansque.append((i,inplist[i]))       
    print(ansque[0][1],end=" ")
