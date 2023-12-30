import heapq
N=int(input())
M_heap=[]
answer=0
for i in range(N):
    heapq.heappush(M_heap,int(input()))
while len(M_heap) >1:
    int1=heapq.heappop(M_heap)
    int2=heapq.heappop(M_heap)
    heapq.heappush(M_heap,int1+int2)
    answer+=int1+int2
print(answer)
    