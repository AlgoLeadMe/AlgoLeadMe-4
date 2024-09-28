import sys
from collections import deque
input = sys.stdin.readline

n = int(input().strip())
queue = deque([i for i in range(1, n+1)])
result = []

while len(queue) > 1:
    result.append(queue.popleft())
    queue.append(queue.popleft())
else:
    result.append(queue.popleft())
print(" ".join(map(str, result)))