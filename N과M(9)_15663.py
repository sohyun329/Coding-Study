import sys

N, M = map(int, sys.stdin.readline().split())
num = sorted(list(map(int, sys.stdin.readline().split())))
visited = [False]*N

result = []

def dfs():
    if len(result) == M:
        print(*result)
        return
    previous = -1
    for i in range(N):
        if previous != num[i] and not visited[i]:
            visited[i] = True
            result.append(num[i])
            previous = num[i]
            dfs()
            visited[i] = False
            result.pop()

dfs()
