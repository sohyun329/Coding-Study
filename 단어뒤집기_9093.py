import sys

T = int(sys.stdin.readline())

for _ in range(T):
    sentence = list(sys.stdin.readline().strip().split())
    stack = [''.join(reversed(word)) for word in sentence]
    print(' '.join(stack))
