from collections import deque
import sys
input = sys.stdin.readline

# 테스트 케이스를 입력받음
m, n = map(int, input().split())
tomato_grid = [list(map(int, input().split())) for _ in range(n)]

# 익은 토마토 좌표를 큐에 추가함
queue = deque([(i, j) for i in range(n) for j in range(m) if tomato_grid[i][j] == 1])

# 방향 벡터를 초기화함 (상, 하, 좌, 우)
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# BFS 탐색을 시작함
def bfs():
    while queue:
        x, y = queue.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            # 범위 내에 있고, 익지 않은 토마토(0)일 경우 익힘
            if 0 <= nx < n and 0 <= ny < m and tomato_grid[nx][ny] == 0:
                tomato_grid[nx][ny] = tomato_grid[x][y] + 1
                queue.append((nx, ny))

# BFS를 실행함
bfs()

# 결과를 계산함
days = 0
for row in tomato_grid:
    # 익지 않은 토마토가 있으면 -1을 출력함
    if 0 in row:
        print(-1)
        exit()
    # 가장 큰 값이 걸린 날짜를 계산함
    days = max(days, max(row)) 

# 시작을 1에서 했으므로 결과에서 1을 빼줌
print(days - 1)