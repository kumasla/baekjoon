T = int(input())
for i in range(T) : 
    n,m = map(int, input().split())
    temp = 1
    r = 1
    for j in range(m, m-n, -1) :
        temp = temp * j
        temp = temp // r
        r += 1
    
    print(temp)