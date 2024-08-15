'''
다이나믹은 이미 써져 있으니께.. 다이나믹은당연히 필요한거고
그래프 이론도 섞인듯
DP를 어떻게 작성할까 최단경로의 개수->왼쪽/아래이동횟수는 같은데 최소 경로가 의미가있나?
dp[i][j]=max(dp[i][j],dp[i][j-1]+dp[i-1][j])->여러 경로가 겹칠수도 있으니까,
숫자 상승 로직설정이 다음으로 중요해보임
이게 기본 로직이긴한데
->물 돌아가는거만 잘 설정하면
물 돌아가는건 신경 안써도 될듯->위의 점화식이 무조건맞을듯

점화식은 맞음
어떻게 채울지?->bfs이용
visited는 신경x->어차피 역주행 안함

@ 
좌표구조 위<->아래 변경되는건 크게 상관없나==>ㅇㅇ/아래로이동-->y+1
visited-->어차피 역방문 안되서 소용x
==========
다이나믹프로그래밍+BFS 가 아니네 씌벌
'''
from collections import deque

def solution(m,n,puddles):
    field=[[0]*(m+1) for x in range(n+1)]
    for i in puddles:
        field[i[1]][i[0]]=-1
    field[1][1]=1
    for i in range(1,n+1):
        for j in range(1,m+1):
            if i==j==1:
                continue
            if field[i][j]==-1:
                field[i][j]=0
            else:
                field[i][j]=field[i-1][j]+field[i][j-1]    
            
      
    answer=field[n][m]%1000000007
    return answer
    