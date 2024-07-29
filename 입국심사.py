import sys

n = int(sys.stdin.readline().strip())
times = list(map(int, sys.stdin.readline().split()))

def solve(n, times):
    answer = 0
    start, end, mid = 1, max(times)*n, 0
    
    # 이분 탐색 : start가 end보다 이하일 때까지 반복
    while start <= end:
        mid = (start+end)//2
        # 심사한 사람 수
        people = 0
        for time in times:
            people += mid//time
        
        # n명 초과 심사 -> 시간 남음
        # n명만 심사했더라도 시간 남을 가능성 존재
        if people>=n:
            end = mid-1
        # n명 미만 심사 -> 시간 부족
        else:
            start = mid+1
            
    answer = start           
    return answer

print(solve(n,times))