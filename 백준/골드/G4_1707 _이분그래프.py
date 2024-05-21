import sys
sys.setrecursionlimit(10**6)
input=sys.stdin.readline
CH=True


T=int(input())

def DFS(n):
    global CH
    visited[n]=True
    for i in field[n]:
        if not visited[i]:
            check[i]=(check[n+1])%2
            DFS(i)
        
        elif check[n]==check[i]:
            CH=False
anslist=[]    
for _ in range(T):
    V,E=map(int,input().split())
    field=[[]for _ in range(V+1)]
    visited=[False]*(V+1)
    check=[0]*(V+1)
    CH=True
    
    for i in range(E):
        a,b=map(int,input().split())
        field[a].append[b]
        field[b].append(a)
    
    for i in range(1,V+1):
        if CH:
            DFS(i)
        else:
            break
        
    if CH:
        anslist.append("YES")
    else:
        anslist.append("NO")
for i in anslist:
    print(i)