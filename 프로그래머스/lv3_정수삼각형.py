'''
dp를 어떻게 쓰지? 
일단 max이용하면 되긴함

생각은 안어려운데 구현이..

'''

triangle=[[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]

def solution(triangle):
    field=[[triangle[0][0]]]
    for i in range(len(triangle)-1):
        field.append([0]*(i+2))
        for j in range(len(triangle[i])):
            field[i+1][j]=max(field[i+1][j],field[i][j]+triangle[i+1][j])
            field[i+1][j+1]=max(field[i+1][j+1],field[i][j]+triangle[i+1][j+1])
    
    return max(field[len(triangle)-1])

print(solution(triangle))
            
            
        