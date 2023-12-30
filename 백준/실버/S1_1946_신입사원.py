import sys
T=int(sys.stdin.readline())

answer_list=[0]*T
for i in range(T):
    N=int(sys.stdin.readline())
    nlist = [[0, 0] for _ in range(N)]
    for j in range(N):
        nlist[j][0],nlist[j][1]=map(int,sys.stdin.readline().split())
    nlist=sorted(nlist,key=lambda x:x[0])
    cnt=1
    min_1=nlist[0][1]
    for j in range(1,N):
        if nlist[j][1]<min_1:
            min_1=nlist[j][1]
            cnt+=1
            
    answer_list[i]=cnt
for i in range(T):
    print(answer_list[i])
