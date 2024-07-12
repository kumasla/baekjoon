import sys
input = sys.stdin.readline

n = int(input())
dp = list(0 for _ in range(n+1))

for i in range(n) :
    t,p = map(int, input().split(' '))
    dp[i+1] = max(dp[i+1],dp[i])

    if t+i < n +1 :
        dp[i+t] = max(dp[i+t],dp[i]+p)

print(dp[n])