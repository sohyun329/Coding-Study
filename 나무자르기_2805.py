import sys

n, m = map(int, sys.stdin.readline().strip().split())
trees = slist(map(int, sys.stdin.readline().split()))

def solve(m,trees):
    answer = 0
    start, end = 0, max(trees)
    
    while start <= end:
        mid = (start+end) // 2
        length = 0
        for t in trees:
            if t > mid:
                length += t - mid
        
        if length >= m :
            answer = mid
            start = mid + 1
        else:
            end = mid - 1
            
    return answer

print(solve(m, trees))
