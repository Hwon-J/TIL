# 중앙값 구하기
def solution(arr):
    a=sorted(arr)
    if len(a) % 2==1:
        rlt=a[len(a)//2]    
    else:
        rlt=(a[len(a)//2-1]+a[len(a)//2])/2
    
    return rlt

# 최빈값 구하기
from collections import Counter
def solution(array):
    rlt=Counter(array)
    arr=sorted(rlt.items(), key=lambda x:x[1], reverse=True)
    if len(arr)==1:
        return array[0]
    elif arr[0][1]==arr[1][1]:
        return -1
    else:
        return arr[0][0]

#짝수는 싫어요
def solution(n):
    odd=[]
    for i in range(1,n+1,2):
        odd.append(i)
    return odd

# 피자 나눠 먹기 (1)
import math
def solution(n):
    rlt=math.ceil(n/7)
    return rlt

# 피자 나눠 먹기(2)
def solution(n):
    for i in range(max(6,n),6*n+1,1):
        if i % 6==0 and i % n ==0:
            rlt=i//6
            return rlt

# 피자 나눠 먹기(3)
def solution(slice, n):
    rlt=((n-1)//slice)+1
    return rlt

# 배열의 평균값
def solution(numbers):
    return sum(numbers)/len(numbers)

# 짝수 홀수 개수
def solution(num_list):
    even=[]
    odd=[]
    for i in num_list:
        if i%2==0:
            even.append(i)
        else:
            odd.append(i)
    
    rlt=[len(even),len(odd)]
    return rlt

# 제곱수 판별하기
def solution(n):
    if n**(1/2)%1==0:
        return 1
    else:
        return 2

# 가까운 수
def solution(array, n):
    lst=[]
    for i in array:
        a=abs(i-n)
        lst.append(a)

    b=sorted(lst)
    if b[0]==b[1]:
        return n-b[0]    
    else:
        pass
# 내일 다시..