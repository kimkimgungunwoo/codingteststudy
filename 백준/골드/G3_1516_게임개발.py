'''
다음 타겟도 그게 되는거냐
'''

import sys    
from collections import deque
input=sys.stdin.readline
N=int(input())
answerList=[0]*(N+1)
TimeLIst=[0]*(N+1)
field=[[] for x in range(N+1)]
DegreeList=[0]*(N+1)
Qeue=deque()
for i in range(1,N+1):
    Inp=list(map(int,input().split()))
    j=0
    TimeLIst[i]=Inp[j]
    j+=1
    while Inp[j]!=-1:
        field[Inp[j]].append(i)
        DegreeList[i]+=1
        j+=1
        
for i in range(1,len(DegreeList)):
    if DegreeList[i]==0:
        Qeue.append(i)
while Qeue:
    Node=Qeue.popleft()
    for i in field[Node]:
        DegreeList[i]-=1
        answerList[i]+=(TimeLIst[Node])
        if DegreeList[i]==0:
            Qeue.append(i)
for i in range(N+1):
    TimeLIst[i]+=answerList[i]

for i in range(1,N+1):
    print(TimeLIst[i])      
            
    



        