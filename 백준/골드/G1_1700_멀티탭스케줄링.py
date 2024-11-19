'''
N==1 이상황도 생각해야지

'''
import sys
input=sys.stdin.readline
line_index=0
N,K=map(int,input().split())
inputlist=list(map(int,input().split()))
devicelist=[[]for x in range(K+1)]
answer_list=[-1]*(K)
answer=0
line_device_cnt=[0]*(N)#각 라인당 사용해야할 디바이스 몇개 남았는지
line_used_device_cnt=[0]*N
line_last_use_device=[0]*(N) #답 구할때 최근에 무슨 콘센트에 무슨 기기 꽂았는지 기록

for i in range(len(inputlist)):
    devicelist[inputlist[i]].append(i)
    
for i in range(len(inputlist)):
    min_use_cnt=min(line_device_cnt)
    if line_device_cnt.count(min_use_cnt)>1:
        
    else:
        line_index=line_device_cnt.index(min_use_cnt)
    if answer_list[i]==-1:
        if max(line_device_cnt)==0:
            line_index=(line_index+1)%N
        for j in devicelist[inputlist[i]]:
            line_device_cnt[line_index]+=1
            answer_list[j]=line_index
    line_device_cnt[line_index]-=1
    
for i in range(len(answer_list)):
    if line_last_use_device[answer_list[i]]==0:
        line_last_use_device[answer_list[i]]=inputlist[i]
    else:
        if inputlist[i]!=line_last_use_device[answer_list[i]]:
            answer+=1
            line_last_use_device[answer_list[i]]=inputlist[i]
        
print(answer)
    
    



    
    





