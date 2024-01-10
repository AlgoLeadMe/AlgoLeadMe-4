import sys
input = sys.stdin.readline
N = int(input())
check = 0
A = [int(x) for x in input().split()]
stack = [[] for _ in range(4)]

for num in A:
    for j in range(4):
        if len(stack[j]) == 0 or stack[j][-1] < num:
            stack[j].append(num)
            break

for s in stack:
    check += len(s)
    
print("YES" if check==N else "NO")

