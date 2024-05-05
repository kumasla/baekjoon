n,k = map(int,input().split())

coin = [0]*n
for x in range(0,n):
    coin[x] = int(input())

dp = [0 for _ in range(k+1)]
dp[0] = 1

for i in range(n):
    for j in range(k+1) :
        if j - coin[i] >= 0 : 
            dp[j] =dp[j]+ dp[j-coin[i]]

print(dp[k])