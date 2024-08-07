import sys
input = sys.stdin.readline

board = [list(map(int,input().split())) for i in range(5)]
visited = [[0]*5 for _ in range(5)]
dx, dy = [0,0, -1, 1], [-1, 1, 0, 0]
s_x,s_y = map(int,input().split())
cnt = 99999

def OOB(x,y):
    return 0 <= x < 5 and 0 <= y < 5
def dfs(x,y,apple, dist):
    global cnt
    # 사과를 3개 가져가면 return - 이동 횟수 저장 및 초기화

    if apple == 3:
        cnt = min(cnt,dist)
        return 

    for d_x, d_y in zip(dx,dy):
        nx = x + d_x
        ny = y + d_y
        if OOB(nx,ny) and not visited[nx][ny] and board[nx][ny] != -1 :
            # 일단 한번 가봐야하니까 방문 찍고 탐색
            visited[nx][ny] = 1
            if board[nx][ny]:
                apple += 1
                apple_status = True

            else:
                apple_status = False

            dfs(nx, ny, apple ,dist + 1)

            # *지나온 길은 다시 되돌아갈 수 없고*, -1의 경우에는 아예 지나갈 수 없다
            # -> 탐색만 하고 다시 원상태로 돌아와야함 (백트래킹)
            visited[nx][ny] = 0

            # 백트래킹을 할 때는 특정 칸을 탐색한 후에 그 칸을 초기 상태로 되돌려 줘야 한다.
            if apple_status:
                apple -= 1
    return


visited[s_x][s_y] = 1
dfs(s_x,s_y,0,0)
print(cnt if cnt != 99999 else -1)


# 삽질 코드
# import sys
# from collections import deque
# input = sys.stdin.readline
#
# board = [list(map(int,input().split())) for i in range(5)]
# dx, dy = [0,0, -1, 1], [-1, 1, 0, 0]
# s_x,s_y = map(int,input().split())
# cnt = []
#
# def OOB(x,y):
#     return 0 <= x < 5 and 0 <= y < 5
#
# def bfs(x,y):
#     global cnt
#     queue = deque([(x,y)])
#
#     apple = 0
#     # 큐가 빌 때까지 반복
#     while queue:
#         x, y = queue.popleft()
#
#         for d_x, d_y in zip(dx,dy):
#             nx = x + d_x
#             ny = y + d_y
#
#             if OOB(nx,ny) and board[nx][ny] != -1:
#                 if board[nx][ny]:
#                     apple += 1
#                     if apple == 3:
#                         cnt.append(board[x][y] + 1)
#
#                 board[nx][ny] = board[x][y] + 1
#                 queue.append((nx, ny))
#     return
# bfs(s_x, s_y)
# print(cnt)