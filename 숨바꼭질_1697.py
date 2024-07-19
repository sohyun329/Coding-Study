import sys
from collections import deque

MAX = 100001

N, K = map(int, sys.stdin.readline().split())
visited = [0]*MAX

def bfs(n):
    queue = deque([n])
    while queue:
        cur = queue.popleft()
        if cur == K :
            return visited[K]
        for i in (cur-1, cur+1, cur*2):
            if 0<=i<MAX and not visited[i]: # queue 방문 중복 방지
                visited[i] = visited[cur]+1
                queue.append(i)
                
print(bfs(N))