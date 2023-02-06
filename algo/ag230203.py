# #swea13699.색칠하기
# T = int(input())
# for test_case in range(1, T + 1):
#     arr=[[0]*10 for _ in range(10)]
#     n=int(input())
#     ipt=[list(map(int, input().split())) for _ in range(n)]
#     def ans(k):
#         for i in range(k[0],k[2]+1):
#             for j in range(k[1],k[3]+1):
#                 arr[i][j]= arr[i][j]+k[4]

#     for k in ipt:
#         ret=ans(k)
    
#     cnt=0
#     for i in range(10):
#         for j in range(10):
#             if arr[i][j]>=3:
#                 cnt+=1
#     print(f'#{test_case} {cnt}')

# # swea 달팽이 숫자
# T = int(input())
# for test_case in range(1, T + 1):
#     n=int(input())
#     arr=[[0]*n for _ in range(n)]
#     q=1
#     for i in range()

# # swea13702. 델타 검색
# T = 10
# for test_case in range(1, T + 1):
#     n=int(input())
#     arr=[list(map(int, input().split())) for _ in range(n)]
#     di=[0,0,1,-1]
#     dj=[1,-1,0,0]

#     def ans(x,y):
#         summ=0
#         for i in range(4):
#             dx=x+di[i]
#             dy=y+dj[i]
#             if 0<=dx<n and 0<=dy<n:
#                 summ+=abs(arr[dx][dy]-arr[x][y])
#         return summ

#     rlt=0
#     for x in range(n):
#         for y in range(n):
#             rlt+=ans(x,y)
                
#     print(f'#{test_case} {rlt}')

# swea13702. Flatten
T = 10
for test_case in range(1, T + 1):
    n= int(input())
    lst=list(map( int,input().split()))
    mxidx=0
    mnidx=0
    for i in range(n):
        maxx=0
        minn=100
        for j in range(len(lst)):     
            if lst[j]>= maxx:
                maxx=lst[j]
                mxidx=j
            elif lst[j]<=minn:
                minn=lst[j]
                mnidx=j
        
        lst[mxidx]-=1
        lst[mnidx]+=1
    
    print(f'{test_case} {lst[mxidx]-lst[mnidx]}')