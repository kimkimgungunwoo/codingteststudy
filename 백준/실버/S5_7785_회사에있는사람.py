import sys
input=sys.stdin.readline
N=int(input())
ansset=set()
for i in range(N):
    hu,ans=map(str,input().split())
    if ans =="enter":
        ansset.add(hu)
    if ans=="leave":
        ansset.discard(hu)
anslist=list(ansset)
anslist.sort(reverse=True)
for i in range(len(anslist)):
    print(anslist[i])
