from itertools import combinations,product

def solution(dice):
    n=len(dice)
    adice=[]
    rst=[]
    cases=list(combinations(range(n),n//2))
    
    
    for case in cases:
        dices=[dice[x] for x in case]
        sums=sorted([sum(x) for x in product(*dices)])
        adice.append(sums)
    
    m,e=0,len(adice)
    for i in range(e):
        bdice=adice[e-i-1]
        tmp=0
        
        for index in adice[i]:
            start=0
            end=len(bdice)-1
            while start<=end:
                mid=(start+end)//2
                if bdice[mid]<index:
                    start=mid+1
                else:
                    end=mid-1
            tmp+=start
        
        if m<tmp:
            m=tmp
            answer=[x+1 for x in cases[i]]
            
    
    return answer