# # swea 우주선 착륙 2
# T=int(input())
# for test_case in range(1,T+1):
#     N,M=map(int, input().split())
#     lst=[list(map(int, input().split())) for _ in range(N)]
#
#     directy=[0,0,1,-1,1,-1,1,-1]
#     directx=[1,-1,0,0,1,-1,-1,1]
#
#     def ans(i,j):
#         cnt=0
#         for k in range(8):
#             dy=i+directy[k]
#             dx=j+directx[k]
#             if 0<=dy<N and 0<=dx<M:
#                 if lst[i][j]> lst[dy][dx]:
#                     cnt+=1
#         if cnt>=4:
#             return 1
#         else:
#             return 0
#
#     ret=0
#     for i in range(N):
#         for j in range(M):
#             ret+=ans(i,j)
#     print(f'#{test_case} {ret}')
#
# # swea 그래프 경로
# T=int(input())
# for test_case in range(1,T+1):
#     # V: 노드 개수, E:간선개수
#     V,E=map(int, input().split())
#     # 간선경로
#     arr=[list(map(int, input().split())) for i in range(E)]
#     # S: 시작노드, G: 도착노드
#     S,G=map(int, input().split())
#     # 인접행렬 만들 리스트
#     lst=[[0]*(V+1) for _ in range(V+1)]
#     used=[0]*(V+1)
#     for i in range(E):
#         lst[arr[i][0]][arr[i][1]]=1
#     flag=0
#     def ans(now):
#         global flag
#         if now==G:
#             flag=1
#
#         for i in range(V+1):
#             if lst[now][i]==1 and used[i]==0:
#                 used[i]=1
#                 ans(i)
#                 used[i]=0
#
#     used[S] = 1
#     ans(S)
#
#     if flag:
#         print(f'#{test_case} {1}')
#     else:
#         print(f'#{test_case} {0}')
#
#
# # swea 거듭제곱
# T=10
# for test_case in range(1,T+1):
#     _ = input()
#     N,M=map(int, input().split())
#
#     def ans(level,rlt):
#         if level==M:
#             print(f'#{test_case} {rlt}')
#             return
#
#         ans(level+1,rlt*N)
#
#     ans(0,1)
#
#
# # SWEA 괄호검사
# T=int(input())
# for test_case in range(1,T+1):
#     lst=list(input())
#     stack=[]
#     for i in lst:
#         if i=='(' or i=='{':
#             stack.append(i)
#         elif i==')' or i=='}':
#         # 만약 stack의 길이가 0이고 바로 닫는괄호를 발견하여 break를하면
#         # 마지막에 과정이 완료되어 길이가 0인지 문제가 되어 길이가 0인지
#         # 구분할 수 없다.
#             if len(stack)==0:
#                 stack.append(i)
#                 break
#             elif stack[-1]=='(' and i==')':
#                 stack.pop()
#             elif stack[-1]=='{' and i=='}':
#                 stack.pop()
#             else:
#                 stack.append(i)
#                 break
#
#     if len(stack)==0:
#         print(f'#{test_case} 1')
#     else:
#         print(f'#{test_case} 0')
#
# # swea forth
#
# T=int(input())
# for test_case in range(1,T+1):
#     lst=list(input().split())
#     stack=[]
#
#     for i in range(len(lst)):
#         if lst[i].isdigit():
#             stack.append(int(lst[i]))
#         elif lst[i]=='+' or lst[i]=='-' or lst[i]=='*' or lst[i]=='/':
#             if len(stack)>=2:
#                 b=stack.pop()
#                 a=stack.pop()
#                 if lst[i]=='+':
#                     stack.append(a+b)
#                 elif lst[i]=='-':
#                     stack.append(a-b)
#                 elif lst[i]=='*':
#                     stack.append(a*b)
#                 elif lst[i]=='/':
#                     # 나눗셈의 경우 항상 나누어 떨어진다의 의미가
#                     # 나누어 떨어지지 않는 경우 error처리 하는 것이 아니라
#                     # 몫만 필요하다는 의미
#                     stack.append(a//b)
#
#             else:
#                 print(f'#{test_case} error')
#                 break
#
#         if lst[i]=='.':
#             if len(stack)!=1:
#                 print(f'#{test_case} error')
#             else:
#                 print(f'#{test_case} {stack[-1]}')
#
#
# # swea 미로찾기
# # 문자열 아니면 인식안해서 런타임 에러 남
# import sys
# sys.stdin = open("sample_input(8).txt","r")
# T=int(input())
# for test_case in range(1,T+1):
#     N=int(input())
#     arr=[list(input()) for _ in range(N)]
#     visit=[[0]*N for _ in range(N)]
#     directy=[0,0,-1,1]
#     directx=[1,-1,0,0]
#     flag=0
#     def ans(i,j):
#         global flag
#         for k in range(4):
#             dy=i+directy[k]
#             dx=j+directx[k]
#
#             if 0<=dy<N and 0<=dx<N and visit[dy][dx] ==0:
#                 visit[dy][dx]=9
#                 if arr[dy][dx]=='3':
#                     flag=1
#                 elif arr[dy][dx]=='0':
#                     ans(dy, dx)
#                     visit[dy][dx] = 0
#
#     for i in range(N):
#         for j in range(N):
#             if arr[i][j]=='2':
#                 ans(i,j)
#                 visit[i][j]=9
#     if flag:
#         print(f'#{test_case} 1')
#     else:
#         print(f'#{test_case} 0')
#
#
# # swea 배열 최소 합
# T=int(input())
# for test_case in range(1,T+1):
#     N=int(input())
#     arr=[list(map(int, input().split())) for _ in range(N)]
#     used=[0]*N
#     minn=21e8
#
#     def ans(level,summ):
#         global minn
#
#         if level==N:
#             if summ<minn:
#                 minn=summ
#             return
#         if summ>minn:
#             return
#
#         for i in range(N):
#             if used[i]==0:
#                 used[i]=1
#                 ans(level+1,summ+arr[level][i])
#                 used[i]=0
#     ans(0,0)
#
#
#     print(f'#{test_case} {minn}')