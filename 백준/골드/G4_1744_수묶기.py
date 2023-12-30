from collections import deque
ans=0
N=int(input())
inplist=[]
zerolist=[]
undintlist=[]
for i in range(N):
    inp=int(input())
    if inp>=2:
        inplist.append(inp)
    if inp==1:
        ans+=1
    if inp==0:
        zerolist.append(inp)
    if  inp<0:
        undintlist.append(inp)
        
inplist.sort()
ansque=deque(inplist)
undintlist.sort()
undintque=deque(undintlist)

while len(ansque)>0:
    a1=ansque.pop()
    if len(ansque)==0:
        ans+=a1
        break
    ans+=(a1*ansque.pop())
while len(undintque)>0:
    a1=undintque.popleft()
    if len(undintque)>0:
        ans+=(a1*undintque.popleft())
    else:        
        if len(zerolist)>=1:
            zerolist.pop()
        else:
            ans+=a1
print(ans)

    

