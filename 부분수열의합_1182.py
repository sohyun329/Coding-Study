import sys

N, S = map(int, sys.stdin.readline().split())
num_list = list(map(int, sys.stdin.readline().split()))
cnt = 0

def solve(start, temp):
    global cnt
    
    if temp == S and start > 0 :
        cnt += 1
        
    for i in range(start, N):
        solve(i+1, num_list[i]+temp)
    
    return cnt

print(solve(0,0))
        