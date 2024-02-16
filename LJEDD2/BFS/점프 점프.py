# boj 14248 BFS
from collections import deque

n = int(input())
graph = list(map(int, input().split()))
visited = [0] * n 
start = int(input())-1
cnt = 0

# 그래프 범위를 벗어나는지 체크 
def OOB(x):
    return 0 <= x < n

def bfs(start):
    global cnt
    q = deque([start])
    visited[start] = 1
    cnt += 1

    while q:
        x = q.popleft()

        for d in [-graph[x], graph[x]]:
            nx = x + d
            if OOB(nx) and not visited[nx]:
                q.append(nx)
                cnt += 1
                visited[nx] = 1

bfs(start)
print(cnt)