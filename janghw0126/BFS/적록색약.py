from collections import deque

n = int(input())
graph = [list(input()) for _ in range(n)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

def bfs(graph, x, y, color):
    queue = deque([(x, y)])
    graph[x][y] = '0'  
    while queue:
        cx, cy = queue.popleft()
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == color:
                graph[nx][ny] = '0'
                queue.append((nx, ny))

def solve():
    graph1 = [row[:] for row in graph]  
    
    count, count1 = 0, 0
    for i in range(n):
        for j in range(n):
            if graph[i][j] != '0':
                bfs(graph, i, j, graph[i][j])
                count += 1
            if graph1[i][j] != '0':
                color = graph1[i][j]
                if color == 'R' or color == 'G':
                    color = 'R'  
                bfs(graph1, i, j, color)
                count1 += 1

    return count, count1

count, count1 = solve()
print(count, count1)
