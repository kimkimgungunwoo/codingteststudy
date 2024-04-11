'''
1.다이나믹 프로그래밍의 정수인 문제인듯
2.어차피 옮겨야할애들 뽑아두면 무조건 알아서 배열됨
3.만들어지는 오름차순의 최대 길이만 체크하면 됨
4.최대 길이 체크가 dp,
'''
N=int(input())
inp=list(map(int,input().split()))
dp=[0]*(N+1)
for i in range(N):
    dp[inp[i]]=dp[inp[i]-1]+1
print(N-max(dp))

        