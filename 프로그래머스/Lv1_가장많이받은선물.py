def solution(friends, gifts):
    friendsdict={friends[x]:x for x in range(len(friends))}
    giftsfield=[[0 for x in range(len(friends))] for k in range(len(friends))]
    for i in range(len(gifts)):
        a=gifts[i].split()[0]
        b=gifts[i].split()[1]
        giftsfield[friendsdict[a]][friendsdict[b]]+=1 #선물 준 사람껑 체크
        giftsfield[friendsdict[a]][friendsdict[a]]+=1 #준사람 선물 지수 증가
        giftsfield[friendsdict[b]][friendsdict[b]]-=1 #받은사람 선물 지수 감
    maxanswer=0
    for i in range(len(giftsfield)):
        answer=0
        for j in range(len(giftsfield[i])):
            if i!=j:
                if giftsfield[i][j]>giftsfield[j][i]:
                    answer+=1
                if giftsfield[i][j]==giftsfield[j][i]:
                    if giftsfield[i][i]>giftsfield[j][j]:
                        answer+=1
        if answer>maxanswer:
            maxanswer=answer
           
    return maxanswer

