import sys
from collections import deque

n = int(sys.stdin.readline())
list_a = list(map(int, sys.stdin.readline().split()))  # 0 1 1 0 (0 = queue, 1 = stack)
list_b = list(map(int, sys.stdin.readline().split()))  # 1 2 3 4

m = int(sys.stdin.readline())
list_c = list(map(int, sys.stdin.readline().split()))

res = deque()

for qs in range(n):
    if list_a[qs] == 0:
        res.appendleft(list_b[qs])
        
for i in range(m):
    res.append(list_c[i])
    print(res.popleft(), end=' ')