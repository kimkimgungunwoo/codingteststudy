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