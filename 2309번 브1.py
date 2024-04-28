a = [0]*9
for i in range(9) : 
    a[i] = int(input())

a = sorted(a)
total = sum(a)
total -= 100

i = 0
j = 1
stop = False
for i in range(8) :
    for j in range(9) :
        if(total == a[i] + a[j]) : 
            stop = True
            break
    
    if(stop == True) : 
        break

for x in range(9) :
    if (x != i and x != j) :
        print(a[x])
            