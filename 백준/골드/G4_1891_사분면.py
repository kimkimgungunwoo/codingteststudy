
import math
def DotControll_x(M_l,value,index):
    if M_l[0]==-1:
        return 
    ulist=[2,1]
    dlist=[3,4]
    cnt=0
    if M_l[index] in ulist:
        dot_x_index=ulist.index(M_l[index])
        if value>0:
            M_l[index]=ulist[(dot_x_index+abs(value))%2]
            cnt=(dot_x_index+value)//2
        else:
            M_l[index]=ulist[(dot_x_index+value)%2]    
            cnt=(dot_x_index+value)//2
        
    if M_l[index] in dlist:
        dot_x_index=dlist.index(M_l[index])
        if value>0:
            M_l[index]=dlist[(dot_x_index+abs(value))%2]
            cnt=(dot_x_index+value)//2
        else:
            M_l[index]=dlist[(dot_x_index+value)%2]    
            cnt=(dot_x_index+value)//2   
        
                    
    if index==0:
        if cnt!=0:
            M_l[0]=-1
            return
        else:
            return
    DotControll_x(M_l,cnt,index-1)
            
def DotControll_y(M_l,value,index):
    if M_l[0]==-1:
        return 
    llist=[3,2]
    rlist=[4,1]
    cnt=0
    if M_l[index] in llist:
        dot_y_index=llist.index(M_l[index])
        if value>0:
            M_l[index]=llist[(dot_y_index+abs(value))%2]
            cnt=(dot_y_index+value)//2
        else:
            M_l[index]=llist[(dot_y_index+value)%2]    
            cnt=(dot_y_index+value)//2
        
    if M_l[index] in rlist:
        dot_y_index=rlist.index(M_l[index])
        if value>0:
            M_l[index]=rlist[(dot_y_index+abs(value))%2]
            cnt=(dot_y_index+value)//2
        else:
            M_l[index]=rlist[(dot_y_index+value)%2]    
            cnt=(dot_y_index+value)//2
    if index==0:
        if cnt!=0:
            M_l[0]=-1
            return
        else:
            return
    DotControll_y(M_l,cnt,index-1)

    
N,M=map(int,input().split())
M_l=[int(char) for char in str(M) ]
x,y=map(int,input().split())
DotControll_x(M_l,x,N-1)
DotControll_y(M_l,y,N-1)
if M_l[0]==-1:
    print(-1)
else:
    print(int(''.join(map(str,M_l))))