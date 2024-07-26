import sys

L, C = map(int, sys.stdin.readline().split())
alphabet = sorted(list(map(str, sys.stdin.readline().split())))
comp = ['a', 'e', 'i', 'o', 'u']
key = []

def solve(start):
    if len(key) == L:
		# key에 있는 문자 중 comp에 포함된 문자 개수 (모음 개수)
        vowel_count = sum(1 for k in key if k in comp)
        # key에 있는 문자 중 자음 개수는 L - 모음 개수
        consonant_count = L - vowel_count
        # 모음 개수가 1 이상이고 자음 개수가 2 이상일 때
        if vowel_count >= 1 and consonant_count >= 2:
            print(''.join(key))
        return
    
    # alphabet의 첫번째 문자부터 암호 만들기
    for i in range(start, C):
        key.append(alphabet[i])
        solve(i + 1)
        key.pop()

solve(0)
