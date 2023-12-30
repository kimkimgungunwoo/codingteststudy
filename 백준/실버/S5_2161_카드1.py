N=int(input())
backedcrd=[x+1 for x in range(N)]
printcard=[]
cnt=1
while len(printcard)<N:
    if cnt%2==0:
        backedcrd.append(backedcrd.pop(0))
    else:
        printcard.append(backedcrd.pop(0))
    cnt+=1
for i in range(N):
    print(printcard[i],end=" ")
