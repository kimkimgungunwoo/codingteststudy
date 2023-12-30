'''
1.새로운 리스트 만들고
2.원래 숫자 넣고
3.전 숫자랑 현숫자가 다르면 바뀐숫자 넣기
4.둘중 더 적은거 넣으면 되자나



'''

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

    