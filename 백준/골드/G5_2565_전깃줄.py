import sys
N = int(input())
field = []
afield = []

for _ in range(N):
    a, b = map(int, input().split())
    field.append((a, b))

field.sort(key=lambda x: x[0])
dp = [1] * N

for i in range(1,N):
    for j in range(0,i):
        if field[j][1] <field[i][1]:
            dp[i]=max(dp[i],dp[j]+1)
print(N-max(dp))
