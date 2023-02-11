# # 버블정렬
# '''
# 인접한 두 개의 원소를 비교하며 자리를 계속 교환하는 방식
# 첫번째원소부터 인접한 원소끼리 계속 자리를 교환하면서 맨 마지막자리까지 이동
# 한단계가 끝나면 가장 큰 원소가 마지막자리로 정렬
# n**2이 평균속도 코딩이 가장 쉬움
# '''
# #55 7 78 12 42
# lst=[55, 7, 78, 12, 42]
# # 버블정렬시 리스트의 개수보다1개 적게 검사함
# # 마지막은 검사할 필요가 없기 떄문
# for i in range(len(lst)-1):
#     # 처음에는 4번, 다음에는 3번 이렇게 검사가 줄어듬
#     # 그래서 i 가 하나씩 늘어날 떄마다 for문의 횟수가 줄어든다
#     for j in range(len(lst)-1-i):
#         # 작은 순서대로 정렬하기 위해서 i가 i+1보다 더 크면
#         # 더 작은 i+1을 앞으로 바꾼다
#         if lst[j]>lst[j+1]:
#             lst[j], lst[j+1] = lst[j+1], lst[j]
# print(lst)
# # [7, 12, 42, 55, 78]
#
#
#
# # 카운팅 정렬
# '''
# 항목들의 순서를 결정하기 위해 집합에 각항목이 있는지 세는 알고리즘
# 정수나 정수로 표현할 수 있는 자료에 대해서만 적용 가능
# 카운트를 위한 충분한 공간을 할당하려면 집합내 가장 큰 정수를 알아야 한다.
# 정렬된 집합에서 각 항목의 앞에 위치할 항목의 개수를 반영하기 위해 원소를 조정한다.
# 누적합을 구해서 사용한다.
# n의 속도 n이 작을 때만 가능
# data=[0,4,1,3,1,2,4,1]  원데이터의 마지막부터 가져와서 넣음
# counts=[1,4,5,6,8]      갯수의 누적합
# temp=[0,1,1,1,2,3,4,4]  원데이터의 마지막을 ex)1을 가져옴 counts[1]에서 1을 빼줌
#                         그러면 3이 되므로 counts=[1,3,5,6,8]로 변경됨
#                         temp의 3번 인덱스에 1을 넣음
# '''
# lst=[0,4,1,3,1,2,4,1]
# temp=[0]*len(lst)
# k=max(lst)
# counts=[0]*(k+1)    #bucket과 동일
# # lst를 돌려서 counts를 갯수대로 채움
# for i in range(0,len(lst)):
#     counts[lst[i]]+=1
# #counts의 누적합 리스트를 구함
# for i in range(1,len(counts)):
#     counts[i]+=counts[i-1]      #counts=[1,4,5,6,8]
# # lst의 마지막 인덱스부터 처음까지 temp리스트 채우기
# for i in range(len(lst)-1,-1,-1):
#     #counts에서 1을 빼고
#     counts[lst[i]]-=1
#     #temp에서 counts[lst[i]]의 자리에 lst[i]를 넣는다.
#     temp[counts[lst[i]]]=lst[i]
#
# print(temp)     #[0, 1, 1, 1, 2, 3, 4, 4]
#
# #####################################
# # counting sort 계수정렬
#
# n=int(input())      #n=10
# a=list(map(int,input().split()))    #lst=14 5 7 32 56 9 18 23 40 4
# bucket=[0]*101
# # dat 등록
# for i in range(n):
#     bucket[a[i]]+=1
#
# # 누적합 구하기
# for i in range(1,len(bucket)):
#     bucket[i]+=bucket[i-1]
#     # bucket[i]=bucket[i]+bucket[i-1]
#
# # 값넣기
# result=[0]*101  # 정렬해서 넣을 빈 리스트 만들기
# # 숫자의 개수만큼 for문 실행
# for i in range(n):
#     index=a[i] #리스트a의 원소들을 index로 고정
#     # result라는 0으로 채워진 리스트에 bucket의 인덱스에서 1을 뺀 자리에
#     # a[i]를 넣는다.
#     result[bucket[index]-1]=a[i]
#     # 그리고 사용한 bucket[index]에서 1을 뺀다.
#     bucket[index]-=1
#
# for i in range(n):
#     print(result[i],end=' ')
#     # 4 5 7 9 14 18 23 32 40 56
# print()
#
#
#
#
#
# #Baby-gin Game
# '''
# 0~9사이의 숫자카드에서 임의의 카드 6장을 뻡았을 떄 3장의 카드가 연속적인 번호를
# 갖는경우를 run이라고 하고 3장의 카드가 동일한 번호를 갖는 경우를 triplet이라고 한다.
# 그리고, 6장의 카드가 run과 triplet으로만 구성된 경우를 baby-gin으로 부른다.
# 6자리 숫자를 입력받아 baby-gin 여부를 판단하는 프로그램을 작성하시오
# -6개숫자로 만들수 있는 모든 숫자 나열
# -6개숫자를 반으로 나눠 3개씩 검사
# #완전검색 사용
# #모든 수를 나열하여 확인하는 기법(경우의 수가 적어야 함)
# '''
#
# #순열
# # 서로 다른 것들 중 몇개를 뽑아 한 줄로 나열하는 것
# # 팩토리얼
# #1,2,3을 포함하는 모든 순열을 생성하는 함수
# #i,j,k는 모두 1,2,3 중에 하나
# for i in range(1,4):
#     for j in range(1,4):
#         #j와i는 다르고 k,i,j는 모두 달라야 한다.
#         #1,2,3 모두가 한번씩 나와야하고 순서만 변경됨
#         if j !=i:
#             for k in range(1,4):
#                 if k !=i and k != j:
#                     print(i,j,k)
#
# #탐욕알고리즘(그리디)
# '''
# 최적해를 구하는 데 사용되는 근시안적인 방법
# 여러 경우중 하나를 결정해야 할 때 그순간 최적이라고 생각되는 것을 선택해나가는 방식
# 선택의 시점에서 가장 최적이지만 이후에 그 선택이 최적이라고 할 수 없음
# #거스름돈 줄이기
# 동전의 갯수가 가장 작은 경우를 고르는 것
# '''
# coin=[500,100,50,10]
# changes=int(input())  #260 # 거슬러 줄돈
# answer=0 # 4 # 정답 (사용하는 동전 개수)
# index=0 # 0=500원 1=100월 2=50원 3=10원
# while 1:    # while True와 동일
#     cnt=changes//coin[index]       #index가 0일때 500짜리 동전 개수를 cnt에 넣기
#     changes-=(cnt*coin[index])     # 거슬러 준 만큼 changes에서 빼고(남은돈)
#     answer+=cnt                     # 동전 사용한 만큼 정답에 더해 주고
#     index+=1                        # 500 다음에 100원 짜리 사용
#     if index==4:                    # 10원짜리 까지 다 사용 했으면 break
#         break
# print(answer)   # 정답출력
# '''
# baby-gin을 탐욕알고리즘으로 할 수 있음
# bucket을 만들고 1번으로 triplet조사 (동일한 숫자가 3개 이상)
# 2번으로 run조사 triplet을 만들고 남은 숫자가 3개가 연속이면 run
# '''
# num=456789  #확인할 수
# counts=[0]*12   #bucket만들기(DAT)
# # 숫자가 6개이므로 범위 6
# for i in range(6):
#     # num을 10으로 나누고 난 나머지(1의 자리)인 bucket에 1을 더함
#     counts[num%10]+=1
#     num//=10    #num을 10으로 나눈 몫을 구해 bucket에 넣은 마지막 수를 없앰(과정 자릿수만큼 반복)
# i=0 #count의 인덱스 역할
# tri=run=0
# while i<10: #숫자가 9까지 있으므로 10 미만까지
#     #triplet조사하기(한 숫자가 3이상이면 triplet)
#     if counts[i]>=3:
#         counts[i]-=3    #있으면 3을 빼고
#         tri+=1          #tri에 1추가
#         continue
#     #run 조사하기(연속된 숫자여부 찾기)
#     if counts[i]>=1 and counts[i+1]>=1 and counts[i+2]>=1:
#         # 대상이 된 것을하나씩 빼주기
#         counts[i]-=1
#         counts[i+1]-=1
#         counts[i+2]-=1
#         run+=1
#         continue
#     i+=1    #counts인덱스 증가
# if run+tri == 2:    #run과 tri의 숫자가 2를 넘으면 'baby_jin'
#     print('Baby-gin')
# else:print('lose')
#
#
# '''
# 2차원 배열
# 배열 순회: 모든원소를 빠짐없이 조사하는 방법
# # 행우선 순회(nXm배열)-가로
# for i in range(n):
#     for j in range(m):
#         arr[i][j]
# # 열우선 순회(nXm배열)-세로
# for i in range(n):
#     for j in range(m):
#         arr[j][i]
# # 지그재그 순회(nXm배열)
# for i in range(n):
#     for j in range(m):
#     #행이 짝수일때와 홀수일때 다름
#     # (i%2)를 이용하여 i가짝수일 때는 j만 순서대로
#     # 홀수일 때는 (m-1):마지막 인덱스에서 거꾸로 감
#     #이미 앞에서 더한 j를 빼줘야하므로 2*j를 빼줌
#         arr[i][j+(m-1-2*j)*(i%2)]
#
# '''
#
# # 2차원 배열의 델타
#
# # 배열에서 입력받은 좌표의 상하좌우의 합을 구하시오
# # 1 1 입력시 5+1+3+2=11로 정답은 11
# arr = [[3, 5, 4],
#        [1, 1, 2],
#        [1, 3, 9]]
# # 상하좌우의 좌표 설정
# directy=[-1,1,0,0]
# directx=[0,0,-1,1]
# # 좌표 입력받기
# y,x=map(int,input().split())
# sum=0   #합
# # 상하좌우 4방향의 합을 구해야 하므로 for문 4번
# for i in range(4):
#     # 상하좌우 방향의 좌표를 dy,dx로 설정
#     dy = y + directy[i]
#     dx = x + directx[i]
#     # 3X3 배열이므로 이것을 넘어서는 배열의 범위를 제한해야함
#     #if dy<0 or dx<0 or dy>2 or dx>2: continue
#     if 0<=dy<3 and 0<=dx<3:
#         # 상하좌우 좌표의 값을 더함
#         sum+=arr[dy][dx]
# print(sum)
#
#
#
#
# # 배열에서 입력받은 좌표의 대각선 4방향의 곱을 구하시오
# # 1 1 입력시 3*4*1*9=108로 정답 108
# arr = [ [3, 5, 4, 5, 6],
#         [1, 1, 2, 7, 8],
#         [1, 2, 9, 1, 2],
#         [3, 5, 4, 5, 6],
#         [1, 1, 2, 7, 8]]
# # 좌표 입력 받기
# y,x=map(int,input().split())
# # 대각선 방향 좌표 설정
# directy=[-1,1,1,-1]
# directx=[1,1,-1,-1]
# # 곱 기본값 설정 0으로 할 경울 곱하면 0이므로 1곱하기
# gop=1
# # 대각선 4방향 곱이므로 for문 4번
# for i in range(4):
#     # 대각선 4방향의 좌표를 dy,dx로 설정
#     dy=directy[i]+y
#     dx=directx[i]+x
#     # 5X5 배열이므로 이것을 넘어서는 배열의 범위를 제한해야함
#     # if dy<0 or dx<0 or dy>4 or dx>4: continue
#     if 0 <= dy < 5 and 0 <= dx < 5: #arr배열의 길이
#         gop*=arr[dy][dx]
# print(gop)
#
#
#
#
#
# # 위 아래 좌 우로 2칸까지 떨어진 곳들의 합을 구하기
# # 2 2 입력시  18 출력
# # (9+9=18)
# arr = [ [3, 5, 4, 5, 6],
#         [1, 1, 2, 7, 8],
#         [1, 2, 9, 1, 2],
#         [3, 5, 4, 5, 6],
#         [1, 1, 2, 7, 8]]
# # 좌표 입력
# y, x = map(int,input().split())
# # 상하좌우의 좌표 설정
# movey = [-1, 0, 1, 0]
# movex = [0, 1, 0, -1]
# sum = 0
# # 상하좌우 4방향의 합을 구해야 하므로 for문 4번
# for i in range(4):
#     # 상하좌우 2칸의 합이므로 1,2를 곱해야함(범위설정 1,3)
#     for j in range(1,3):
#         # 상하좌우 1번째칸을 구할 떄는 j=1을 곱하고
#         # 2번쨰 칸을 구할 때는 j=2를 곱한다.
#         newy = y + movey[i] * j
#         newx = x + movex[i] * j
#         # 5X5 배열이므로 이것을 넘어서는 배열의 범위를 제한해야함
#         if 0 <= newy <= 4 and 0 <= newx <= 4:
#             sum += arr[newy][newx]
#
# print(sum)
#
#
#
#
# # 위 아래 좌 우  좌표들의 합이 가장 큰 곳의 합과
# # 그 기준 좌표값을 출력하기 !!!
# arr=[[1,2,3,4],
#      [1,2,9,4],
#      [1,9,3,9],
#      [1,2,9,4]]
#
# # 함수로 각 좌표의 상하좌우의 합을 구함
# def isSum(y,x):
#     # 상하좌우의 좌표 설정
#     directy=[-1,1,0,0]
#     directx=[0,0,-1,1]
#     sum=0
#     # 상하좌우 4방향의 합을 구해야 하므로 for문 4번
#     for i in range(4):
#         dy=directy[i]+y
#         dx=directx[i]+x
#         # 범위제한 : 범위를 벗어나는 것은 건너뜀
#         if dy<0 or dx<0 or dy>3 or dx>3:continue
#         sum+=arr[dy][dx]
#     return sum #합을 리턴
# #sum의 최대값 저장
# Maxvaule=int(-21e8)
# Maxi=0  # i좌표
# Maxj=0  # j 좌표
# # 4X4배열을 돌려서 함수에 (i,j)좌표 전달
# for i in range(4):
#     for j in range(4):
#         ret=isSum(i,j)
#         # sum의 최댓값 구해서 Maxvaule에 저장
#         if ret>Maxvaule:
#             Maxvaule=ret
#             # Maxvaule의 좌표를 각각 Maxi와 Maxj에 저장
#             Maxi=i
#             Maxj=j
# # 최대값과 좌표 출력    #36,2,2
# print(Maxvaule,Maxi,Maxj)
#
#
#
# # 전치행렬
# arr=[[1,2,3],           #[[1,4,7],
#      [4,5,6],    #==>   #[2,5,8],
#      [7,8,9]]           #[3,6,9]]
#
# for i in range(3):
#     for j in range(3):
#         # 대각선을 기준으로 맞바꿈
#         if i<j:
#             arr[i][j],arr[j][i]=arr[j][i],arr[i][j]
#
#
#
#
# # 부분집합 합 문제:
# # 정수의 집합이 있을 때 이 집합의 부분집합 중에서 그 집합의 원소를 모두 더한 값이
# # 0이 되는 경우가 있는가     (완전집합: 모든 것 계산)
# # 집합의 원소가 N개 일때 공집합을 포함한 부분집합의 수는 2**N개이다.
# # 부분집합 생성방법
# a=[1,2,3,4]
# bit=[0,0,0,0]   # 리스트의 원소 갯수만큼 만듬
# # bit의 각 자리에 0이나1을 채워 넣음
# for i in range(2):
#     bit[0] = i
#     for j in range(2):
#         bit[1]= j
#         for k in range(2):
#             bit[2] = k
#             for l in range(2):
#                 bit[3] = l
#                 print(bit, end=' ')
#                 # bit가 4자리이므로 for문을 4번 시행해
#                 # 1인 경우만 출력
#                 for p in range(4):
#                     # bit[p]==1인데 '==1' 생략
#                     if bit[p]:
#                         print(a[p], end=' ')
#                 print()
# # 결과값   bit가 1인 a의 자리만출력
# # [0, 0, 0, 0]
# # [0, 0, 0, 1] 4
# # [0, 0, 1, 0] 3
# # [0, 0, 1, 1] 3 4
# # [0, 1, 0, 0] 2
# # [0, 1, 0, 1] 2 4
# # [0, 1, 1, 0] 2 3
# # [0, 1, 1, 1] 2 3 4
# # [1, 0, 0, 0] 1
# # [1, 0, 0, 1] 1 4
# # [1, 0, 1, 0] 1 3
# # [1, 0, 1, 1] 1 3 4
# # [1, 1, 0, 0] 1 2
# # [1, 1, 0, 1] 1 2 4
# # [1, 1, 1, 0] 1 2 3
# # [1, 1, 1, 1] 1 2 3 4
#
#
# # 정수값 10을 이진수로 표현하기
# a=10
# print(bin(a))
#
# # 2진수의 값을 정수로 표현하기
# b=0B1111
# print(b)
#
# # 2진수(문자) 값을 정수로 출력하기
# c='0B1111'
# print(int(c,2))
#
# # 비트 연산 할때 and or >> <<
#
# # and
# # 2개의 각자릿수를 비교할 때 둘다 1인 자리의 값을 출력
# a=0b0001
# b=0b1001
# print(a&b)
#
# # or연산
# # 2개의 각자릿수를 비교할 때 둘중 하나이상 1인 자리의 값을 출력
# a=0b0001
# b=0b1001
# print(a|b)
#
# #shift 연산
# # <<n은 각 자리를 왼쪽으로 n만큼 이동하여 계산
# a=0b0001
# b=0b00101001
# print(a<<2)
# print(b<<3)
#
# # >>n은 각 자리를 오른쪽으로 n만큼 이동하여 계산
# # 기본 자릿수를 넘어가면 수는 없어짐
# a=0b0011
# b=0b00101001
# print(a>>1)
# print(b>>3)
#
#
# # 비트 연산법으로 부분집합 만들기
# arr=[3,6,7,1,5,4]   #1,0으로 숫자변환한다고 생각
# n=len(arr)  #원소의 개수
# for i in range(1<<n):   #1<<n:부분집합의 개수
#     for j in range(n):  #원소의 수 만큼 bit비교
#         if i & (i<<j):  #i의 j번 비트가 1인 경우
#             print(arr[j], end=', ') #j번 원소 출력
#     print()
# print()
#
# '''
# # 순차검색
# 일렬로 되어 있는 단어를 순차적으로 검색하는 방법
# 배열이나 연결리스트 등 순차구조로 구현된 자료구조에서 사용이 유리
# 구현이 쉽지만 검색대상이 많으면 시간이 많이걸려 비효율
# 1. 정렬 안된 경우
#  첫번째부터 검색하여 키값과 같은 원소를 찾고 그 인덱스를 반환
#  못찾으면 검색 실패, 찾고자하는 원소 순서에 따라 비교횟수 결정
#  시간복잡도 : O(n)
# '''
# lst=[3,4,1,9,5,6]
# n= len(lst) # 최대 리스트의 갯수만큼 반복
# key=9       # 찾아야 할 키
# i=0         # 인덱스
# # while문에서 i가 최대횟수n보다 작고
# # lst[i]가 키와 다를 때까지 반복
# while i<n and lst[i]!=key:
#     i=+1 # 한번 할 떄마다 i에 +1
# if i<n : # 최대횟수까지 계속 반복
#     print(i)  #lst[i]!=key인경우 i출력
# else:   # 못찾으면 -1 출력
#     print(-1)
# '''
# 2. 정렬이 된 경우
#  오름차순으로 순차 검색하고 원소의 키값이 검색대상 키값보다 크다면
#  더이상 검색할 필요가 없으므로 검색 중단
#  '''
# lst=[2,4,6,7,8]
# n= len(lst) # 최대 리스트의 갯수만큼 반복
# key=6      # 찾아야 할 키
# i=0
# # while문에서 i가 최대횟수n보다 작고
# # lst[i]이 찾을 키보다 커지면 중단
# while i<n and lst[i]<key:
#     i=+1 # 한번 할 떄마다 i에 +1
# if i<n and lst[i]==key: # 키를 찾았다면 i출력
#     print(i)
# else:   # 못찾으면 -1 출력
#     print(-1)
#
#
#
# # 이진 검색
# '''
# 자료의 가운데 있는 항목의 키값과 비교하여 다음 검색의 위치를 결정하고
# 검색을 계속하는 방법
# 자료가 정렬되어 있어야 함
# 검색시 중앙값이 아니라면 st,ed를 중앙값으로 변경한다.
# '''
# # binary search
# # 이진 탐색
# # 검색할 정렬되지 않은 리스트 (lst=list(map(int,input().split())))입력받기 가능
# lst=[5,21,9,35,20,14]
# #찾아야 할 타겟
# target=14
# # 이진탐색은 정렬이 필요함 (버블 정렬하기)
# # 리스트의 개수-1 만큼 for문 실행
# for i in range(len(lst)-1):
#     # 비교 시작해서 5-4-3-2-1순으로 비교하기
#     for j in range(len(lst)-1-i):
#         # 비교해서 j가 더 크면 j+1과 자리바꾸기
#         if lst[j] > lst[j+1]:
#             lst[j], lst[j+1] = lst[j+1], lst[j]
# # 이진탐색 함수
# def bs(st,ed,target):
#     # while문 시작
#     while 1:
#         # 가운데 mid를 시작과 끝을 더한 다음 //2
#         mid=(st+ed)//2
#         # 만약 lst[mid]가 타겟과 같다면 1 리턴
#         if lst[mid]==target:
#             return 1
#         # lst[mid]가 타겟보다 크다면 끝값을 mid+1로 변경
#         # (+1은 리스트이기 때문 숫자라면 ed=mid로 변경 )
#         elif lst[mid] > target:
#             ed=mid+1
#         # lst[mid]가 타겟보다 작다면 시작값을 mid+1로 변경
#         # (+1은 리스트이기 때문 숫자라면 st=mid로 변경 )
#         elif lst[mid] < target:
#             st=mid-1
#         # 시작값과 끝값의 순서가 뒤바뀌면 0리턴
#         if st>ed:
#             return 0
#
# ans=bs(0,len(lst)-1,target)
# if ans:
#     print('찾음')
# else:
#     print('없음')
#
# #<parametric search>
# # 배터리가 몇% 충전되었나요??
# bettery='######____'    #60%
#
# def parametric_search(st,ed):
#     Max=-1
#     while 1:
#         mid=(st+ed)//2
#         if bettery[mid]=='_':
#             ed=mid-1
#         elif bettery[mid]=='#':
#             Max=mid
#             st=mid+1
#         if st>ed:
#             break
#     # 리스트이므로 인덱스는 1개 적은 상태이므로 +1
#     return Max+1
#
# answer=parametric_search(0,9)
# print(answer*10)
#
#
# # 워드 작업 중 정전으로 인하여 컴퓨터가 강제 종료 되었습니다.
# # 다시 전기가 들어와 컴퓨터를 켰더니 다행이도 자동복구가 실행 되었습니다.
# # 우리는 자동복구가 되었을떄 커서의 위치가 어디인지를 알려줘야 합니다.
# # 커서의 위치를 알려주는 프로그램을 완성해 주세요.
# # 시간복잡도 O(n) 보다 빨라야 합니다.
# # 정답 (2,3)
# # 6*10 size 리스트 입니다.
#
# curser=[
#  '##########',
#  '##########',
#  '###_______',
#  '__________',
#  '__________',
#  '__________']
# # 리스트 원소의 첫번째만을 먼저 탐색
# def bs1(st,ed):
#     Max=-1
#     while(1):
#         mid=(st+ed)//2
#         if curser[mid][0]=='_':
#             ed=mid-1
#         elif curser[mid][0]=='#':
#             Max=mid #Max에 마지막 # 인덱스 저장
#             st=mid+1
#         if st>ed:
#             break
#     # '_'의 직전 # 의 위치를 찾아냄
#     return Max
# # 찾아낸 인덱스의 요소 '###_______'만을 가지고 함수 실행
# def bs2(st,ed,yy): # yy는 찾아낸 인덱스의 열
#     Maxx = -1
#     while (1):
#         mid = (st + ed) // 2
#         if curser[yy][mid] == '_':
#             ed = mid - 1
#         elif curser[yy][mid] == '#':
#             Maxx = mid
#             st = mid + 1
#         if st > ed:
#             break
#     return Maxx + 1
#
# yaxis=bs1(0,5)
# xaxis=bs2(0,9,yaxis)
# print(yaxis,xaxis)




# 선택정렬
'''
주어진 자료들 중 가장 작은 값의 원소부터 차례대로 선택하여 위치를 교환하는 방식
주어진 리스트 중 최소값을 찾는다.
그 값을 리스트의 맨앞에 위치한 값과 교환한다.
맨처음 위치를 제외한 나머지 리스트를 대상으로 위의 과정을 반복한다.
시간 복잡도 : O(n**2)
'''

# 선택정렬 공식
n= 7        # 입력 받을 숫자 개수
arr= [7,2,5,3,4,6,4]
# 0~6까지 i의 범위임 # 마지막까지 비교할 필요 없음
for i in range(n-1):
    minIdx = i          #맨앞이 최소라 가정
    # 1~7까지 비교하기
    for j in range(i+1, n):
        #arr[0~6] 과 arr[1~7]을 비교했을 때
        # arr[minIdx]가 arr[j]보다 크면 바로 minIdx를 j값으로 변경
        # 만약에 여러번 돌더라도 arr[minIdx]가 가장 큰수라면 바뀌지 않음
        if arr[minIdx] > arr [j]:
            #
            minIdx = j
    # for문이 다돌고 난 후 자리바꿈
    arr[minIdx], arr[i] = arr[i], arr[minIdx]
print(arr)