import sys
from collections import deque

# test case
T = int(sys.stdin.readline().strip())

def make_farm(M,N,K):
    farm = [[0]*M for _ in range(N)]
    
    for _ in range(K):
        X, Y = map(int, sys.stdin.readline().split())
        farm[Y][X] = 1
    
    return farm

def bfs(farm, start_x, start_y, M, N):
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    
    queue = deque([(start_x, start_y)])
    farm[start_y][start_x] = 0
    
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            
            if nx < 0 or nx >= M or ny < 0 or ny >= N:
                continue
            
            if farm[ny][nx] == 1:
                farm[ny][nx] = 0
                queue.append((nx,ny))
                

for _ in range(T):
    M, N, K = map(int, sys.stdin.readline().split())
    farm = make_farm(M,N,K)
    result = 0
    for start_y in range(N):
        for start_x in range(M):
            if farm[start_y][start_x] == 1:
                bfs(farm, start_x, start_y, M, N)
                result += 1
                
    print(result)