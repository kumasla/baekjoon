N = int(input())
result = 0

a = list(map(int, input().split()))
b = list(map(int, input().split()))

a_index = sorted(range(N), key=lambda i: a[i])
b_index = sorted(range(N), key=lambda i: b[i], reverse=True)

new = [0] * N
for i, (x, y) in enumerate(zip(b_index, a_index)):
    new[x] = a[y]

for i in range(N) : 
    result =  result + (new[i]* b[i])

print(result)