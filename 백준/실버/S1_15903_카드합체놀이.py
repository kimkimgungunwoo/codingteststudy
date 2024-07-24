import sys
import heapq

input=sys.stdin.readline
n,m=map(int,input().split())
hq=sorted(list(map(int,input().split())))
for _ in range(m):
    a=heapq.heappop(hq)
    b=heapq.heappop(hq)
    temp=a+b
    a=temp
    b=temp
    heapq.heappush(hq,a)
    heapq.heappush(hq,b)
print(sum(hq))
