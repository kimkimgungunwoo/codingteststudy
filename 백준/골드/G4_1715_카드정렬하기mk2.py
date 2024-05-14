import heapq
import sys
input=sys.stdin.readline
lst=[]
answer=0
cnt=0
temp=0
N=int(input())
for i in range(N):
    heapq.heappush(lst,int(input()))

while len(lst)>1:
    i1=heapq.heappop(lst)
    i2=heapq.heappop(lst)
    heapq.heappush(lst,i1+i2)
    answer+=i1+i2
print(answer)