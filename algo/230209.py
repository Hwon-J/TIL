#백준11660. 구간합구하기
n,m=map(int, input().split())
arr=[list(map(int,input().split())) for _ in range(n)]
lst=[list(map(int,input().split())) for _ in range(m)]
def ans(x1,y1,x2,y2):
    summ=0
    for i in range(x1-1,x2):
        for j in range(y1-1,y2):
            summ+=arr[i][j]
    return summ

for i in range(m):
    ret=ans(lst[i][0],lst[i][1],lst[i][2],lst[i][3])
    print(ret)
