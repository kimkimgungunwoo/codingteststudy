'''
1.연산자들의 배치를 어떻게 할것인가?->연산자들을 그대로 두고 숫자들을 때려 박는건 불가능함
2.중복을 어떻게 고려할것인가

===
연산자 배치 로직이 제일 중요해 보이는데
숫자를 작게 만들고 그러는 정해진 무언가가 있나

하나씩 재귀함수로 오른쪽으로 무한 옮기기 하는 식으로?

+ - *
A A A A
A+A A A
A+A-A A
A+A-A*A
A+A A-A
A+A*A-A
A A+A A
A-A+A A
A-A+A*A
A A+A-A
A*A+A-A
A A A+A
A-A A+A
A-A*A+A
A A A+A
A A-A+A
A*A-A+A

이런 로직일거 같은데 그럼 맨 스타트에 있던에가 N+1칸으로 가면 끝나는 걸로 세팅하자

중복은 어떻게 쳐냄?
걍 무시하면 시간초과 날거같은데
+ + - *
....
+...
++..
++-.
++-*
++..
++.-
++*-
+...
+.+.
+-+.
+-+*
+.+.
+*+-
+...
+..+
+-.+

재귀함수 dfs 로 조지면 되긴할듯!
'''
import sys
input=sys.stdin.readline

def Dfs(n,a): #재귀함수로 구현된 백트래킹
    global maxx #최댓값,최솟값 판별한 수 전역변수ㅗ하
    global minn 
    global OList
    
    if n==N-1: #최종결론낼 뭐시깽이 설정
        maxx=max(a,maxx)
        minn=min(a,minn)
        return
    
    if OList[0]!=0:
        OList[0]-=1
        Dfs(n+1,a+InpList[n+1]) 
        OList[0]+=1 #재활용 해야 하니까 다시 늘리긩->재귀 함수 한 턴 끝나고 나면 다시 활용됨
    
    if OList[1]!=0:
        OList[1]-=1
        Dfs(n+1,a-InpList[n+1])
        OList[1]+=1
        
    if OList[2]!=0:
        OList[2]-=1
        Dfs(n+1,a*InpList[n+1])
        OList[2]+=1
        
    if OList[3]!=0:
        OList[3]-=1
        Dfs(n+1,int(a/InpList[n+1]))
        OList[3]+=1
    
N=int(input())
AnswerList=[]
InpList=list(map(int,input().split()))
OList=list(map(int,input().split()))
maxx = -1e9 #작은수,큰수
minn = 1e9
Dfs(0,InpList[0])
print(maxx)
print(minn)