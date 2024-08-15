import sys
input = sys.stdin.readline

A = input().rstrip()
B = input().rstrip()

# dp와 maxList를 B의 길이로 설정
dp = [0] * len(B)
maxList = [0] * len(B)

for i in A:
    maxvalue = 0
    for j in range(len(B)):
        if B[j] == i:
            dp[j] = maxList[j] + 1
        maxvalue = max(maxvalue, dp[j])
        maxList[j] = maxvalue

print(max(maxList))