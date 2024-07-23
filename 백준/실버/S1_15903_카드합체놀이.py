'''
자료구조 필요?

제일작은거+제일 큰거 더해야 할거 같은데?
제일작은거+그 다음작은거가 맞나?
맞네 ㅅㅂ ㅋㅋ 문제 이해를 잘못했네


'''
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
