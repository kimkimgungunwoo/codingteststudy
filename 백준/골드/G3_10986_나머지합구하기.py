import sys
input=sys.stdin.readline
N,M=map(int,input().split())
inplist=list(map(int,input().split()))
alsumlist=[0]*N
sameremlist=[0]*M
ans=0
alsumlist[0]=inplist[0]%M
for i in range(1,N):
    alsumlist[i]=alsumlist[i-1]+inplist[i]
    
for i in range(N):
    rem=alsumlist[i]%M
    if rem==0:
        ans+=1    
    sameremlist[rem]+=1
for i in range(M):
    if sameremlist[i]>1:
        ans+=((sameremlist[i]*(sameremlist[i]-1))//2)
print(ans)