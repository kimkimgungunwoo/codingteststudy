'''
얘도 백트래킹+브루트포스

스타티팀인경오,링크팀인경우 어떻게 구분해야할까?
메모리 제한 평범하고
경우의 수가 너무 많은디
, 걍 두번 하면 되나?->교차로 일단 해보자
->짝수번째->스타티팀/홀수번째 링크팀으로 취급한다음 우겨넣으면 되는건강
아니면 세명만 뽑아가고 나머지 애들끼리만 놀게 하면 되나

세명 뽑아가고 나머지애들끼리 알아서 삐슝빠슝하면 될듯
visited 쓰면 되지 않낭
visited쓰고 순서 짝수/홀수이냐에 따라서 팀 나누면 될듯

탐색 용 함수랑 
계산용 함수 따로 만들어두자
'''
import sys
input=sys.stdin.readline
minn=1e9

def Dfs(cnt,vlaue):
    global steam
    global rteam
    global minn
    visited[vlaue]=True
    if cnt%2==0:
        steam.append(vlaue)
        if vlaue!=max(steam):
            return
    else:
        rteam.append(vlaue)
        if vlaue!=max(rteam):
            return
    for i in range(1,N):
        if not visited[i]:
            Dfs(cnt+1,i)
            if cnt%2!=0:
                steam.pop()
            else:
                rteam.pop()
            visited[i]=False    
    if cnt==N:    
        temp=abs(CalTeamStatus(steam)-CalTeamStatus(rteam))
        minn=min(temp,minn)
        

def CalTeamStatus(lst):
    temp=0
    for i in range(len(lst)-1):
        for j in range(i+1,len(lst)):
            temp+=field[lst[i]][lst[j]]+field[lst[j]][lst[i]]
    return temp

field=[]
N=int(input())
visited=[False]*N
steam=[]
rteam=[]

for _ in range(N):
    field.append(list(map(int,input().split())))

Dfs(1,0)
print(minn)
