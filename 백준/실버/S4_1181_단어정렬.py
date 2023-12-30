N=int(input())
oldinputlist=[]
for i in range(N):
    oldinputlist.append(input())
oldinputlist=list((set(oldinputlist)))
oldinputlist=sorted(oldinputlist,key=lambda x: (len(x),x))
for i in range(len(oldinputlist)):
    print(oldinputlist[i])