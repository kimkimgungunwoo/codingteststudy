'''
    고장난 리모콘의 버튼을 최소한으로 눌러서 원하는 채널까지 움직이게 하는 코드
 
    
    목표 번호에서 근처로 탐색->가능한 채널 찾고->이동 횟수 체크
    

    
    '''
    
import math
def check_can(ccN, bblist):
    if ccN==0:
        if 0 in bblist:
            return False
        else:
            return True
    if ccN<0:
        return False
    tempN = ccN
    while tempN >=1:
        last_digit = tempN % 10
        if last_digit in bblist:
            return False
        else:
            tempN //= 10  # 정수 나눗셈으로 변경
    return True

def cnt_Nbutton(ccN):
    tempN=ccN
    cnt=0
    if ccN==0:
        cnt+=1
    while tempN>=1:
        tempN/=10
        cnt+=1
        
    return cnt
    


def check_canC():
    dN=N
    uN=N
    while(True):
        if(check_can(dN,bblist)==True):
            return dN
        else:
            dN-=1
                
        if(check_can(uN,bblist)==True):
            return uN
        else:
            uN+=1
        
    
    
N=int(input())
c=int(input())
if c==10:
    bblist=list(map(int,input().split()))
    print(abs(N-100))
else:
        
    if c!=0:
        bblist=list(map(int,input().split()))
    else :
        bblist=[]

    canc=check_canC()
    print(min(cnt_Nbutton(canc)+abs(canc-N),abs(N-100)))

    
    
