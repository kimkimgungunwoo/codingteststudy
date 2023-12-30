white_paper=[[0 for i in range(100)] for k in range(100)]
N=int(input())
answer=0
for i in range(0,N):
    balck_map=list(map(int, input().split()))
    for j in range(balck_map[1],balck_map[1]+10):
        for jj in range(balck_map[0],balck_map[0]+10):
            white_paper[j][jj]=1
for row in white_paper:
    for num in row:
        answer += num
print(answer)

            
