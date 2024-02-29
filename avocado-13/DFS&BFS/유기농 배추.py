#--------------------------------------------------------
#  1. visited 배열을 활용한 정석 풀이
# import sys
# sys.setrecursionlimit(10**6)
# input = sys.stdin.readline
# MAX = 50 + 10 # 가로와 세로의 최댓값이 50이므로 넉넉하게 + 10

# dirR = [-1,1,0,0]
# dirC = [0,0,1,-1]

# def dfs(x,y):
#     global visited
#     visited[x][y] = True
#     for dirIdx in range(4):
#         newX = x + dirR[dirIdx]
#         newY = y + dirC[dirIdx]
#         if graph[newX][newY] and not visited[newX][newY]:
#             dfs(newX,newY)


# # 0. 입력 및 초기화
# T = int(input())
# for _ in range(T):
#     M,N,K = map(int,input().split())
#     graph = [[False] * MAX for _ in range(MAX)]
#     visited = [[False] * MAX for _ in range(MAX)]

#     # 1. 그래프 정보 입력
#     for _ in range(K):
#         x, y = map(int,input().split())
#         graph[y+1][x+1] = True #(1,1) 부터 시작하는 것이 range 체크를 안해도 되어서 간결하다. 
    
#     # 2, 방문하지 않은 지점부터 dfs 풀기 
#     answer = 0 
#     for i in range(1, N+1):
#         for j in range(1, M+1):
#             if graph[i][j] and not visited[i][j]:
#                 dfs(i,j)
#                 answer += 1

#     print(answer)
#--------------------------------------------------------

# 2. graph 배열만 활용한 풀이
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
MAX = 50 + 10 # 가로와 세로의 최댓값이 50이므로 넉넉하게 + 10

dirR = [-1,1,0,0]
dirC = [0,0,1,-1]

def dfs(x,y):
    graph[x][y] = False
    for dirIdx in range(4):
        newX = x + dirR[dirIdx]
        newY = y + dirC[dirIdx]
        if graph[newX][newY] and not visited[newX][newY]:
            dfs(newX,newY)


# 0. 입력 및 초기화
T = int(input())
for _ in range(T):
    M,N,K = map(int,input().split())
    graph = [[False] * MAX for _ in range(MAX)]

    # 1. 그래프 정보 입력
    for _ in range(K):
        x, y = map(int,input().split())
        graph[y+1][x+1] = True #(1,1) 부터 시작하는 것이 range 체크를 안해도 되어서 간결하다. 
    
    # 2, 방문하지 않은 지점부터 dfs 풀기 
    answer = 0 
    for i in range(1, N+1):
        for j in range(1, M+1):
            if graph[i][j]:
                dfs(i,j)
                answer += 1

    print(answer)