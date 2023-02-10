#백준 10986
n,m=map(int, input().split())
lst=list(map(int, input().split()))
summ=[0]*n
cnt=[0]*m
summ[0]=lst[0]
ans=0
for i in range(1,n):
    summ[i]=summ[i-1]+lst[i]

for i in range(n):
    remainer=summ[i]
    if remainer==0:
        ans+=1
    cnt[remainer]+=1

for i in range(m):
    if cnt[i]>1:
        ans+=(cnt[i]*(cnt[i]-1)//2)
print(ans)