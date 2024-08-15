import sys
input=sys.stdin.readline
anslist=[]
T=int(input())
for _ in range(T):
    N=int(input())
    field=[[0],[0]]
    for i in range(2):
        field[i]+=list(map(int,input().split()))
    dp = [[0] * (N + 1) for _ in range(2)]
    dp[0][1]=field[0][1]
    dp[1][1]=field[1][1]
    for i in range(2,N+1):
        dp[0][i]=max(dp[1][i-1],dp[1][i-2])+field[0][i]
        dp[1][i]=max(dp[0][i-1],dp[0][i-2])+field[1][i]
    anslist.append(max(dp[0][N],dp[1][N]))
for i in anslist:
    print(i)
    
       
    