import sys
import math
input=sys.stdin.readline

def solution(queen_field,y,xlist):
    global ans
    
    if y==N:
        ans+=1
        return
        
    for i in range(N):
        if xlist[i]==True:
            chk=1
            for j in queen_field:
                if abs(i-j[0])/(y-j[1])==1:
                    chk=0
                    break
            if chk==1:
                xlist[i]=False
                queen_field.append([i,y])
                solution(queen_field,y+1,xlist)
                xlist[i]=True
                queen_field.pop()
                
                    
    
    
    
ans=0
N=int(input())
queen_field=[]
xlist=[True]*N
for i in range(N):
    xlist[i]=False
    queen_field.append([i,0])
    solution(queen_field,1,xlist)
    xlist[i]=True
    queen_field.pop()
print(ans)


