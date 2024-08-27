import sys
input=sys.stdin.readline
N=int(input())
answer=0
dp=[[1]*N for _ in range(10)]

for i in range(1,10):
    for j in range(1,N):
        dp[i][j]=dp[i-1][j]+dp[i][j-1]
        
for i in range(10):
    answer+=dp[i][N-1]
    
print(answer%10007)
    