x,y = map(int,input().split()) 
z= y*100//x
min = 0
max = 1000000000
if z >= 99 :
    print(-1)
else:
    while min <= max:
        mid =  (min + max ) // 2
        newZ = (y+mid)*100//(x+mid)
        if(newZ > z) :
            result = mid
            max = mid - 1
        else:
            min = mid + 1
    print(result)
