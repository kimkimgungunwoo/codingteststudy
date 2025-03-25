'''
N kg 짜리 무게를 M kg 가 최대인 가방에 넣을때 M-Nkg 가  최대인 가방에 물건을 추가한다는 방식으로 접근 하기때문에 dp문제

6 kg가최대인 가방에 3kg 넣을지 말지 고민→ 3kg 가방에 3kg 물건 추가 할까? 로 변환 

⇒가방에 가방을 넣을 수 있다고 생각하자

무게를 0에서 부터 키워가며 탐색할떄

→무게가 w인 가방에  k번째 물건까지 탐색했다 쳤을때

→물건을 안담으면 dp[k+1][w]=dp[k]p[w]

⇒물건을 담으면 dp[k+1][w]=max(dp[k][w],dp[k][w-weight[k+1])
'''

import sys
input = sys.stdin.readline

N, K = map(int, input().split())
items = [list(map(int, input().split())) for _ in range(N)]

dp = [[0] * (K + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    weight, value = items[i - 1]
    for w in range(K + 1):
        if weight > w:
            dp[i][w] = dp[i - 1][w]
        else:
            dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weight] + value)

print(dp[N][K])
