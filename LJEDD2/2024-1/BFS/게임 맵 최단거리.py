from collections import deque
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

def OOB(x, y):
    global maps
    n, m = len(maps), len(maps[0]) # MAP_SIZE = N X M
    # 이동할 위치가 그래프 범위 내에 포함이 되는지 확인
    return 0 <= x < n and 0 <= y < m

def bfs(x, y):
    global maps
    # Queue
    queue = deque([(x, y)])

    while queue:
        x, y = queue.popleft()
        for d_x, d_y in zip(dx, dy):
            # 다음 STEP 이동 (상,하,좌,우)
            nx = x + d_x
            ny = y + d_y

            # 다음 이동 위치가 그래프 내에 있는지,
            # 이동 가능한 (=1) 위치인지를 판단 (0은 이동할 수 없음)
            if OOB(nx, ny) and maps[nx][ny] == 1:
                # 칸 개수 +1 : 1이 아닐 경우 이미 방문했음(계속 ++1)을 알 수 있음
                maps[nx][ny] = maps[x][y] + 1
                #  그 다음 위치
                queue.append((nx, ny))

    # 최소비용 : 마지막 장소 maps[n][m]의 값
    return maps[len(maps) - 1][len(maps[0]) - 1]


def solution(board):
    # 입력 받은 maps 전역변수 선언
    global maps
    maps = board.copy()

    # 너비 우선 탐색 (BFS)
    answer = bfs(0, 0)

    return -1 if answer == 1 else answer # 결과 출력

