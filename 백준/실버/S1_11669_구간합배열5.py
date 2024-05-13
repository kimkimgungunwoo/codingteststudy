'''
어떤식으로 채우지->맨윗줄,맨왼쪽줄->그냥 단순채우기
중간부터->위+왼쪽+지금-겹(i-1)(j-1)-->왼,위에 0으로 채워진 애들 추가하고 그걸로 계산
한번에 받아들이면서 합치면 될듯?->구간합

어떻게 뺄것인가? -> 빼고 빼고 겹치는부분 더하기
'''
import sys

input=sys.stdin.readline
N,M=map(int,input().split())
anslist=[]
field=[[0 for i in range(N+1)] for i in range(N+1)]
for i in range(1,N+1):
    inp=list(map(int,input().rstrip().split()))
    for j in range(1,N+1):
        field[i][j]=field[i-1][j]+field[i][j-1]+inp[j-1]-field[i-1][j-1]

for i in range(M):
    x1,y1,x2,y2=map(int,input().split())
    answer=field[x2][y2]-field[x2][y1-1]-field[x1-1][y2]+field[x1-1][y1-1]
    anslist.append(answer)

for i in range(len(anslist)):
    print(anslist[i])
    