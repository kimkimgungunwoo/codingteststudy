'''
소문자/대문자관련해서생각하장->사전순배열->첫번째 글자끼리 비교
대문자-대문자/대-소/소-소 개수 세놓는게 좋으려나?
소문자 개수 관련해서 생각해놓고 시작
1.소수사이에 많이
2.대-소 사이에 많이
3.남는건 맨뒤쪽에 넣는게?
한바퀴 삥 돌고 남는 애들은 뒤에 우겨넣을까?
'''
import sys
N,M=map(int,sys.stdin.readline().split())
strlist=['']*N
strl=0
for i in range(N):
    strlist[i]=sys.stdin.readline().rstrip()
    strl+=len(strlist[i])
    
need_under=M-strl
answer=""
over_under=need_under%(N-1)
for i in range(N-1):
    if strlist[i+1]>='a' and over_under>0:
        strlist[i]+="_"*(int((need_under/(N-1))+1))
        over_under-=1
    else:
        strlist[i]+="_"*(int(need_under/(N-1)))

while over_under>0 and i>0:
    if strlist[i].count("_")==int((need_under/(N-1))):
        strlist[i]+="_"
        over_under-=1
    i-=1
answer=''.join(strlist)    
print(answer)
    

