T = int(input())

for _ in range(T) :
    a,b = 1,0
    n = int(input())

    for i in range(n) :
        a,b = b, b+a
    
    print(a , b)
