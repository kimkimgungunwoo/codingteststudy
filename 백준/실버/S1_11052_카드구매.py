import sys
input=sys.stdin.readline
N=int(input())
dp=[0]
dp+=list(map(int,input().split()))
for i in range(1,N+1):
    for j in range(i+1,N+1):
        dp[j]=max(dp[j-i]+dp[i],dp[j])
print(dp[N])

        