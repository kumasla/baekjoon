import math

T = int(input())
for i in range(T) : 
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    
    d = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    sum = r1 + r2
    r_abs =abs(r1 - r2)

    if d == 0 and r1 == r2 : 
        point = -1
    elif d == sum or d == r_abs :
        point = 1
    elif r_abs < d and d < sum :
        point = 2
    else : 
        point = 0
    print(point)