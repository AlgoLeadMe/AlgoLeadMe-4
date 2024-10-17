import sys
input = sys.stdin.readline

n = int(input())
graph = [list(input().strip()) for _ in range(n)]
visited = [[0] * n for _ in range(n)]

for k in range(n):
    for i in range(n):
        for j in range(n):
            if i == j:
                continue

        # 2-친구인 경우
            if graph[i][j] == 'Y' or (graph[i][k] == 'Y' and graph[k][j] == 'Y'):
                visited [i][j] = 1

res = 0
for row in visited:
  res = max(res,sum(row))
print(res)