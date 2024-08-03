import sys
from collections import deque
input = sys.stdin.readline

# 이동 방향: 상, 하, 좌, 우
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# 그리드의 크기 입력 받기
n, m = map(int, input().split())

# 그리드와 방문 여부 및 거리 배열 초기화
grid = [input().split() for _ in range(n)]
visited = [[False] * m for _ in range(n)]
distance = [[0] * m for _ in range(n)]

# 시작점을 찾고 BFS 초기화
for i in range(n):
    for j in range(m):
        if grid[i][j] == "2":
            visited[i][j] = True
            q = deque([(i, j)])

# BFS 탐색
while q:
    x, y = q.popleft()
    for dx, dy in directions:
        nx = x + dx
        ny = y + dy

        # 그리드 범위 내에 있고, 값이 "1"이며, 아직 방문하지 않은 경우
        if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == "1" and not visited[nx][ny]:
            q.append((nx, ny))
            visited[nx][ny] = True
            distance[nx][ny] = distance[x][y] + 1

# 결과 출력
for i in range(n):
    for j in range(m):
        if not visited[i][j] and grid[i][j] == "1":
            print(-1, end=" ")  # 방문하지 않은 "1"인 경우 -1 출력
        else:
            print(distance[i][j], end=" ")  # 거리 출력
    print()