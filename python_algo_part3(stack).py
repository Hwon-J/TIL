'''
스택
물건을 쌓아올리듯 자료를 쌓아올린 형태의 자료구조
스택에 저장된 자료는 선형구조(자료간의 관계가 1대1)를 갖는다.
if 비선형구조: 자료간의 관계가 1대N (ex)트리)
스택에 자료를 삽입하거나 꺼낼 수 있다.
마지막에 삽입한 자료를 가장먼저 꺼낸다(후입선출)

자료구조: 자료를 선형을 저장할 저장소
배열(리스트) 사용, 저장소 자체를 스택이러고하기도 함
스택에서 마지막에 삽입된 원소의 위치를 top이라고 한다.

연산
-삽입(push): 저장소에 자료 저장
-삭제(pop): 저장소에서 자료를 꺼낸다.
-isEmpty: 스택이 공백인지 아닌지 확인하는 연산
-peek: 스택의 top(마지막으로 저장된 위치)에 있는 원소를 반환하는 연산

스택구현 고려사항
1차원 배열 이용시 구현이 용이하지만 스택의 크기를 변경하는 것이 어렵다.
이를 해결하기 위해 저장소를 동적으로 할당하여 스택을 구현하는 방법이 있다.
동적연결리스트를 이용하여 구현하는 것으로 구현이 복잡하나 메모리를 효율적으로 사용한다.

'''
#
# # 스택의 push 알고리즘(append가 보편적이나 속도가 느림)
# def push(item,size):
#     global top
#     top+=1
#     #top이 size와 같다면 overflow
#     if top == size:
#         print('overflow!')
#     else:
#         stack[top]=item
# size=10
# stack=[0]*size
# top=-1
# push(10,size)
# top+=1
# stack[top]=20

# #스택의 pop 알고리즘
# def pop():
#     if len(s) ==0:
#         #underflow
#         return
#     else:
#         return s.pop();
#
# def pop():
#     global top
#     if top==-1:
#         print('underflow')
#         return 0
#     else:
#         top-=1
#         return stack[top+1]
# print(pop())
# if top>-1:  #pop()
#     top-=1
#     print(stack[top+1])
#
#
# # 구현한 스택을 이용하여 3개의 데이터를 스택에 저장하고 다시 3번 꺼내서 출력
# stack=[0]*3
# top=-1
# top+=1  # push(10)
# stack[top]=10
#
# top+=1  # push(20)
# stack[top]=20
#
# top+=1  # push(30)
# stack[top]=30
# # 마지막부터 꺼내지므로 30 20 10으로 출력
# # 끝까지 다 꺼낸후에 다시 위로 돌라가는 것을 방지하기 위해
# # if top>-1이라는 조건을 넣는다. top의 높이가 0이상일때만 출력
# if top>-1:
#     top-=1
#     print(stack[top+1])
#
# if top>-1:
#     top-=1
#     print(stack[top+1])
#
# if top>-1:
#     top-=1
#     print(stack[top+1])


# 괄호 검사
# 조건 왼쪽괄호와 오른쪽괄호 개수가 같아야 한다.
# 같은 괄호에서 왼쪽괄호는 오른쪽괄호보다 먼저 나와야 한다.
# 괄호 사이에는 포함관계만 존재한다.
# 여는 괄호가 나오면 push 그러다 닫는괄호가 나오면 pop
# 끝났을 때 남는 괄호가 없고 스택이 비었으면 정상
# 스택에 괄호가 남아있거나 스택이 비었는데 괄호가 남았다면 오류


'''
function call
프로그램에서 함수의 호출과 복귀에 따른 수행순서를 관리
-후입선출 구조의 스택을 이용하여 수행순서 확인
함수호출이 발생하면 호출한 함수 수행에 필요한 지역변수, 매개변수, 
및 수행 후 복귀할 주소 등의 정보를 스택프레임에 저장하여 시스템 스택에 삽입
함수의 실행이 끝나면 스택의 top원소를 삭제(pop)하면서 프레임에 저장되어있던 복귀주소를 확인하고 복귀
함수의 호출과 복귀에 따라 이과정을 반복하여 전체 프로그램 수행이 종료되면 시스템스택은 공백스택이 된다.
'''

