import sys
x = list(sys.stdin.readline().strip())
M = list(sys.stdin.readline().strip())
m = len(M)
stack = []

for i in x:
    stack.append(i)
    if stack[len(stack)-m:len(stack)] == M: 
        for _ in range(m): 
            stack.pop()
            
if stack:
    print(*stack, sep='')
else:
    print("FRULA")