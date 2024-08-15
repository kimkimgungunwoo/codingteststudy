import sys
input=sys.stdin.readline
N=int(input())
dp=[[0 for _ in range(N+1)]for _ in range(10)]

for i in range(1,10):
    dp[i][1]=1
for j in range(2,N+1):
    for i in range(10):
        if i!=0 and i!=9:
            dp[i][j]=dp[i-1][j-1]+dp[i+1][j-1]
        if i==0:
            dp[i][j]=dp[i+1][j-1]
        if i==9:
            dp[i][j]=dp[i-1][j-1]
ans=0
for i in range(10):
    ans+=dp[i][N]
print(int(ans%1000000000))