'''
재귀호출
-자기자신을 호출하여 순환 수행하는 것 (실제로 저장값이 다르나 내부가 똑같이 생겨서 재귀라 함)
- 함수에서 실행해야 하는 작업의 특성에 따라 일반적인 호출 방식보다 재귀호출 방식이
프로그램의 크기를 줄이고 간단하게 작성된다.
ex)팩토리얼 n!
피보나치: 0과1로 시작하고 이전 두 수의 합을 다음항으로 하는 수열
def fibo(n):
    if n<2:
        return n
    else:
        return fibo(n-1)+fibo(n-2)
        
메모이제이션
-피보나치 재귀함수에는 엄청난 중복호출이 존재한다는 문제가 있다.
-메모이제이션은 컴퓨터 프로그램을 실행할 때 이전에 계산한 값을 메모리에 저장해서 
매번 다시 계산하지 않도록하여 전체적인 실행속도를 빠르게 하는 기술(동적계획법의 핵심)
예를 들어 피보나치 알고리즘에서 fibo(n)의 값을 계산하자마자 저장하면 실행시간을 O(n)으로 단축 가능
# memo를 위한 배열 할당, 0으로 초기화
def fibo1(n):
    global memo
    if n >=2 and memo[n]==0:
        memo[n] = (fibo1(n-1) + fibo1(n-2))
    return memo[n]
memo=[0]*(n-1)
memo[0]=0
memo[1]=1
'''

'''
DP(동적 계획법)
최적화 문제를 해결하는 알고리즘
입력 크기가 작은 부분의 문제를 모두 해결한 후에 그 해를 이용하여 
보다 큰 부분 문제들을 해결하여 최종적으로 원래 주어진 입력의 문제를 해결하는 알고리즘
피보나치 DP적용-부분문제의 답으로 본문제의 답을 구할 수 있다.
def fibo1(n):
    f=[0]*(n+1)
    f[0]=0
    f[1]=1
    for i in range(2,n+1):
        f[i]=f[i-1]+f[i-2]
    return f[n]
    
메모이제이션을 재귀적 구조에 사용하는 것보다 반복적 구조로 DP를 구현한 것이 성능면에서 효율적
재귀적 구조는 내부에 시스템 호출 스택을 사용하는 오버헤드가 발생하기 때문
'''
# # 재귀는 기본적으로 2개의 인자를 가짐( 현재상태, 목표)
# def f(i,k):
#     if i==k:
#         print(B)
#         return
#     else:
#         B[i]=A[i]
#         f(i+1,k)
# A=[10,20,30]
# B=[0]*3
# f(0,3)

'''
DFS(깊이우선탐색)-
-스택을 이용하는 탐색
-시작의 정점에서 시작하여 갈수 있는 경로가 있는 곳까지 가다가 더이상 갈 곳이 없으면 
가장 마지막에 만났던 갈림길로 가서 탐색하며 모든경로를 방문하는 방법
-후입선출 구조의 스택 사용 
DFS알고리즘
visited[],stack[]
DFS(v)
    시작점v 방문
    visited[v] <- true:
    while {
        if (v의 인접 정점 중 방문 안한 정점 w가 있으면)
            push(v);
            v <- w; (w에 방문)
            visited[w] <-true;
        else 
            if (스택이 비어있지 않으면)
                v <-pop(stack);
            else
                break
        }
end DFS()

BFS(너비우선탐색)
-큐를 이용하는 탐색
'''
#
# # DFS
# # 7 8
# # 1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
# # 인접행렬, 인접리스트
# # V: 인접행렬을 만들 갯수(1-7) E:연결된 길이 개수
# V,E=map(int, input().split())
# # 연결된 길이 관계 입력받기
# arr=list(map(int, input().split()))
# # 인접행렬 만들 빈리스트 만들기 (V+1)개: 0번 인덱스는 사용X
# adjM=[[0]*(V+1) for _ in range(V+1)]
#
# # adjL=[[]for _ in range(V+1)]
# # 연결된 길이 개수(E)만큼 for문 실행
# for i in range(E):
#
#     v1,v2=arr[i*2],arr[i*2+1]
#     adjM[v1][v2]=1
#     adjM[v2][v1]=1
#     # adjL[v1].append(v2)
#     # adjL[v2].append(v1)
# print(adjM)



