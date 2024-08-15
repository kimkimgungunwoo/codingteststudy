import sys
input=sys.stdin.readline

def gcd(a,b):
  if a%b == 0:
    return b
  return gcd(b,a%b)

def DFS(n):
    visited[n]=True
    for i in field[n]:
        if not visited[i[0]]:
            value[i[0]]=i[2]*value[n]//i[1]
            DFS(i[0])

N=int(input())
field=[[] for x in range(N)]
value=[1]*(N)
visited=[False]*(N)

common_denominator=1
for i in range(N-1):
    a,b,p,q=map(int,input().split())
    field[a].append((b,p,q))
    field[b].append((a,q,p))
    common_denominator*=((p*q)//gcd(p,q))
value[0]=common_denominator


DFS(0)

GCD=value[0]
for i in range(N):
    GCD=gcd(GCD,value[i])
    
for i in range(len(value)):
    value[i]=value[i]//GCD
print(*value)


