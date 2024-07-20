import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
miro = [list(map(int, sys.stdin.readline().strip())) for _ in range(N)]

def bfs(miro, x, y):
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    
    queue = deque([(x,y)])
    
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            
            if nx<0 or nx>=M or ny<0 or ny>=N:
                continue
            
            if miro[ny][nx] == 1:
                miro[ny][nx] = miro[y][x]+1
                queue.append((nx,ny))
                
    return miro[N-1][M-1]

print(bfs(miro, 0, 0))