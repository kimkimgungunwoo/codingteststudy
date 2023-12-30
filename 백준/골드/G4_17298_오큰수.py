import sys
input=sys.stdin.readline
N=int(input())
inplist=list(map(int,input().split()))
anslist=[0]*N
ansstack=[0]
for i in range(1,N):
    if inplist[i]>inplist[ansstack[-1]]:
        while len(ansstack)>0 and inplist[i]>inplist[ansstack[-1]] :
            anslist[ansstack.pop()]=inplist[i]
    ansstack.append(i)
        
for i in range(len(ansstack)):
    anslist[ansstack.pop()]=-1
print(*anslist)