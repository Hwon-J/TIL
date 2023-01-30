# # 두 수의 합
# def solution(num1, num2):
#     pl=num1+num2
#     return pl

# print(solution(2,3))

# # 두 수의 차
# def solution(num1, num2):
#     mi=num1-num2
#     return mi
# print(solution(2,3))

# # 두 수의 곱
# def solution(num1, num2):
#     answer = num1,num2
#     return answer

# # 몫 구하기
# def solution(num1, num2):
#     answer = num1//num2
#     return answer

# # 두 수의 나눗셈
# def solution(num1, num2):
#     answer = int(num1/num2*1000)
#     return answer

# # 숫자 비교하기
# def solution(num1, num2):
#     if num1==num2:
#         return 1
#     else:
#         return -1

# # 분수의 덧셈
# def solution(numer1, denom1, numer2, denom2):
#     answer_numer = numer1*denom2+numer2*denom1
#     answer_denom = denom1*denom2
    
#     for i in range(min(answer_numer,answer_denom),0,-1):
#         if answer_numer%i==0 and answer_denom%i==0:
#             ma=i
#             break

#     answer=[answer_numer//ma,answer_denom//ma]
#     return answer

# # 배열 두배 만들기
# def solution(numbers):
#     lst=[]
#     for i in numbers:
#         lst.append(i*2)
#     return lst

# # 나머지 구하기
# def solution(num1, num2):
#     answer = num1%num2
#     return answer

# # 나이 출력
# def solution(age):
#     answer = 2022-age+1
#     return answer

# # 각도기
# def solution(angle):
#     if 0 < angle < 90:
#         return 1
#     elif angle==90:
#         return 2
#     elif 90 < angle < 180:
#         return 3
#     elif angle==180:
#         return 4

# # 대문자와 소문자
# def solution(my_string):
#     lst=list(my_string)
#     result=[]
#     for i in lst:
#         if 65<=ord(i)<=90:
#             result.append(chr(ord(i)+32))
#         elif 97<=ord(i)<=122:
#             result.append(chr(ord(i)-32))
#     rlt=''.join(result)
#     return rlt