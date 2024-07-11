import sys

T = int(sys.stdin.readline())

for _ in range(T):
    stack = []
    ps = sys.stdin.readline().strip()
    is_vps = True
    
    for p in ps:
        if p == "(":
            stack.append(p)
        elif p == ")":
            if stack:
                stack.pop()
            else:
                is_vps = False
                break
            
    if stack or is_vps == False :
        print("NO")
    else:
        print("YES")
    
