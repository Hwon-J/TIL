# # 파이썬 알고리즘 string
#
# # 고지식한 알고리즘
# # 본문 문자열을 처음부터 끝까지 차례로 순회하면서 패턴 내 문자를 일일이 비교
# # 최악의 경우 시간복잡도는  O(MN)이 될 수 있음
# # 불필요한 수행시간을 줄이기위해 KMP알고리즘 탄생
# p = 'ab'    #찾을 패턴
# t= 'aaaabaaaabaaaabab'    #전체문장
# M= len(p)
# N= len(t)
# def bf(p,t,N,M ):
#     i=0     #t에서의 비교위치
#     j=0     #p에서의 비교위치
#     # 비교할 문장이 남아있고 패턴을 찾기 전이면
#     # i가 전체문장길이보다 작고 j가 찾을 패턴 길이보다 작을 때 까지
#     while i < N and j<M:
#         #방법2
#         if t[i] == p[j]:    # 서로 같은 글자를 만나면
#             i+=1            # i와 j에 1씩 더해 다음 순서를 비교한다.
#             j+=1
#         else:       # 아니면 비교를 시작했던 위치에서 1을 더한곳부터 다시 비교
#             i=i-j+1
#             j=0     #찾을 패턴은 첫번째로 리셋
#         # 방법1
#         # if t[i] != p[j]:    # 서로 다른 글자를 만나면
#         #     i -= j      # 비교를 시작한 위치로
#         #     j= -1       # 패턴을 시작한 위치로
#         # i+=1  # 계속 1씩 더하면서 끝까지 검색
#         # j+=1
#     if j==M:    #패턴을 찾은 경우
#         return i-M  #패턴의 시작위치를 찾기 위해 비교 끝점 i에서
#                     # 패넡 길이 M만큼 빼기
#     else:
#         return -1
# print(bf(p,t,N,M))
# # 다른 방식
# # 찾을 패턴길이 M만큼씩 떼어내어 비교할 함수
# def bf2(p,t,N,M):
#     for i in range(N-M+1):
#         for j in range(M):
#             if t[i+j] != p[j]:  # 비교 대상이 서로 다르면 바로 break
#                 break
#         else:   #아니면 시작위치 i리턴
#             return i
#     return -1
# print(bf2(p,t,N,M))
#
#
# # 패턴의 갯수 찾기
# def bf3(p,t,N,M):
#     cnt=0
#     for i in range(N-M+1):
#         for j in range(M):
#             if t[i+j] != p[j]:  # 비교 대상이 서로 다르면 바로 break
#                 break
#         else:   #아니면 cnt에 1더하기
#             cnt+=1
#     return cnt
# print(bf3(p,t,N,M))
#

# 보이어 무어 알고리즘
'''
오른쪽에서 왼쪽으로 비교
대부분의 상용소프트 웨어레서 채택하고 있는 알고리즘
패턴의 오른쪽 끝 문자가 불일치하고 이 문자가 패턴 내에 존재하지 않는 경우
이동거리는 최대 패턴길이만큼 될 수 있다.
'''