import sys
sys.setrecursionlimit(10**6)

cnt = 0
dx, dy = [-1,1,0,0], [0,0,-1,1]

# dfs 함수 선언
def dfs(x,y):
    global graph
    global countPerDanzi
    countPerDanzi += 1 
    # 방문처리
    graph[x][y] = 0 

    for r,c in zip(dx,dy):
        nx = x + r
        ny = y + c
        # 범위를 벗어나는지 확인 그리고 단지가 있는 곳인지도 확인
        if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] : 
            dfs(nx,ny)

# n 입력받기 
n = int(input())
graph = [[0 for _ in range(n)] for _ in range(n)]

# 그래프 정보 저장 
for row in range(n):
    graph[row] = list(map(int,input()))

countList = []

# 그래프를 탐색하며 dfs 실행 
for i in range(n):
    for j in range(n):
        if graph[i][j] :
            countPerDanzi = 0
            dfs(i,j)
            countList.append(countPerDanzi)

print(len(countList))
countList.sort()
for i in range(len(countList)):
    print(countList[i], end= ' ')
