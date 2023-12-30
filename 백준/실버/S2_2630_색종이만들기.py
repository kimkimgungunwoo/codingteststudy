
import sys
def solution(search_range,x,y,cnt_col):
    base=field[y][x]
    for i in range(y,y+search_range):
        for j in range(x,x+search_range):
            if field[i][j]!=base:
                search_range//=2
                solution(search_range,x,y,cnt_col)
                solution(search_range,x,y+search_range,cnt_col)
                solution(search_range,x+search_range,y,cnt_col)
                solution(search_range,x+search_range,y+search_range,cnt_col)
                return
    if base==0:
        cnt_col[0]+=1
    else:
        cnt_col[1]+=1
N=int(sys.stdin.readline().rstrip())
field=[]
for i in range(N):
    field.append(list(map(int,sys.stdin.readline().rstrip().split())))
cnt_col=[0,0]
search_range=N
solution(search_range,0,0,cnt_col)
print(cnt_col[0])
print(cnt_col[1])