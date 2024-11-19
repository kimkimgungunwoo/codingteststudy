'''
그래프?
->각 리스트의 시작점에는 현재 진행중인 상담의 종료시간,유형 pair로?

그리디 느낌인데

1.시작시간이 의미가 있나?

k,n->크지않음->n^3까지도 괜찮을듯

브루트 포스 접근하듯이 해야하지않나,
유형끼리 영향을 주고받진 않으니까 유형하나씩만 보게해도될듯

총시간->알빠노->대기시간이 더 중요함
상담원이 어떤 유형을맡을지일단 그래프 형식으로 하나의 유형에 붙은 애들 정리
상담원 애들 나눠주고 추가로 필요한애들 존재확인
->상담원을 어떻게 나눠줄지가 메인이네

1.총 대기시간 구하는 함수
2.상담원 보내고 나서 어떻게 업무를 나눠줄지 ㅁㅇㄴㄹ

'''

# def solution(k, n, reqs):
    
#     def check_wating_time(lst):
#         time=0
#         waiting=0
#         for i in lst:
#             if time>i[0]:
#                 waiting+=time-i[0]
#             if time<=i[0]:
#                 time=i[0]
#             time+=i[1]
#         return waiting
        
#     def agent_assignment(index):
#         waiting_time=[0]*agent_list[index]
#         timelist=[0]*agent_list[index]
#         for i in range(len(waiting_list[index])):
#             minindex=0
#             minwaititme=1e9
#             for j in range(len(timelist)):
#                 if timelist[j]<minwaititme:
#                     minwaititme=timelist[j]
#                     minindex=j
#             if timelist[minindex]<=waiting_list[index][i][0]:
#                 timelist[minindex]=waiting_list[index][i][0]
#             else:
#                 waiting_time[minindex]+=timelist[minindex]-waiting_list[index][i][0]
#             timelist[minindex]+=waiting_list[index][i][1]
            
#         return sum(waiting_time)     
                
                    

#     waiting_list=[[] for x in range(k)]
#     for i in reqs:
#         waiting_list[i[2]-1].append([i[0],i[1]])
#     agent_list=[1]*k
#     answer = 0
#     n-=k
#     waiting_time=[check_wating_time(waiting_list[x]) for x in range(k)]
#     while n>0:
#         max_decreased_time=0
#         max_index=0
#         for i in range(k):
#             agent_list[i]+=1
#             fixed_time=agent_assignment(i)
#             print(fixed_time)
#             decreased_time=waiting_time[i]-fixed_time
#             if max_decreased_time<decreased_time:
#                 max_decreased_time=decreased_time
#                 max_index=i
#             agent_list[i]-=1
#         agent_list[max_index]+=1
#         waiting_time[max_index]=fixed_time
#         n-=1
#         print(max_index)

        
#     answer=sum(waiting_time)
        
        
    
#     return answer
def solution(k, n, reqs):
    
    def check_wating_time(lst):
        time=0
        waiting=0
        for i in lst:
            if time>i[0]:
                waiting+=time-i[0]
            if time<=i[0]:
                time=i[0]
            time+=i[1]
        return waiting
        
    def agent_assignment(index):
        waiting_time=[0]*agent_list[index]
        timelist=[0]*agent_list[index]
        for i in range(len(waiting_list[index])):
            minindex=0
            minwaititme=1e9
            for j in range(len(timelist)):
                if timelist[j]<minwaititme:
                    minwaititme=timelist[j]
                    minindex=j
            if timelist[minindex]<=waiting_list[index][i][0]:
                timelist[minindex]=waiting_list[index][i][0]
            else:
                waiting_time[minindex]+=timelist[minindex]-waiting_list[index][i][0]
            timelist[minindex]+=waiting_list[index][i][1]
            
        return sum(waiting_time)    
                
                    

    waiting_list=[[] for x in range(k)]
    for i in reqs:
        waiting_list[i[2]-1].append([i[0],i[1]])
    agent_list=[0]*k
    answer = 0
    for i in range(k):
        n-=1
        agent_list[i]=1
    waiting_time=[check_wating_time(waiting_list[x]) for x in range(k)]
    while n > 0:
        max_decrease = -float('inf')
        best_index = -1

        for i in range(k):
            agent_list[i] += 1
            new_waiting_time = agent_assignment(i)
            decrease = waiting_time[i] - new_waiting_time
            
            
            if decrease > max_decrease:
                max_decrease = decrease
                best_index = i
            
            agent_list[i] -= 1
        
        agent_list[best_index] += 1
        waiting_time[best_index] = agent_assignment(best_index)
        n -= 1

        
        
        
    
    return sum(waiting_time)




print(solution(3,5,	[[10, 60, 1], [15, 100, 3], [20, 30, 1], [30, 50, 3], [50, 40, 1], [60, 30, 2], [65, 30, 1], [70, 100, 2]]))