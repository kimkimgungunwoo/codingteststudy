N=int(input())
answerlist=[]
for i in range(N):
    ScoreList=list(map(int,input().split()))
    ScoreList.pop(0)
    lagap=0
    sorScore=sorted(ScoreList)
    for i in range(len(sorScore)-1):
        lagap=max(lagap,sorScore[i+1]-sorScore[i])
    answerlist.append([max(ScoreList),min(ScoreList),lagap])
for i in range(N):
    
    
    print(f"Class {i+1}")
    print(f"Max {answerlist[i][0]}, Min {(answerlist[i][1])}, Largest gap {answerlist[i][2]}")