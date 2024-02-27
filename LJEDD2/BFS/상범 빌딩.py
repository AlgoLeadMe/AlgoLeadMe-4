# 정육면체
# 금으로 이뤄진 부분은 지나갈 수 없다.
# 이동 가능 범위 - 동 서 남 북 상 하 - 6 방향 
# 대각선 X

from collections import deque

# 3차원에서의 이동을 나타내야 함.

# 제자리 - 동 서 남 북
# 상 - 동 서 남 북  # 하 - 동 서 남 북
offset = [(1,0,0),(-1,0,0),(0,-1,0),(0,1,0),(0,0,-1),(0,0,1)]

# 그래프 범위 내 체크 
def OOB(floor,x,y):
    return not(0 <= floor < L and 0 <= x < R and 0 <= y < C)

# 너비 탐색 알고리즘
def bfs(sl,sr,sc):
    visited = [[[0] * C for _ in range(R)] for _ in range(L)]
    visited[sl][sr][sc] = 1

    queue = deque([(sl,sr,sc)])

    while queue:
        # f = floor를 의미 
        f, x, y = queue.popleft()

        for df, dx, dy in offset:
            nf, nx, ny = f + df, x + dx, y + dy

            if not OOB(nf,nx,ny) and not visited[nf][nx][ny] and building[nf][nx][ny] != '#':
                # 탈출 지점일 경우 소요 시간 리턴
                if building[nf][nx][ny] == 'E':
                    return visited[f][x][y]
                
                visited[nf][nx][ny] = visited[f][x][y] + 1
                queue.append((nf,nx,ny))
    return None

#  주어진 빌딩 구조와 출발점 정보를 기반으로 탈출 가능 여부를 판단 
def solve(L, R, C):
    global building
    building = []

    for l in range(L):
        building.append([list(input().rstrip()) for _ in range(R)])
        for r in range(R):
            for c in range(C):
                if building[l][r][c] == "S":
                    sl, sr, sc = l, r, c
        input()

    # 최소 소요 시간 계산 
    time = bfs(sl,sr,sc)
    
    if time:
        return print(f"Escaped in {time} minute(s).")
    else:
        return print('Trapped!')

# MAIN
while True:
    L,R,C = map(int,input().split())

    if not L and not R and not C :
        break

    # 각 케이스별 소요시간을 리턴 
    solve(L, R, C)