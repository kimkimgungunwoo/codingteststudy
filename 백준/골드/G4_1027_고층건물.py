def check_s(x, n, index, b_list):
    
    x_g = (h_list[x] - h_list[index]) / (x - index)
    if x_g >n:
        b_list[index][x] = b_list[x][index] = 1
        n = x_g
    if x == N - 1:
        return
    check_s(x + 1, n, index, b_list)

N = int(input())
b_list = [[0 for _ in range(N)] for _ in range(N)]
h_list = list(map(int, input().split()))

for index in range(N - 1):
    b_list[index][index+1]=b_list[index+1][index]=1
    check_s(index + 1, h_list[index + 1] - h_list[index], index, b_list)

answer = sum(b_list[0])
for l in range(N):
    answer = answer if answer > sum(b_list[l]) else sum(b_list[l])
print(answer)