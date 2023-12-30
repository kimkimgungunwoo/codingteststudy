

import sys
input=sys.stdin.readline
N=int(input())
timelist=[]
for i in range(N): 
    timelist.append(list(map(int,input().split())))
timelist.sort(key=lambda x:(x[1],x[0]) )
lasttime=0
cnt=0
for i in range(len(timelist)):
    if timelist[i][1]>=lasttime:
        if timelist[i][0]>=lasttime:
            cnt+=1
            lasttime=timelist[i][1]
print(cnt)        
