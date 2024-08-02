import sys

n,s,m = map(int, sys.stdin.readline().strip().split())
v = list(map(int,sys.stdin.readline().strip().split()))
dp = [[False]*(m+1) for _ in range(n+1)]
dp[0][s] = True

for i in range(n):
    for j in range(m+1):
        if dp[i][j] == True:
            n1 = v[i]+j
            n2 = j-v[i]
            
            if n2 >= 0:
                dp[i+1][n2] = True
            if n1 <= m:
                dp[i+1][n1] = True
                
for i in range(m,-1,-1):
    if dp[n][i] == True:
        print(i)
        exit()
else:
    print(-1)