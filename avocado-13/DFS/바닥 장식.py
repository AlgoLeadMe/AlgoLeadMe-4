n, m = map(int, input().split())
graph = []
visited = [[0 for _ in range(m)] for _ in range(n)]

for _ in range(n):
    graph.append(list(input()))

def dfs_row(x, y):
    if x >= n or x < 0 or y >= m or y < 0 or visited[x][y] == 1:  # 범위를 확인하고 visited 체크
        return False
    if graph[x][y] == '-':
        visited[x][y] = 1
        dfs_row(x, y - 1)
        dfs_row(x, y + 1)
        return True
    return False 

def dfs_col(x, y):
    if x >= n or x < 0 or y >= m or y < 0 or visited[x][y] == 1:  # 범위를 확인하고 visited 체크
        return False
    if graph[x][y] == '|':
        visited[x][y] = 1
        dfs_col(x - 1, y)
        dfs_col(x + 1, y)
        return True
    return False 

result = 0
for i in range(n):
    for j in range(m):
        if dfs_row(i, j) or dfs_col(i, j):  # dfs_row 또는 dfs_col 중 하나라도 True라면 result 증가
            result += 1 

# 방문하지 않은 모든 영역을 하나의 판자로 처리해주어야 합니다.
for i in range(n):
    for j in range(m):
        if visited[i][j] == 0:
            result += 1

print(result)
