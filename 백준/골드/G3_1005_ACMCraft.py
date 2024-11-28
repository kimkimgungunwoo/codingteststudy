import sys
from collections import deque

input = sys.stdin.readline

T = int(input())
answer = []
for _ in range(T):
    N, K = map(int, input().split())
    timelist = [0] + list(map(int, input().split()))
    in_degree = [0] * (N + 1)
    build_flow = [[] for _ in range(N + 1)]
    dp = [0] * (N + 1)

    for _ in range(K):
        s, e = map(int, input().split())
        build_flow[s].append(e)
        in_degree[e] += 1

    target = int(input())
    
    # 위상 정렬을 위한 큐
    queue = deque()

    # 진입 차수가 0인 노드를 큐에 넣기
    for i in range(1, N + 1):
        if in_degree[i] == 0:
            queue.append(i)
            dp[i] = timelist[i]

    # 위상 정렬 수행
    while queue:
        current = queue.popleft()
        for next_node in build_flow[current]:
            in_degree[next_node] -= 1
            dp[next_node] = max(dp[next_node], dp[current] + timelist[next_node])
            if in_degree[next_node] == 0:
                queue.append(next_node)

    answer.append(dp[target])

for res in answer:
    print(res)
