import sys
from itertools import combinations

answer = []
# 전체 가능한 게임 결과
games = list(combinations(range(6),2))

def dfs(depth):
    global possible
    
    # 마지막 15번째 게임에 도달했을 때
    if depth == 15 : 
        possible = 1
        for sub in result:
            if sub.count(0) != 3:
                possible = 0
                break
        return
    
    # 전체 경기 15번의 조합
    g1, g2 = games[depth]
    # 각 경기의 승무패 -> 승 : 2, 무 : 1, 패 : 0
    for i,j in ((0,2),(1,1),(2,0)):
        if result[g1][i] > 0 and result[g2][j] > 0 :
            result[g1][i] -= 1
            result[g2][j] -= 1
            dfs(depth+1)
            # 재귀 끝나고 다시 원래대로 복구 -> backtracking / for문의 (0,2), (1,1), (2,0) 모두 탐색하기 위해
            result[g1][i] += 1
            result[g2][j] += 1

for _ in range(4):
    # 입력값
    input_data = list(map(int, sys.stdin.readline().split()))
    # 입력값을 토대로 문제의 예제처럼 표현
    result = [input_data[i:i+3] for i in range(0,16,3)]
    possible = 0
    dfs(0)
    answer.append(possible)
    
print(*answer)

                 
