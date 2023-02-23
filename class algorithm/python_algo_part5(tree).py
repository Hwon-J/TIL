# 트리(tree)
'''
비선형 구조
원소들간의 1:n관계를 가지는 자료구조
원소들간의 계층관계를 가지는 자료구조
상위원소에서 하위원소로 내려가면서 확장되는 나무모양구조
노드: 트리의 원소
간선: 노드를 연결하는 선
루트노드: 트리의 시작노드
형제노드: 같은 부모노드의 자식노드들
조상노드: 간선을 따라 루트노드까지 이르는 경로에 있는 모든 노드들
서브트리: 부모노드와 연결된 간선을 끊었을 때 생선되는 트리
자손노드: 서브트리에 있는 하위레벨의 노드들
노드의 차수: 노드에 연결된 자식노드의 수
트리의 차수: 트리에 있는 노드의 차수 중 가장 큰 값
단말노드: 차수가 0인 노드, 자식노드가 없는 노드
노드의 높이: 루트에서 노드에 이르는 간선의 수, 노드의 레벨
트리의 높이: 트리에 있는 노드의 높이 중에서 가장 큰 값, 최대레벨
'''
'''
이진트리
모든 노드들이 2개의 서브트리를 갖는 특별한 트리
각노드가 자식노드를 최대 2개만 가질 수 있음
레벨i에서 노드의 최대 개수는 2**i

포화이진트리:
모든레벨에 노드가 포화상태로 차있는 이진트리

완전이진트리:
마지막 레벨이 가득차 있지 않은 이진트리(중간은 다 차있음)

편향이진트리
한쪽방향의 자식노드만을 가진 이진트리

순회:
트리의 각노드를 중복되지 않게 전부 방문하는 것을 말하는데 트리는 비선형 구조라서
선후연결관계를 알 수 없다.
방법3가지
1.전위순회:
부모노드 방문 후 자식노드를 좌우순서로 방문
2.중위순회:
왼쪽 자식노드, 부모노드, 오른쪽 자식노드 순으로 방문
3.후위순회:
자식노드를 좌우순서로 방문한 후 부모노드 방문
'''
# 전위순회
# def preorder_traverse(T):
#     if T:
#         visit(T)
#         preorder_traverse(T.left)
#         preorder_traverse(T.left)

# 중위순회
# def inorder_traverse(T):
#     if T:
#         inorder_traverse(T.left)
#         visit(T)
#         inorder_traverse(T.left)

# 후위순회
# def postorder_traverse(T):
#     if T:
#         postorder_traverse(T.left)
#         postorder_traverse(T.left)
#         visit(T)

'''
배열을 이용한 이진트리 표현의 단점
편향이진트리의 경우 사용하지 않는 원소 배열에 대한 메모리 공간 낭비 발생
트리 중간에 새로운 원소 삽임이나 기존노드 삭제시 배열 크기변경이 어려워 비효율적
보완책: 연결리스트
이진트리의 모든 노드는 최대 2개의 자식노드를 가지므로 일정한 구조의 단순 연결 리스트 노드로 구현
'''
'''
이진트리 표현에 대하여 전위순회하여 정점의 번호를 출력하시오
13
1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13
'''
#
# def preorder(i):
#     if i:
#         print(i,end=' ')
#         preorder(left[i])
#         preorder(right[i])
#     return
#
# def inorder(i):
#     if i:
#         inorder(left[i])
#         print(i, end=' ')
#         inorder(right[i])
#     return
#
# def postorder(i):
#     if i:
#         postorder(left[i])
#         postorder(right[i])
#         print(i, end=' ')
#     return
#
# # V: 정점의 개수
# V=int(input())
# arr=list(map(int,input().split()))
# E=V-1   # 간선 수
# left=[0]*(V+1)  # 부모를 인덱스로 왼쪽 자식 저장
# right=[0]*(V+1) # 부모를 인덱스로 오른쪽 자식 저장
# par=[0]*(V+1)   # 자식을 인덱스로 부모저장
# for i in range(E):
#     #p:부모, c:자식
#     p,c=arr[i*2], arr[i*2+1]
#     if left[p]==0:
#         left[p]=c
#     else:
#         right[p]=c
#     par[c]=p
# root=1
# while par[root]!=0: #root찾기
#     root+=1
# preorder(root)
# print()
# inorder(root)
# print()
# postorder(root)


'''
수식트리
수식을 표현하는 이진트리
연산자는 루트노드이거나 가지노드
피연산자는 모두 잎노드
'''

'''
이진탐색트리
탐색작업을 효율적으로 하기위한 자료구조
모든원소는 서로 다른 유일한 키를 갖는다.
key(왼쪽 서브트리)<key(루트노드)<key(오른쪽 서브트리)
왼쪽서브트리에는 루트보다 작은 값 
오른쪽 서브트리에는 루트보다 큰 값
왼쪽 서브트리와 오른쪽 서브트리도 이진탐색트리다.
중위순회하면 오름차순으로 정렬된 값을 얻을 수 있다.
탐색,삽입,삭제시간은 트리의높이만큼 시간이걸린다.
시간복잡도: O(logN)
최악의 경우:O(N)-한쪽으로 치우친 이진트리

'''

'''
힙(Heap)
우선순위큐 구현이 가능
완전이진트리에 있는 노드 중에서 키값이 가장 큰 노드나 키값이 가장 작은 노드를 찾기 위해서 만든 자료구조
최대힙(max heap)
-키값이 가장 큰 노드를 찾기 위한 완전이진트리
-부모노드의 키값 > 자식노드의 키값
-루트노드: 가장 키값이 큰 노드
최소힙(min heap)
-키값이 가장 작은 노드를 찾기 위한 완전이진트리
-부모노드의 키값 < 자식노드의 키값
-루트노드: 가장 키값이 작은 노드

힙연산의 삭제:
-루트노드의 원소만을 삭제할 수 있다.
-루트노드의 원소를 삭제하여 반환한다.
-힙의 종류에 따라 최대값 또는 최소값을 구할 수 있다.
'''

#최대 100개의 key
#최대힙

def enq(n):
    global last
    last+=1         #완전이진트리에 마지막 정점을 추가하고
    heap[last]=n    # 마지막 정점에 저장
    c=last          # 부모가 있고 부모>자식 조건 검사 위해
    p=c//2

    while p>0 and heap[p]<heap[c]:
        heap[p],heap[c]=heap[c],heap[p]
        c=p     #옮긴 자리에서 부모와 비교하기 위해
        p=c//2
    return

def deq():
    global last
    tmp=heap[1]         #루트 임시저장
    heap[1]=heap[last]  # 마지막 정점의 값을 루트로 이동
    last-=1             #마지막 정점 삭제
    p=1
    c=p*2           #왼쪽 자식번호
    while c <=last: #자식이 하나이상 있으면
        if c+1 <= last and heap[c] < heap[c+1]: #오른쪽자식도 있고 오른쪽 자식의 키가 크면
            c+=1        #비교대상을 오른쪽 자식으로 변경
        if heap[c] > heap[p]:
            heap[c], heap[p]=heap[p], heap[c]
            p=c
            c=p*2
        else:
            break
    return tmp


heap=[0]*101    #완전이진트리 1~100번 인덱스 준비
last=0          #완전이진트리의 마지막정점번호

enq(5)
print(heap[1])
enq(15)
print(heap[1])
enq(8)
print(heap[1])
enq(20)
print(heap[1])


while last>0:
    print(deq())