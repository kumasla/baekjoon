n,k = map(int,input().split())

coin = []
for i in range(n):
    coin.append(int(input()))

coin.sort()

temp = n-1
count = -1
while True:
    if k - coin[temp] == 0:
        break
    while True:
        if k - coin[temp] <= -1:
            temp -= 1
            break
        else:
            k -= coin[temp]
            count += 1

print(count)