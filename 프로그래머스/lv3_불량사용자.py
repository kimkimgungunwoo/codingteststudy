from itertools import permutations

user_id=["frodo", "fradi", "crodo", "abc123", "frodoc"]
banned_id=["fr*d*", "abc1**"]

def solution(user_id, banned_id):
    def check(user,banned):
        if len(user)!=len(banned):
            return False
        for i in range(len(user)
                       ):
            if user[i]!=banned[i]:
                if banned[i]!="*":
                    return False
        
        return True
    
    answer=[]
    for rst in permutations(user_id,len(banned_id)):
        ch=True
        for i in range(len(banned_id)):
            if not check(rst[i],banned_id[i]):
                ch=False
            
        if ch and set(rst) not in answer:
            answer.append(set(rst))
        
    return len(answer)

print(solution(user_id,banned_id))