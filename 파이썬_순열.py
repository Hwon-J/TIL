# # 중복 순열
# # n개의 주사위를 던졌을 때 나올 수 있는 모든 경우를 출력해 주세요
# n=int(input())
# path=[0]*n # 조합을 출력하기 위한 저장소
# def ans(level):
#
#     if level==n:
#         for i in range(n):
#             print(path[i], end=' ')
#         print()
#         return
#
#     for i in range(6):
#        # 주사위의 눈은 1씩 늘어나므로 앞 숫자를 고정해두고 하나씩 1을 더해가며 변경
#         path[level]=i+1
#         ans(level+1)
#
# ans(0)
#
#
# # dice에서 n개의 카드를 뽑아가능한 조합 모두 출력하기(중복 가능)
# n=3
# dice=[1,2,3,4]
# path=[0]*n
# # used는 단방향 트리에서는 사이클이 발생하지 않으므로 사용할 필요가 없다.
# # 그러나 양방향 에서는 사이클에 따라 맴도는 것을 방지하기 위해 used를 사용한다.
# # used=[0]*4
#
# def dfs(level):
#
#     if  level==n:
#         for i in range(n):
#             print(path[i], end=' ')
#         print()
#         return
#
#     for i in range(4):
#         path[level]=dice[i]
#         dfs(level+1)
#
#
# dfs(0)
#
# # 첫번째 주사위에서 '2'가 나오지 않는 경우
# n=3
# dice=[1,2,3,4]
# path=[0]*n
# used=[0]*4
# def jg(level):
#     # 일단 다음가지에는 진입하고 난 후 만약 path의 첫번째 값이 2라면 리턴
#     if path[0]==2:
#         return
#     if level==n:
#         for i in range(n):
#             print(path[i], end=' ')
#         print()
#         return
#
#     for i in range(4):
#         # # level이 0이고(첫번째 칸이고) dice[i]==2 (들어가는 숫자가 2)이면 skip
#         # # 해당가지에 진입부터 하지 않음
#         # if level==0 and dice[i]==2: continue
#         # path[level]이 고정됨에 따라 dice의 i가 변화하여 배열을 채움
#         path[level]=dice[i]
#         jg(level+1)
#
# jg(0)
#
# # ABCD가 적혀있는 카드 3 묶음이 있습니다
# # 각 묶음에서 카드를 1장씩 뽑았을때
# # 1.c로 시작하는 경우는 다 제외하기 (생략)
# # 2.모든 경우에서 B는 제외하기
# candidates=['A','B','C','D']
# path=[' ']*len(candidates)
#
# def jg(level):
#     # 다음 가지 진입 후 리턴하기
#     # continue는 for문 안에서 사용가능
#     if path[0]=='C':
#         return
#     if 'B' in path:
#         return
#     if level==3:
#         for i in range(3):
#             print(path[i], end=' ')
#         print()
#         return
#
#     for i in range(4):
#         # 진입 안하고 제외하기
#         # if level==0 and candidates[i]=='C': continue
#         # if candidates[i]=='B': continue
#         path[level]=candidates[i]
#         jg(level+1)
#
# jg(0)
#
# # ABCD가 적혀있는 카드 3 묶음이 있습니다
# # 각 묶음에서 카드를 1장씩 뽑았을때
# # 연속해서 같은 카드를 뽑으면 않됨 !!!
# candidates=['A','B','C','D']
# path=[0]*3
#
# def ans(level):
#     # level이 2이상일때 부터 가능
#     # 만약 level을 ==2로 한정한다면 path[0]==path[1]만 비교해서
#     # path[2]==path[1]는 비교하지 않아 중복되는 경우가 생긴다.
#     if level>1 and path[level-1] == path[level -2]: return
#     if level==3:
#         for i in range(3):
#             print(path[i], end=' ')
#         print()
#         return
#     for i in range(4):
#         # level이 1일 때부터 비교해서 path[0]==candidates[i]면 continue
#         # 이전에 넣은 값과 현재 넣은 값이 같으면 continue
#         # if level>0 and (path[level-1]==candidates[i]):continue
#         path[level] = candidates[i]
#         ans(level+1)
# ans(0)
#
# #<조합>
# # ABCD가 적혀있는 카드 3 묶음이 있습니다
# # 각 묶음에서 카드를 1장씩 뽑았을때
# # path배열을 활용하여 '조합' 구현 (중복이 없음)
# candidates=['A','B','C','D']
# path=[0]*4
#
# def ans(level):
#     if level==3:
#         for i in range(3):
#             print(path[i], end=' ')
#         print()
#         return
#
#     for i in range(4):
#         # level이 1일 때부터 비교해서 path[0]==candidates[i]면 continue
#         # 이전에 넣은 값과 현재 넣은 값을 비교했을 때 앞선 글자가 더 크다면 continue
#         # 문자가 자동으로 아스키코드 값으로 계산된다.
#         if level>0 and path[level-1]>=candidates[i]: continue
#         path[level]=candidates[i]
#         ans(level+1)
# ans(0)
#
# # for문을 시작하는 i를 바꿔서 조합 구현
#
# candidates=['A','B','C','D']
# path=[0]*4
#
# def abc(level,start):
#
#     if level==3:
#         for i in range(3):
#             print(path[i], end=' ')
#         print()
#         return
#     for i in range(start,4):
#         path[level]=candidates[i]
#         abc(level+1, i+1)
# abc(0,0)

