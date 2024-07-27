import sys

N = int(sys.stdin.readline().strip())

# 인접한 두 개의 부분 수열이 동일성 판단
def check(seq):
    length = len(seq)
    for l in range(1, length // 2 + 1):
        if seq[-2*l:-l] == seq[-l:]:
            return True
    return False

def solve(temp):
    if len(temp) == N:
        print(''.join(map(str, temp)))
        sys.exit()
    
    for i in [1, 2, 3]:
        temp.append(i)
        if not check(temp):
            solve(temp)
        temp.pop()

solve([])
