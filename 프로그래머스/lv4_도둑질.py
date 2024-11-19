
def solution(money):
    answer1=0
    answer2=0
    dp=[0]*len(money)
    dp[0]=money[0]#2번은 무조건 안됨
    if len(money)==3:
        return max(money)
    for i in range(len(dp)-3):
        if i==1:
            pass
        dp[i+2]=max(dp[i+2],money[i+2]+dp[i])
        if i<len(dp)-4:  
           dp[i+3]=max(dp[i+3],money[i+3]+dp[i])
    
    answer1=max(dp)
    
    dp=[0]*(len(money))
    
    dp[1],dp[2]=money[1],money[2]
    for i in range(1,len(dp)-2):
        dp[i+2]=max(dp[i+2],money[i+2]+dp[i])
        if i<len(dp)-3:
            dp[i+3]=max(dp[i+3],money[i+3]+dp[i])
    answer2=max(dp)
    
    
    return max(answer1,answer2)
