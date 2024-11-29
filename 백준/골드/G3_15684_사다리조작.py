import sys
input=sys.stdin.readline
def check_ladder():
    for s in range(N):
        n=s
        for j in range(H):
            if field[j][n]:
                n+=1
            elif n>0 and field[j][n-1]:
                n-=1
        
        if n!=s:
            return False
        
    return True
   
def dfs(cnt,x,y):
    global ans 
    if check_ladder():
        ans=min(cnt,ans)
        return 
    elif cnt==3 or ans<=cnt:
        return 
    
    
    for i in range(x,H):
        for j in range(0,N-1):
            if field[i][j]==0:
                field[i][j]=True
                dfs(cnt+1,i,j+2)
                field[i][j]=False
    
N,M,H=map(int,input().split())
field=[[False] *N for x in range(H)]
for _ in range(M):
    a,b=map(int,input().split())
    field[a-1][b-1]=True
    
ans=4
dfs(0,0,0)
print(ans if ans<4 else -1)