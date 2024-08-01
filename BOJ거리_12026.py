import sys

n = int(sys.stdin.readline())
blocks = sys.stdin.readline().strip()
dp = [1e9]*n
dp[0] = 0

for i in range(n):
    for j in range(i+1,n):
        if dp[i] == -1 : continue
        
        if blocks[i] == 'B' and blocks[j] != 'O':
            continue
        
        elif blocks[i] == 'O' and blocks[j] != 'J':
            continue
        
        elif blocks[i] == 'J' and blocks[j] != 'B':
            continue
        
        else: 
            dp[j] = min(dp[i]+(j-i)**2,dp[j])
            
            
if dp[n-1] == 1e9:
    print(-1)
else:
    print(dp[n-1])