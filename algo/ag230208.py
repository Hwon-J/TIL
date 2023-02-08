# 백준11659. 구간합 구하기
# 책에서 추천하는 방식 (시간초과)
n,m=map(int,input().split())
lst=list(map(int, input().split()))
summ=[0]
temp=0
for i in lst:
    temp+=i
    summ.append(temp)

for i in range(m):
    a,b=map(int, input().split())
    print(summ[b]-summ[a-1])


#처음에 푼 방식: 시간초과로 통과 불가
n,m=map(int,input().split())
lst=list(map(int, input().split()))
arr=[list(map(int, input().split())) for _ in range(m)]
def getsum(x,y):
    summ=0
    for i in range(x-1,y):
        summ+=lst[i]
    return summ

for j in range(m):
    ret=getsum(arr[j][0],arr[j][1])
    print(ret)