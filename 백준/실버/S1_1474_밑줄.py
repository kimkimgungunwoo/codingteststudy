
import sys
N,M=map(int,sys.stdin.readline().split())
strlist=['']*N
strl=0
for i in range(N):
    strlist[i]=sys.stdin.readline().rstrip()
    strl+=len(strlist[i])
    
need_under=M-strl
answer=""
over_under=need_under%(N-1)
for i in range(N-1):
    if strlist[i+1]>='a' and over_under>0:
        strlist[i]+="_"*(int((need_under/(N-1))+1))
        over_under-=1
    else:
        strlist[i]+="_"*(int(need_under/(N-1)))

while over_under>0 and i>0:
    if strlist[i].count("_")==int((need_under/(N-1))):
        strlist[i]+="_"
        over_under-=1
    i-=1
answer=''.join(strlist)    
print(answer)
    