# # <dfs>
# #나는솔로
# people = ['Amy','Bob','Chloe','Diane','Edger']
#
# arr = [[0,0,1,0,1],
#        [1,0,0,0,0],
#        [0,1,0,0,0],
#        [0,1,0,0,0],
#        [0,0,0,1,0]]
# # 여기서  가장 인기가 많은 사람은 누구인지 출력
# maxx=0
# # 세로로 봤을 때 1이 가장 많은 사람
# for i in range(5):
#     cnt=0
#     for j in range(5):
#         if arr[j][i]==1:
#             cnt+=1
#     if cnt>maxx:
#         maxx=cnt
#         Idx=people[i]
#
# print(Idx)
#
# '''
# 문자를 하나 입력받아 주세요
# 그리고 입력받은 문자의 형제노드를 출력해 주세요
# 예
# A 입력시  형제없음 출력됨
# B 입력시  C 출력됨
# E 입력시  D 출력됨
# F 입력시  형제없음이 출력 됩니다 !!
# '''
#
# lst=['a','b','c','d','e','f']
# n=input()
# Idx=0   #입력받은 n의 인덱스 찾기
# root=0  #뿌리 인덱스 찾기
# arr = [[0,1,1,0,0,0],
#        [0,0,0,1,1,0],
#        [0,0,0,0,0,1],
#        [0,0,0,0,0,0],
#        [0,0,0,0,0,0],
#        [0,0,0,0,0,0]]
# #입력받은 n의 인덱스 찾기
# for i in range(6):
#     if lst[i]==n:
#         Idx=i
# # 첫번째 뿌리를 위해 flag사용
# flag=0
# #뿌리 인덱스 찾기
# for i in range(6):
#     if arr[i][Idx]==1:
#         root=i
#         flag=1  # 1인 값이 하나라도 있으면 flag=1
# # 첫번째 뿌리를 위한 식
# if flag==0:
#     print('형제없음')
# # 그외의 경우
# else:
#     bro=[]
#     # 뿌리인덱스 리스트에서 1인 형제 찾기
#     for i in range(6):
#         if arr[root][i]==1:
#             bro.append(i)
#     # 찾은 형제에서 본인 제외
#     bro.remove(Idx)
#     # 본인을 제외하고 남은 것이 없으면 형제없음
#     if len(bro) == 0:
#         print('형제없음')
#     # 있으면 형제들 출력
#     else:
#         for i in bro:
#             print(lst[i], end=' ')
#
#
# # K에서 부터 DFS 탐색하면서 탐색되는 순서를 출력해 주세요 !!
# #
# name=['K','F','C','D','M','G','A']
# # 인접행렬 만들기
# arr=[[0,1,1,1,0,0,0],
#     [0,0,0,0,1,1,0],
#     [0,0,0,0,0,0,1],
#     [0,0,0,0,0,0,0],
#     [0,0,0,0,0,0,0],
#     [0,0,0,0,0,0,0],
#     [0,0,0,0,0,0,0]]
# path=[]
#
# def ans(now):
#     global path
#     # path에 name을 하나씩 넣기
#     path.append(name[now])
#     # name의 길이만큼 for문
#     for i in range(7):
#         # 만약 now열에서 1을 찾는다면 그것으로 재귀 호출
#         if arr[now][i]==1:
#             ans(i)
#
# ans(0)
# print(*path)    #K F M G C A D
#
#
# # TREE 모양이 아닌 그래프 dfs 1번씩 탐색 순서 출력하기
# lst= ['b','a','c','d']  # b c a d
# arr=[[0,0,1,1],
#      [1,0,0,0],
#      [0,1,0,1],
#      [0,0,0,0]]
# # 탐색순서를 넣을 빈리스트 만들기
# path=[]
# # 방문여부를 확인할 used만들기
# used=[0]*4
# def ans(now):
#     global path
#     # 출발시작할 것부터 path에 추가
#     path.append(lst[now])
#     # 리스트 갯수만큼 for문 돌리기
#     for i in range(4):
#         # 탐색결과 이동이 가능한 1인 동시에 방문한적이 없는 used=0일 경우
#         if arr[now][i]==1 and used[i]==0:
#             # 방문의 의미로 1로 변경
#             used[i]=1
#             # 함수를 호출
#             ans(i)
# # 시작을 첫번째에서 하므로 used[0]을 1로 설정
# used[0]=1
# ans(0)
# print(*path)
#
#
# # 한 지점에서 다른 지점까지 갈 수 있는 경로가 몇가지 인지 출력해 주세요 ( A -> D) 4가지
# lst= ['b','a','c','d']
# arr=[[0,0,1,1],
#      [1,0,1,0],
#      [1,0,0,1],
#      [0,0,0,0]]
# # 횟수를 세어줄 cnt
# cnt=0
# used=[0]*4
#
# def ans(now):
#     global cnt
#     # 만약 now가 3이 된다면 도착지점의 인덱스가 3
#     if now==3:
#         cnt+=1
#         return
#     for i in range(4):
#         if arr[now][i]==1 and used[i]==0:
#             used[i]=1
#             ans(i)
#             # 가능한 경로의 갯수를 세는 것이므로 리턴하면서 0으로 바꿔줄 것
#             used[i]=0
# # 시작점의 인덱스 찾기
# for i in range(4):
#     if lst[i]=='a':
#         ans(i)
# print(cnt)
#
# # 한 지점에서 다른 지점까지 갈 수 있는 경로를 모두 출력해 주세요 ( A -> D)
# lst= ['b','a','c','d']
# arr=[[0,0,1,1],
#      [1,0,1,0],
#      [1,0,0,1],
#      [0,0,0,0]]
# # 경로를 넣어줄 path 생성
# path=[]
# used=[0]*4
# def ans(now):
#     global path
#     path.append(lst[now])
#     # 도착지 인덱스를 종료값으로 설정
#     if now==3:
#         # 마지막까지 오면 출력
#         print(*path)
#         return
#
#     for i in range(4):
#         if arr[now][i]==1 and used[i]==0:
#             used[i]=1
#             ans(i)
#             used[i]=0
#             # pop에서 인덱스를 생략한 경우 마지막 값을 제거
#             # path가 global로 설정되어 있어 리턴할때 임려간 값을 다시 빼주어야함
#             path.pop()
#
# for i in range(4):
#     if lst[i]=='a':
#         ans(i)
#         used[i]=1


# A=>D 까지 가는 최소비용 구하기
lst= ['b','a','c','d']
arr=[[0,0,3,14],
     [7,0,19,0],
     [3,0,0,1],
     [0,0,0,0]]

used=[0]*4
minn=21e8

def ans(now,sum):
    if now==3:
        return

    for i in range(4):
        if