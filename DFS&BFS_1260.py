import sys
from collections import deque

def DFS(graph, v, visited):
    # 현재 노드 방문 처리
    visited[v] = True
    print(v, end= ' ')
    for i in sorted(graph[v]):
        if not visited[i]:
            DFS(graph, i, visited)
    
    
def BFS(graph, v, visited):
    queue = deque([v])
    # 현재 노드 방문 처리
    visited[v] = True
    while queue:
        node = queue.popleft()
        print(node, end=' ')
        for i in sorted(graph[node]):
            if not visited[i]:
                queue.append(i)
                visited[i] = True
    
    
N, M, V = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(N+1)]

# 간선 입력
for _ in range(M):
    n1, n2 = map(int, sys.stdin.readline().split())
    graph[n1].append(n2)
    graph[n2].append(n1)
    
visited = [False]*(N+1)
DFS(graph, V, visited)
print()
visited = [False]*(N+1)
BFS(graph, V, visited)