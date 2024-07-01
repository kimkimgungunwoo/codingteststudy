'''
반복문 설정이 애매하넹
'''

import sys
input=sys.stdin.readline

N,M=map(int,input().split())
std_lst=[0]*(N+1)
std_lst[0]=-1
field=[[] for x in range(N+1)]
AnswerList=[]
zeroque=[]

for i in range(M):
    a,b=map(int,input().split())
    field[a].append(b)
    std_lst[b]+=1

for i in range(N+1):
    if std_lst[i]==0:
        zeroque.append(i)
        AnswerList.append(i)
while zeroque:
    A=zeroque.pop(0)
    for i in field[A]:
        if std_lst[i]>0:
            std_lst[i]-=1
            if std_lst[i]==0:
                zeroque.append(i)
                AnswerList.append(i)
    
for i in range(len(AnswerList)):
    print(AnswerList[i],end=" ")
        
        
    
    