#######   stack2        ###############################

'''
계산기1
문자열로 된 계산식이 주어질 때, 스택을 이용하여 이계산식의 값응 계산할 수 있다.
문자열 수식계산의 일반적 방법
1. 중위표기법의 수식을 후위표기법으로 변경한다.(스택이용)
2. 후위표기법의 수식을 스택을 이용하여 계산한다.
<중위표기법>
연산자를 피연산자의 가운데 표기 A+B
<후위표기법>
연산자를 피연산자 뒤에 표기 AB+

중위표기법에서 후위표기법으로 변경하는 알고리즘
1. 토큰(한글자?)하나 가져오기
2. 비어있으면 push '('이면 스택에 넣기
3. 피연산자(숫자)면 출력
4. 연산자(+,-,*,/)면 스택에 push
5. 닫는괄호')' 나오면 여는괄호'('를 만날때까지 모두 pop한 뒤 ')'를 버리고 
top을 변경, 연산자가 나타나면 우선순위를 비교하고 위의 내용 반복


후위표기법의 수식을 스택을 이용하여 계산
1.피연산자를 만나면 스택에 push
2.연산자를 만나면 필요한 만큼 피연산자를 스택에서 pop하여 연산하고 
연산결과를 다시 스택에 push
3.수식이 끝나면 마지막으로 스택을 pop하여 출력
'''
'''
백트래킹
해를 찾는 도중에 막히면(해가 아니면) 되돌아가서 다시 해를 찾는 기법
최적화 문제와 결정문제를 해결할 수 있다.
결정문제: 문제의 조건을 만족하는 해의 존재여부를 yes, no로 답하는 문제

백트래킹:미로찾기
입구와 출구가 주어진 미로에서 입구부터 출구까지의 경로를 찾는 문제

백트래킹-DFS차이
어떤 노드에서 출발하는 경오가 해결책이 아닐것 같으면 멈춤(가지치기)
DFS:모든경로 탐색
백트래킹: 불필요한 경로 조기에 차단
일반 백트래킹 알고리즘
# 노드의 유망성 점검
def checknode(v):
# v 가 유망하니?
    is promising(v):
    # v가 최종 해결책인가?
        if there is a solution at v:
        # 그렇다면 해결책을 써라
            write the solution
        else:
        # 아니라면 v의 가지들을 탐색
            for u in each child of v:
            # 가지확인
                checknode(u)
'''
'''
백트래킹을 이영한 부분집합 구하기
어떤 집합의 골집합과 자기자신을 포합한 모든 부분집합을 powerset이라하고
구하려는 집합의 원소가 n개일 경우 부분집합의 개수는 2**n이다.
-각원소가 부분집합에 포함되었는지 loop를 이용하여 확인하고 
부분집합을 생성하는 방법
bit=[0,0,0,0]
for i in range(2):
    bit[0]=i
    for j in range(2):
        bit[1]=j
        for k in range(2):
            bit[2]=k
            for l in range(2):
                bit[3]=l
                print(bit)
                
-powerset(부분집합)을 구하는 백트래킹 알고리즘
def backtrack(a,k,input):
    global MAXCANDIDATES
    c = [0]*MAXCANDIDATES
    
    if  k== input:
        process_solution(a,k)
    else:
        k+=1
        ncandidates = construct_candidates(a,k,input,c)
        for i in range(ncandidates):
            a[k] = c[i]
            backtrack(a,k,input)

def construct_candidates(a,k,input,c):
    c[0] = True
    c[1] = False
    return 2
    
MAXCANDIDATES = 2
NMAX=4
a = [0]*NMAX
backtrack(a,0,3)

--{1,2,3}을 포함하는 모든 순열을 생성하는 함수
for i1 in range(1,4):
    for i2 in range(1,4):
        if i2!=i1:
        for i3 in range(1,4):
            if i3!=i1 and i3!=i2:
                print(i1,i2,i3)


- 백트래킹으로 순열 구하기
def backtrack(a,k,input):
    global MAXCANDIDATES
    c = [0]*MAXCANDIDATES
    
    if  k== input:
        for i in range(1,k+1):
            print(a[i],end=' ') 
        print()
    else:
        k+=1
        ncandidates = construct_candidates(a,k,input,c)
        for i in range(ncandidates):
            a[k] = c[i]
            backtrack(a,k,input)

def construct_candidates(a,k,input,c):
    in_perm = [False]*NMAX
    
    for i in range(1,k+1):
        in_perm[a[i]] =True
        
    ncandidates=0
    for i in range(1,input+1):
        if in_perm[i] == False:
            c[candidates] = i
            ncandidates=1
    return ncandidates

MAXCANDIDATES = 10
NMAX=11
a = [0]*NMAX
backtrack(a,0,3)
'''
# # # 부분집합
# def f(i,k):
#     if i==k:
#         #s=0
#         for j in range(k):
#             if bit[j]:
#                 print(A[j], end=' ')
#             #print()
#             # 합구하기
#             #     s+= A[j]
#         print(bit)
#     #print(bit,s)
#     else:
#         bit[i]=1
#         f(i+1,k)
#         bit[i]=0
#         f(i + 1, k)
#
# A=[1,2,3]
# N=len(A)
# bit=[0]*N
# f(0,N) #(인덱스,배열의 크기)
# #
# # '''
# # 1 2 3 [1, 1, 1]
# # 1 2 [1, 1, 0]
# # 1 3 [1, 0, 1]
# # 1 [1, 0, 0]
# # 2 3 [0, 1, 1]
# # 2 [0, 1, 0]
# # 3 [0, 0, 1]
# # [0, 0, 0]
# # '''
# # 합이 key인 집합의 개수세기
# # i: 원소, k:집합의 크기, s: i-1까지의 합 t:목표값
# def f(i,k,s,t):
#     global cnt
#     # 합이 이미 key를 넘은 경우 가지치기(백트래킹)
#     if s>t:
#         return
#     elif s==t:
#         cnt+=1
#         return
#     if i==k:
#         if s==t:
#             cnt+=1
#         return
#     else:
#         f(i+1,k,s+A[i],t)
#         f(i+1,k,s,t)
#
# A=[1,2,3,4,5,6,7,8,9,10]
# N=len(A)
# key=10
# cnt=0
# f(0,N,0,key)
# print(cnt)
#
#
# #순열
# def f(i,k):
#     if i==k:
#         print(p)
#     else:
#         for j in range(i,k):
#             p[i],p[j]=p[j],p[i]
#             f(i+1,k)
#             p[i], p[j] = p[j], p[i]
#
# p=[1,2,3]
# N=len(p)
# f(0,N)

