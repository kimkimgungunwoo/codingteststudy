'''
1.숫자 입력받아 문자열 안에서 동작 반복
2.숫자 두개 입력받기
    1.행렬 형식으로 작동?->도화지 크기 만큼의 이중배열 0으로 채워놓고 
        색종이 부분 1로 채우기


'''

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

            
