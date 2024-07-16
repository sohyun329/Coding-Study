import sys
from collections import deque

# 지도 크기
N = int(sys.stdin.readline().strip())

# 지도 정보 입력
map_info = [list(map(int, sys.stdin.readline().strip())) for _ in range(N)]

# BFS 구현
def bfs(start_x, start_y, graph):
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    queue = deque([(start_x, start_y)])
    #graph[start_x][start_y] = 0 # 탐색 시작한 곳 0으로 변경 
    cnt = 1 # 인접한 아파트 수 저장
    
    while queue:
        x,y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            
            if graph[nx][ny] == 1:
                # 방문처리
                graph[nx][ny] = 0
                queue.append((nx,ny))
                cnt += 1
    
    return cnt

info = [bfs(x,y,map_info) for x in range(N) for y in range(N) if map_info[x][y]==1]
print(len(info))
for i in sorted(info):
    print(i)