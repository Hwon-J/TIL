# 큐(Queue)
'''
스택과 마찬가지로 삽입과 삭제의 위치가 제한적인 자료구조
-뒤에소는 삽입만하고 앞에서 삭제만 이루어지는 구조
선입선출구조(FIFO)
삽입:enQueue
삭제:deQueue
Qpeek: 제일 앞원소가 무엇인지 확인
<큐의 연산과정>
1.[] 공백 큐 생성 : createQueue():
2.[A]원소 A 삽입 : enQueue(A):
3.[A,B]원소 B 삽입 : enQueue(B):
4.[B]원소 반환/삭제 :deQueue():
5.[B,C]원소 C 삽입 : enQueue(C):
6.[C]원소 반환/삭제 :deQueue():
7.[] 원소 반환/삭제 :deQueue():

선형큐
1차원 배열을 이용한 큐
큐의 크기= 배열의 크기
-초기상태: front= rear = -1
-공백상태: front==rear
-포화상태: rear==n-1(n:배열의 크기,n-1:배열의 마지막 인덱스)

삽입 : enQueue(item)
def enQueue(item):
    global rear
    if isfull(): print("Queue_Full")
    else:
        rear+=1
        #큐의 마지막에 item저장
        Q[rear]=item

삭제 :deQueue()
deQueue()
    if(isEmpty()) then Queue_Empty:
    else:
        front+=1
        return Q[front]

def isEmpty():
    return front==rear

def Full():
    return rear==len(Q)-1

검색: Qpeek()
def Qpeek():
    if isEmpty() : print("Queue_Empty")
    else: return Q[front+1]

'''
# # 구현한 큐를 이용하여 3개의 데이터를 큐에 저장하고 다시 3번 꺼내서 출력
# def enqueue(data):
#     global rear
#     rear+=1
#     queue[rear] = data
#
# def dequeue():
#     global front
#     front+=1
#     return queue[front]
#
# queue=[0]*3
# front=-1
# rear=-1
#
# rear+=1
# queue[rear] = 1
#
# enqueue(2)
# enqueue(3)
#
# print(dequeue())
# print(dequeue())
# # 만약 큐가 비었는데도 꺼내려고 할 경우 오류 방지를 위한 코드
# if front != rear:
#     print(dequeue())
# if front != rear:
#     print(dequeue())

'''
선형큐의 문제점
잘못된 포화상태 인식
-해결방법1: 매연산마다 원소를 앞으로 이동 (큐의 효율성 떨어짐)
-해결방법2: 1차원배열을 사용하되 처음과 끝이 연결된 원형의 큐라고 가정
원형큐의 구조
초기공백 상태: front=rear=0
index의 순환(나머지 연산자 mod사용)
front 변수: 공백 포화 구분 용이를 위해 front자리는 사용X
공백: front==rear
포화: rear+1==front

삽입 : enQueue(item)
def enQueue(item):
    global rear
    if isfull(): print("Queue_Full")
    else:
    # rear값을 조정하여 새로운 원소 자리 만들기
        rear=(rear+1) % len(cQ)
        Q[rear]=item

삭제 :deQueue()
def deQueue()
    global front
    if(isEmpty()):
     print("Queue_Empty")
    else:
        front=(front+1) % len(cQ)
        return cQ[front]

'''
'''
우선순위 큐
우선순위를 가진 항목을 저장하는 큐
우선순위 큐의 적용분야
시뮬레이션 시스템
네트워크 트래픽제어


큐의 활용: 버퍼
버퍼
데이터를 한 곳에서 다른 곳으로 전송하는 동안 
일시적으로 그 데이터를 보관하는 메모리 영역
버퍼링: 버퍼를 활용하는 방식 또는 버퍼를 채우는 동작 의미
버퍼의 자료 구조
일반적으로 입출력 및 네트워크 관련 기능에서 이용
순서대로 입출력 및 전달이 필요해 큐 사용
'''
'''
BFS(너비우선탐색)
트리형태
def BFS(G,v):   # 그래프G 탐색시작점v
    visited = [0]*(n+1) 정점의 개수n
    queue=[]
    queue.append(v) #시작점v를 큐에 삽입
    while queue:    #큐가 비어있지 않은 경우
        t=queue.pop(0)  #큐의 첫번쨰원소 반환
        if not visisted[t]: #방문되지 않은 곳이라면
            visited[t] = True   #방문표시
            visit(t)    #정점t에서 할일
            for i in G[t]:  #t와 연결된 모든정점에 대해
                if not visited[i]: # 방문하지 않은 곳이라면 큐에 넣기
                    queue.append(i)
                    
                    
트리x
def BFS(G,v):   # 그래프G 탐색시작점v
    visited = [0]*(n+1) 정점의 개수n
    queue=[]
    queue.append(v) #시작점v를 큐에 삽입
    VISITED[V] =1
    while queue:    #큐가 비어있지 않은 경우
        t=queue.pop(0)  #큐의 첫번쨰원소 반환
        visit(t)
        for i in G[t]:  #t와 연결된 모든정점에 대해
            if not visited[i]: # 방문하지 않은 곳이라면 큐에 넣기
                queue.append(i)
                visited[i]=visited[n]+1 #n으로부터 1만큼

'''