t = int(input())

for _ in range(t) :
    m,n,k = map(int,input().split())
    form = [[0] * n for j in range(m)]
    for i in range(k) :
        x, y = map(int,input().split())
        form[x][y] = 1

