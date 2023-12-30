'''
1.일단 첫번째수의 맨끝둘 0으로 교체
2.나누어 떨어지는지 확인  
    1.나누어 떨어지지 않을시 값-나머지 값 프린트
'''



N=int(input())
N=N-N%100
F=int(input())
if N%F==0:
    answer="00"
else:
    answer=str(F-N%F)
    if len(answer)==1:
        answer="0"+answer

print(answer)