

S=input()
int_list=[]
int_list.append(int(S[0]))
for i in range(1,len(S)):
    if S[i]!=S[i-1]:
        int_list.append(int(S[i]))
if (int_list.count(1)<int_list.count(0)):
    print(int_list.count(1))
else:
    print(int_list.count(0))

    