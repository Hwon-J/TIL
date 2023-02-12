# # swea 파리퇴치
# T = int(input())
# for test_case in range(1, T + 1):
#     n, m =map(int,input().split())
#     lst=[list(map(int,input().split())) for _ in range(n)]
#
#     def ans(i,j):
#         summ=0
#         for y in range(m):
#             for x in range(m):
#                 summ+=lst[i+y][j+x]
#         return summ
#
#     maxx=0
#     for i in range(n-m+1):
#         for j in range(n-m+1):
#             ret=ans(i,j)
#             if ret>maxx:
#                 maxx=ret
#     print(maxx)
#
#
# # 백준 색종이
# n= int(input())
# paper=[[0]*100 for _ in range(100)]
# for k in range(n):
#     a,b= map(int, input().split())
#     for i in range(10):
#         for j in range(10):
#             paper[a+i][b+j]=1
#
# cnt=0
# for i in range(100):
#     for j in range(100):
#         if paper[i][j]==1:
#             cnt+=1
# print(cnt)
#
# # swea 구간합
#
# T = int(input())
# for test_case in range(1, T + 1):
#     n, m=map(int, input().split())
#     lst=list(map(int, input().split()))
#     maxx = 0
#     minn = 21e8
#     for i in range(n-m+1):
#         summ = 0
#         for j in range(m):
#             summ+=lst[i+j]
#         if summ>maxx:
#             maxx=summ
#         if summ<minn:
#             minn=summ
#     print(f'#{test_case} {maxx-minn}')
#
# # swea 숫자카드
# T = int(input())
# for test_case in range(1, T + 1):
#     n=int(input())
#     lst=list(map(int, input()))
#     bucket=[0]*10
#     for i in range(len(lst)):
#         bucket[lst[i]]+=1
#     maxx=0 # 가장 큰 숫자 카드
#     max_num=0   # 가장 많은 숫자카드 장수
#     # 가장 많은 카드 장수를 찾기 위해 bucket리스트 숫자가 가장 큰 것을 찾음
#     for i in range(10):
#         if bucket[i]>max_num:
#             max_num=bucket[i]
#     # 카드 장 수가 동일하다면 더 큰 수를 출력
#     # 같은 장수인 숫자카드를 넣을 빈리스트 만들기
#     new=[]
#     for i in range(10):
#         if bucket[i]==max_num:
#             new.append(i)
#     # 작은 수부터 리스트에 담기므로 뒤에서 첫번쨰가 가장 큰수
#     maxx=new[-1]
#     print(f'#{test_case} {maxx} {max_num}')
#
#
# # swea max min
# T = int(input())
# for test_case in range(1, T + 1):
#     n=int(input())
#     lst=list(map(int, input().split()))
#     maxx=0
#     minn=21e8
#     for i in range(n):
#         if lst[i] > maxx:
#             maxx=lst[i]
#         if lst[i]< minn:
#             minn=lst[i]
#     print(maxx-minn)
#
# # swea 델타검색
# T = 1
# for test_case in range(1, T + 1):
#     n=int(input())
#     arr=[list(map(int, input().split())) for _ in range(n)]
#     dy=[1,-1,0,0]
#     dx=[0,0,1,-1]
#     def ans(i,j):
#         summ=0
#         for k in range(4):
#             if 0<= i+dy[k] <n and 0<= j+dx[k] <n:
#                 summ+=abs(arr[i+dy[k]][j+dx[k]]-arr[i][j])
#         return summ
#
#     ret=0
#     for i in range(n):
#         for j in range(n):
#             ret+=ans(i,j)
#
#     print(f'{test_case} {ret}')
#
# # swea 이진탐색
# T = int(input())
# for test_case in range(1, T + 1):
#     # ed: 총 페이지 수, a: a가 찾을, b: b가 찾을
#     ed,a,b=map(int, input().split())
#     def ans(st,ed,r):
#         cnt=0
#         while 1:
#             mid=(st+ed)//2
#             if r==mid:
#                 cnt+=1
#                 break
#             elif r > mid:
#                 st=mid
#                 cnt+=1
#             elif r < mid:
#                 ed=mid
#                 cnt+=1
#         return cnt
#
#     ret1=ans(1,ed,a)     # a의 cnt
#     ret2=ans(1,ed,b)
#
#     if ret1==ret2:
#         print(f'#{test_case} 0')
#     if ret1 > ret2:
#         print(f'#{test_case} B')
#     if ret1 < ret2:
#         print(f'#{test_case} A')
#
# # 색칠하기
# T = int(input())
# for test_case in range(1, T + 1):
#     arr=[[0]*10 for _ in range(10)]
#     n=int(input())  # 색칠할 영역 개수
#     lst=[list(map(int, input().split())) for _ in range(n)]
#
#     def ans(x1,y1,x2,y2,color):
#         for i in range(x1,x2+1):
#             for j in range(y1,y2+1):
#                 arr[i][j]+=color
#
#     for i in lst:
#         ret=ans(i[0],i[1],i[2],i[3],i[4])
#     cnt=0
#     for i in range(10):
#         for j in range(10):
#             if arr[i][j]>=3:
#                 cnt+=1
#     print(f'#{test_case} {cnt}')
#
# # swea Sum
# T = 10
# for test_case in range(1, T + 1):
#     input()
#     lst=[list(map(int, input().split())) for _ in range(100)]
#     maxx=0
#     for i in range(100):
#         summ1=0
#         summ2=0
#         for j in range(100):
#             summ1+=lst[i][j]
#             if summ1> maxx:
#                 maxx=summ1
#             summ2+=lst[j][i]
#             if summ2>maxx:
#                 maxx=summ2
#     summ3=0
#     summ4=0
#     for i in range(100):
#         summ3+=lst[i][i]
#         if summ3>maxx:
#             maxx=summ3
#
#         summ4 += lst[i][100-i-1]
#         if summ4 > maxx:
#             maxx=summ4
#     print(f'#{test_case} {maxx}')
#
# # swea flatten
# T = 10
# for test_case in range(1, T + 1):
#     n=int(input())
#     lst=list(map(int, input().split()))
#     mxidx=0
#     mnidx=0
#     while n>=0:
#         mx=0
#         mn=100
#         for i in range(100):
#             if lst[i]>mx:
#                 mx=lst[i]
#                 mxidx=i
#             if lst[i]<mn:
#                 mn=lst[i]
#                 mnidx=i
#         lst[mxidx]-=1
#         lst[mnidx]+=1
#         n-=1
#     maxx=0
#     minn=100
#     for i in range(100):
#         if lst[i]>maxx:
#             maxx=lst[i]
#         if lst[i]<minn:
#             minn=lst[i]
#     print(f'{test_case} {maxx-minn}')
#
# # swea 파리퇴치3
# #import sys
# #sys.stdin = open("in1.txt", "r")
# T = int(input())
# for test_case in range(1, T + 1):
#     n, m = map(int, input().split())
#     lst = [list(map(int, input().split())) for _ in range(n)]
#     da = [-1, 1, 0, 0]
#     db = [0, 0, -1, 1]
#     dc = [-1, -1, 1, 1]
#     dd = [-1, 1, -1, 1]
#
#     def ans(i, j):
#         summ = lst[i][j]
#         for y in range(4):
#             for z in range(1, m):
#                 dx = i + da[y] * z
#                 dy = j + db[y] * z
#                 if 0 <= dx < n and 0 <= dy < n:
#                     summ += lst[dx][dy]
#         return summ
#
#     def ans2(i, j):
#         summ = lst[i][j]
#         for y in range(4):
#             for z in range(1, m):
#                 dq = i + dc[y] * z
#                 dw = j + dd[y] * z
#                 if 0 <= dq < n and 0 <= dw < n:
#                     summ += lst[dq][dw]
#         return summ
#
#     maxx = 0
#     for i in range(n):
#         for j in range(n):
#             ret = ans(i, j)
#             ret2 = ans2(i, j)
#             if ret>maxx:
#                 maxx=ret
#             if ret2>maxx:
#                 maxx=ret2
#     print(f'#{test_case} {maxx}')
#
# # swea 특별한 정렬
# T = int(input())
# for test_case in range(1, T + 1):
#     n = int(input())
#     lst = list(map(int, input().split()))
#     # 정렬
#     for i in range(len(lst)-1):
#         for j in range(len(lst)-1-i):
#             if lst[j]>lst[j+1]:
#                 lst[j], lst[j + 1] =lst[j +1],lst[j]
#     new=[]
#     if len(lst)%2:
#         cnt=0
#         for i in range((len(lst)//2)+1):
#             new.append(lst[-1-i])
#             cnt+=1
#             if cnt==len(lst):
#                 break
#             new.append(lst[i])
#     else:
#         for i in range(len(lst)//2):
#             new.append(lst[-1-i])
#             new.append(lst[i])
#
#     rlt = ' '.join(map(str, new[:10]))  # 리스트의 요소들만 뽑기 (최대 10개)
#     print(f'#{test_case} {rlt}')
#
# # swea 다솔이의 다이아몬드 장식
# # import sys
# # sys.stdin = open("sample_input.txt", "r")
# T = int(input())
# for test_case in range(1, T + 1):
#     a=input()
#     arr=[['.']*((4*len(a))+1) for _ in range(5)]
#     for i in range(2, (4*len(a))+1, 4):
#         arr[0][i]='#'
#         arr[4][i]='#'
#     for i in range(1,(4*len(a))+1, 2):
#         arr[1][i] = '#'
#         arr[3][i] = '#'
#     for i in range(0, (4*len(a))+2, 4):
#         arr[2][i] = '#'
#     n=0
#     for i in range(2, (4*len(a))+1, 4):
#         arr[2][i] = a[n]
#         n+=1
#
#     for i in arr:
#         print(*i, sep='')
#
# # swea 숫자회전
# T = int(input())
# for test_case in range(1, T + 1):
#     n=int(input())
#     lst= [list(input().split()) for _ in range(n)]
#     ar90 = [[0] * n for _ in range(n)]
#     ar180 = [[0] * n for _ in range(n)]
#     ar270 = [[0] * n for _ in range(n)]
#     for i in range(n):
#         for j in range(n):
#             ar90[i][j]=lst[n-1-j][i]
#             ar180[i][j]=lst[n-i-1][n-j-1]
#             ar270[i][j]=lst[j][n-i-1]
#     print(f'#{test_case}')
#     for i in range(n):
#         for j in range(n):
#             print(ar90[i][j], end='')
#         print(end=' ')
#         for j in range(n):
#             print(ar180[i][j], end='')
#         print(end=' ')
#         for j in range(n):
#             print(ar270[i][j], end='')
#         print()

