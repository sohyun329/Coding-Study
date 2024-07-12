import sys
from collections import deque

T = int(sys.stdin.readline())

def priority_order(n, m, priorities):
    # (우선순위, 위치)를 가지는 우선순위 큐로 변경
    queue = deque([(pri, idx) for idx, pri in enumerate(priorities)])
    print_order = 0 # 인쇄 순서 추적

    # 우선순위 높은거 먼저 정렬되도록 반복
    while queue:
        current = queue.popleft()
        if any(current[0] < item[0] for item in queue):
            queue.append(current)
        else:
            print_order += 1
            if current[1] == m:
                return print_order

for _ in range(T):
    n, m = map(int, sys.stdin.readline().strip().split())
    priorities = list(map(int, sys.stdin.readline().strip().split()))
    
    answer = priority_order(n, m, priorities)
    print(answer)
