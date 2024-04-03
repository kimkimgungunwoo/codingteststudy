
'''
1.연산자에서 우선순위가 큰거 위에 작은게 올라오면 밑에 있는 애들 모두 반환되어야함
2.괄호의 경우,스택속에 있는 모든 애들이 반환되어야함
3.여는괄호와 그 옆쪽은 분리되어야함
4.닫는괄호가 나오면 그 사이에 있는 모든 스택 요소들이 반환됨
((A*B+D)*(F+G))*H
AB*D+FG+*H*

A*(B+c)=>ABC+*
A*B*(C+D)=>AB*CD+*
(A*B+C)*(D+G+H)*(R*H+Y)
AB*C+DG+H*RH*Y+*
'''
def clear(answer,stack,inp):
    string=answer
    while len(stack)>0 and ddict[stack[-1]]<=ddict[inp]:
        st=stack[-1]
        if st!="(":
            string+=stack.pop()
        else:
            if inp==")":
                stack.pop()
            break
        
    return string
 
 
ddict={"+":2,"-":2,"*":1,"/":1,"(":0,")":4}
M=input()
answer=""
stack=[]
for i in range(len(M)):
    if M[i] not in ddict:
        answer+=M[i]
    else:
        if len(stack)>0 :
            if ddict[stack[-1]]>ddict[M[i]]:
                stack.append(M[i])
            else:
                answer=clear(answer,stack,M[i])
                if M[i]!=")":
                    stack.append(M[i])
        else:
            stack.append(M[i])
while len(stack)>0:
    answer+=stack.pop()
    
print(answer)
'''
A+B+C
A*(B+C)
A+B*C-D/E
'''
    
    

