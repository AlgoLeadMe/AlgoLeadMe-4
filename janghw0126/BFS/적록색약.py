import sys
from collections import deque

input = sys.stdin.readline

def bfs(x, y, graph, visited):
    q = deque()
    q.append((x, y))
    visited[x][y] = True
    
    # 상하좌우 방향 선언하기
    dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
    
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                # 색상이 같고 방문하지 않은 경우에만 큐에 넣음
                if graph[x][y] == graph[nx][ny]:
                    visited[nx][ny] = True
                    q.append((nx, ny))

n = int(input())
graph = [list(input().strip()) for _ in range(n)]

# 첫 번째 방문 배열은 정상인 (R, G, B 구분함)
visited = [[False] * n for _ in range(n)]
normal_count = 0

# 두 번째 방문 배열은 적록색맹인 (R, G 구분 안 함)
visited_rg = [[False] * n for _ in range(n)]
rg_count = 0

# 정상인 그룹 개수 구하기
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(i, j, graph, visited)
            normal_count += 1

# 적록색맹인 경우 'G'를 'R'로 바꾸기
for i in range(n):
    for j in range(n):
        if graph[i][j] == 'G':
            graph[i][j] = 'R'

# 적록색맹인 그룹 개수 구하기
for i in range(n):
    for j in range(n):
        if not visited_rg[i][j]:
            bfs(i, j, graph, visited_rg)
            rg_count += 1

print(normal_count, rg_count)