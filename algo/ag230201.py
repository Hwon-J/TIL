# 옷가게 할인 받기
#주의: 정수를 리턴할 것
def solution(price):
    if price>=500000:
        return int(price*0.8)
    elif price>=300000:
        return int(price*0.9)
    elif price>=100000:
        return int(price*0.95)
    else:
        return int(price)

# 아이스 아메리카노
def solution(money):
    coffee=money//5500
    cha=money%5500
    return coffee, cha

# 배열 뒤집기
def solution(num_list):
    lst=reversed(num_list)
    return lst

# 문자열 뒤집기
def solution(my_string):
    lst=list(my_string)
    rever=reversed(lst)
    ans=''.join(rever)
    return ans

# 직각삼각형 출력하기
n = int(input())
for i in range(n):
    for j in range(i+1):
        print('*',end='')
    print()

# 문자 반복 출력하기
def solution(my_string, n):
    lst=list(my_string)
    new=[]
    for i in lst:
        for _ in range(n):
            new.append(i)
    ans=''.join(new)
    return ans

# 다음에 올 숫자
def solution(common):
    if common[1]-common[0]==common[2]-common[1]:
        min=common[1]-common[0]
        return common[-1]+min
    elif common[1]/common[0]==common[2]/common[1]:
        rlt=common[1]//common[0]
        return common[-1]*rlt


