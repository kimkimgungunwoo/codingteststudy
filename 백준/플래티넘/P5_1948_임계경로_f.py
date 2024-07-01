import sys
from collections import deque
input=sys.stdin.readline    
N=int(input())
M=int(input())
field=[[] for x in range(N+1)]
ReverseField=[[] for x in range(N+1)]
DegreeList=[0]*(N+1)
RouteList=[0]*(N+1)
AnswerList=[]
for _ in range(M):
    a,b,c=map(int,input().split())
    field[a].append([b,c])
    ReverseField[b].append([a,c])
    DegreeList[b]+=1
    
s,e=map(int,input().split())
Qeue=deque()
Qeue.append(s)

while Qeue:
    n=Qeue.popleft()
    for i in field[n]:
        DegreeList[i[0]]-=1
        if RouteList[i[0]]<RouteList[n]+i[1]:
            RouteList[i[0]]=RouteList[n]+i[1]
        if DegreeList[i[0]]==0:
            Qeue.append(i[0])

AnswerList.append(RouteList[e])
cnt=0
Qeue.append(e)
visited=[False]*(N+1)
while Qeue:
    n=Qeue.popleft()
    for i in ReverseField[n]:
        #아무 문제 없이 통과한 도로쪽의 도시가 상관 있나?
        if RouteList[i[0]]+i[1]==RouteList[n] and not visited[i[0]]:
            cnt+=1
            Qeue.append(i[0])
            visited[n]==True
AnswerList.append(cnt)
for i in AnswerList:
    print(i)
        
    