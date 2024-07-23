import sys
sys.setrecursionlimit(100000)  # 재귀 깊이 제한을 늘립니다.
input = sys.stdin.readline
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def Dfs(y, x, H):
    global visited
    visited[y][x] = True
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < N and 0 <= nx < N:
            if field[ny][nx] > H and not visited[ny][nx]:
                Dfs(ny, nx, H)
                        

N = int(input())
field = []
maxx = 0
dataset = set()
dataset.add(0)
maxanswer = 0

for i in range(N):
    inp = list(map(int, input().split()))
    field.append(inp)
    dataset.update(set(inp))

for H in dataset:
    answer = 0
    visited = [[False] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if field[i][j] > H and not visited[i][j]:
                Dfs(i, j, H)
                answer += 1
    maxanswer = max(maxanswer, answer)

print(maxanswer)
