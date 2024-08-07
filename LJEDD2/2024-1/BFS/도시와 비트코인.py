from collections import deque

m, n = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(n)]
offset = [(0,1),(1,0)]
visited = [[0]*m for _ in range(n)]

def out_of_bound(x,y):
    return not(0 <= x < n and 0 <= y < m)
def bfs(x,y):
    queue = deque([(x,y)])
    visited[x][y] = 1

    while queue:
        x, y = queue.popleft()

        if x == n-1 and y == m-1:
            print("Yes")
            exit()

        for dx,dy in offset:
            nx = x + dx
            ny = y + dy

            if out_of_bound(nx,ny):
                continue
            if board[nx][ny] and not visited[nx][ny]:
                visited[nx][ny] = 1
                queue.append((nx,ny))
bfs(0,0)
print("No")