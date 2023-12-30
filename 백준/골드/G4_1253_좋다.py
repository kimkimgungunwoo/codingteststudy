import sys
input=sys.stdin.readline
N=int(input())
inplist=list(map(int,input().split()))
inplist.sort()
answer=0

for i in range(N):
    bas=inplist[i]
    sind=0
    eind=N-1
    while sind<eind:
        res=inplist[sind]+inplist[eind]
        if res==bas:
            if sind!=i and eind!=i:                
                answer+=1
                break
            elif sind==i:
                sind+=1
            elif eind==i:
                eind-=1
        if res>bas:
            eind-=1
        if res<bas:
            sind+=1 
print(answer)        
    
            
            
            
            
            
#음수가 있었네 이 십랑라ㅣㅁ;ㄹㅇㄴ