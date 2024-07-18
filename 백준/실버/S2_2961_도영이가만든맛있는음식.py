#재료 재귀적으로 탐색//넣는경우 안넣는 경우 구분 1 1*2 1*2*3 

import sys
input=sys.stdin.readline

def dfs(n,index,s,b):
    global answerlist
    if n==1: #첫 재로일 경우 일단 추가 
        s,b=map(int,inplist[index])
    else:
        s*=inplist[index][0] 
        b+=inplist[index][1]
    answerlist.append(abs(s-b))
    for i in range(index+1,N):
        dfs(n+1,i,s,b)
        
    
    
taste=[]
N=int(input())
inplist=[]
answerlist=[]
for _ in range(N):
    inplist.append(list(map(int,input().split())))
for i in range(N):
    dfs(1,i,0,0)
print(min(answerlist))