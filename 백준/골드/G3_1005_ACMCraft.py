'''
dp+그래프
1.그래프를 어떻게 구현?->역방향
2.dp도 비슷하게

무조건 max값이 답은 아니지 않나->일단 도착선이 두개 이상이면 max이용 해야지
방향 연결 그래프 두개 만들어서 해야할듯?

순서를 어떻게 설정?
어차피 목적지는 설정됐는데 걍 거꾸로 가면 되는거 아니냐
'''

import sys
import copy
import queue
input=sys.stdin.readline

    
    

T=int(input())
answer=[]
for t in range(T):
    N,K=map(int,input().split())
    timelist=[0]+list(map(int,input().split()))
    dp=[0]*(N+1)
    build_flow=[[] for x in range(N+1)]
    reverse_build_flow=[[] for x in range(N+1)]
    for i in range(K):
        s,e=map(int,input().split())
        reverse_build_flow[e].append(s)
    target=int(input())
    dp[target]=timelist[target]
    BFS=queue.Queue()
    BFS.put(target)
    while not BFS.empty():
        sn=BFS.get()
        for A in reverse_build_flow[sn]:
            dp[A]=max(timelist[A]+dp[sn],dp[A])
            BFS.put(A)
    answer.append(max(dp)) 
for i in answer:
    print(i) 
            
    
    