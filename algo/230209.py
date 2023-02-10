arr=[list(input()) for _ in range(4)]

for i in range(3):
    for j in range(3,0,-1):
        for k in range(3-j):
            if arr[j][i]=='_':
                arr[j-1][i],arr[j][i]=arr[j][i],arr[j-1][i]
print(arr)
            
