from collections import deque
edges=[[4, 11], [1, 12], [8, 3], [12, 7], [4, 2], [7, 11], [4, 8], [9, 6], [10, 11], [6, 10], [3, 5], [11, 1], [5, 3], [11, 9], [3, 8]]


def solution(edges):
    answer = [0, 0, 0, 0]
        
    def check(N):
        visited = set()
        queue = deque([N])

        while queue:
            N = queue.popleft()
            
            if N in visited:
                answer[1] += 1
                break 
            
            visited.add(N)
            
            if N not in field:
                answer[2] += 1
                break 
            
            if len(field[N]) == 2:
                answer[3] += 1
                break  
            
            
            queue.append(field[N][0])
        
    end_map = {}
    field = {}
    
    for i in range(len(edges)):
        if edges[i][1] not in end_map:
            end_map[edges[i][1]] = 1
        else:
            end_map[edges[i][1]] += 1
        
        if edges[i][0] not in field:
            field[edges[i][0]] = [edges[i][1]]
        else:
            field[edges[i][0]].append(edges[i][1])
    
    for i in field:
        if i not in end_map and len(field[i])>=2:
            answer[0] = i
            for j in field[i]:
                check(j)
    
    return answer

print(solution(edges))