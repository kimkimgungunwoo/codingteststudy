'''
앞자리가 최대한 커야햠

맨 앞부터 배열에 담으며 더 큰 숫자가 오면 지우고 cnt+1 -> cnt가 N이 될때가지 이어짐
->숫자 남으면 맨뒤 애들 지우기

'''                             
cnt=0
N,K=map(int,input().split())
strint=input()
strintindex=0
stacksize=0
answer=[]
while cnt<K and strintindex<len(strint):
    if len(answer)==0:
        answer.append(int(strint[strintindex]))
        strintindex+=1
    else:
        if answer[-1]<int(strint[strintindex]):
            answer.pop()
            cnt+=1
        else:
            answer.append(int(strint[strintindex]))
            strintindex+=1
if cnt<K:
    for i in range(K-cnt):
        answer.pop()
if strintindex<len(strint):
    for i in range(strintindex,len(strint)):
        answer.append(int(strint[i]))
print(int(''.join(map(str,answer))))