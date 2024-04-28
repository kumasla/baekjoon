a = [int(input()) for _ in range(9)]
a.sort()
total = sum(a) - 100

i,j = 0, 8
while i < j :
    if a[i] + a[j] == total : break
    elif a[i] +a[j] < total : i += 1
    else : j -= 1

for x in range(9) :
    if x != i and x != j : print(a[x])            