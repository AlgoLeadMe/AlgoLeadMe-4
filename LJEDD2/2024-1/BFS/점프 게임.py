from collections import deque
from sys import stdin

# Cur_X가 N을 넘어간다면 클리어

n,k = map(int,input().split())
board = [list(map(int, stdin.readline().strip())) for _ in range(2)] # input()을 사용했을 때 답이 안나온다.  
visited = [[0] * n for _ in range(2)]

def OOB(y,time):
    return not(time < y < n) # 그냥 time도 포함해서 접근 가능 범위를 제한해주면 되지 않을까?

def jump(start):
    queue = deque([start])
    time = 0
    while queue:
        # https://dirmathfl.tistory.com/184
        for _ in range(len(queue)): #  한 번에 한 "레벨"씩만 방문
            row,col = queue.popleft()

            # if time > 0:
            #     board[0][time] = 0
            #     board[1][time] = 0
            # if col >= n-1 or col + k >= n:
            #     return True

            for nrow, ncol in ((row, col+1),(row, col-1),(~row, col+k)): # ~ 사용하면 0과 1 스위칭가능
                # 3번 조건에서 막혔다. 
                if ncol >= n:
                    return print(1)

                if not OOB(ncol,time) and board[nrow][ncol] and not visited[nrow][ncol]:
                    visited[nrow][ncol] = 1
                    queue.append((nrow,ncol))

        time += 1
    return print(0)

start = [0,0]
jump(start)

