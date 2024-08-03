import sys

n = int(sys.stdin.readline())
games = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]
dp = [[0]*(n) for _ in range(n)]
dp[0][0] = 1

for i in range(n):
    for j in range(n):
        if i == n-1 and j == n-1 : 
            print(dp[i][j])
            
        now = games[i][j]
        
        if i+now < n :
            dp[i+now][j] += dp[i][j]
        if j+now < n :
            dp[i][j+now] += dp[i][j]
            