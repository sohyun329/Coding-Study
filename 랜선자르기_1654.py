import sys

k,n = map(int, sys.stdin.readline().strip().split())
lan = [int(sys.stdin.readline().strip()) for _ in range(k)]

def solve(n, lan):
    start, end = 1, max(lan)
    answer = 0
    
    while start <= end:
        mid = (start + end) // 2
        cnt = 0
        
        for l in lan:
            cnt += l // mid
        
        if cnt >= n:
            answer = mid
            start = mid + 1
        else:
            end = mid - 1
            
    return answer

print(solve(n, lan))
