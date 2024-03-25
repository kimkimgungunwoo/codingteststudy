def solution(k, m, score):
    score=sorted(score,reverse=True)
    rindex=m-1
    answer=0
    while rindex<len(score):       
        answer+=score[rindex]*m
        rindex+=m                   
               
    return answer