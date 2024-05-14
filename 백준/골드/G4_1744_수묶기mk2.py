'''
규칙이 어떻게 되징

1. 음의정수, 0, 양의정수 구분해서 담기
2.음의정수개수생각->최대한 양의 정수가 되게, 안되면 0이랑 곱해서
3.
'''
import sys
input=sys.stdin.readline
PIntegerList=[]
NIntegerList=[]
cntz=0
ans=0
N=int(input())
for _ in range(N):
    a=int(input())
    if a==0:
        cntz+=1
    if a<0:
        NIntegerList.append(a)
    if a>0:
        PIntegerList.append(a)
NIntegerList.sort()
PIntegerList.sort()
while NIntegerList:
    if len(NIntegerList)>=2:
        ans+=NIntegerList.pop(0)*NIntegerList.pop(0)
    else:
        if cntz>0:
            NIntegerList.pop()
            cntz-=1
        else:
            ans+=NIntegerList.pop()

while PIntegerList:
    if len(PIntegerList)>=2:
        b=PIntegerList.pop()
        c=PIntegerList.pop()
        if c!=1 and b!=1:
            ans+=b*c
        else:
            ans+=b+c+sum(PIntegerList)
            PIntegerList=[]

    else:
        ans+=PIntegerList.pop()
print(ans)
    
        