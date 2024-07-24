def solution(picks, minerals):
    global mn
    mn=1e9
    mine={"stone":2,"iron":1,"diamond":0}
    def Dfs(N,index,result):#index-->minerals탐색용
        global mn
        picks[N]-=1
        for i in range(5):#index->mineralss
            deg=N-mine[minerals[index+i]]
            if deg<=0:deg=0
            result+=5**deg
            if index+i==len(minerals)-1:
                mn=min(mn,result)
                return
        index+=5
        if sum(picks)==0:
            mn=min(mn,result)
            return
            
        if picks[0]!=0:
            Dfs(0,index,result)
            picks[0]+=1
        
        if picks[1]!=0:
            Dfs(1,index,result)
            picks[1]+=1
        
        if picks[2]!=0:
            Dfs(2,index,result)
            picks[2]+=1
    
    for i in range(len(picks)):
        if picks[i]!=0:
            Dfs(i,0,0)
            picks[i]+=1
    answer = mn
    return answer



