from collections import deque

n, k = map(int, input().split())

queue = deque()
for i in range(1,n+1) :
    queue.append(i)

answer = []
    
while queue:
    for _ in range(k-1):
        queue.append(queue.popleft())
        
    answer.append(queue.popleft())
    
print("<{}>".format(', '.join((map(str,answer)))))
# print(str(answer).replace('[', '<').replace(']', '>'))