'''
분할정복 알고리즘-나폴레옹이 사용한 전략
분할: 해결할 문제를 여러개의 작은 부분으로 나눔
정복: 나눈 문제를 각각 해결
통합: (필요시)해결된 해답모으기
O(log2n)
'''
# # 거듭제곱
# def Power(Base,Exponent):
#     if Exponent ==0 or Base==0:
#         return 1
#     if Exponent % 2 ==0:
#         NewBase = Power(Base, Exponent/2)
#         return NewBase *NewBase
#     else:
#         NewBase = Power(Base, (Exponent-1)/2)
#         return (NewBase * NewBase)*Base
'''
퀵정렬
주어진 배열을 두개로 분할하고 각각을 정렬한다.
기준 아이템(pivot)을 중심으로 이보다 작은 것은 왼쪽, 큰 것은 오른쪽
합병벙렬은 정렬이후 '합병'이라는 후처리가 필요하나 퀵정렬은 필요 없음
-피봇으로 원소 하나를 선택, 피봇의 왼쪽에는 작은것 오른 쪽에는 큰 것 두기
비교하면서 서로 바꿔줌, 만약 왼쪽에 더 작은 원소가 없다면 피봇과 비교 대상을 바꿔준다. 
만약 왼쪽이나 오른쪽이 서로 정렬이 안되었다면 그부분만으로 새로운 피봇을 만들어 정렬
최악의 시간복잡도: O(n**2),  보통 nlogn
'''
# def quickSort(a, begin, end):
#     if begin < end:
#         p = partition(a, begin, end)
#         quickSort(a,begin,p-1)
#         quickSort(a,p+1,end)

