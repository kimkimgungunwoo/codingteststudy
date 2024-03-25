'''
친구가 서로 주고받은 횟수->그래프 이용/탑색들어가서 비교
선물지수->그래프 탐색필요할듯?

그래프에서 본인꺼에는 선물지수 체크해두자



friends->친구목록-->friends*friends만큼의 2중배열
gifts분석해서 하면 될듯?


주어지는게 이름-->이름을 번호에 매핑?(딕셔너리)
아니면 이름만 가지고 하기?

가장많은 선물 받은사람의 선물 개수 
'''


def solution(friends, gifts):
    friendsdict={friends[x]:x for x in range(len(friends))}
    giftsfield=[[0 for x in range(len(friends))] for k in range(len(friends))]
    for i in range(len(gifts)):
        a=gifts[i].split()[0]
        b=gifts[i].split()[1]
        giftsfield[friendsdict[a]][friendsdict[b]]+=1 #선물 준 사람껑 체크
        giftsfield[friendsdict[a]][friendsdict[a]]+=1 #준사람 선물 지수 증가
        giftsfield[friendsdict[b]][friendsdict[b]]=-1 #받은사람 선물 지수 감
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

print(solution(["joy", "brad", "alessandro", "conan", "david"],["alessandro brad", "alessandro joy", "alessandro conan", "david alessandro", "alessandro david"],))
