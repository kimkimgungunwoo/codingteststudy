s=input()
ls=len(s)
cnt=0
header=0
index_l=0
index_r=ls-1

while index_l<=index_r:
    if s[index_l]==s[index_r]:
        index_l+=1
        index_r-=1
    else:
        header+=1
        cnt+=1
        index_l=header
        index_r=ls-1
print(len(s)+cnt)
        
        


