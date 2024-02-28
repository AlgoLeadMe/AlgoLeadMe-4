def OOB(x,y):
    return not(0 <= x < r and 0 <= y < c)

def SetBomb():
    for i in range(r):
        for j in range(c):
            # 폭탄이 없다면 폭탄을 설치
            if board[i][j] != 'O':
                board[i][j] = 'O'
            else:
                # 이미 폭탄이 있다면 현재 폭탄 위치 기록
                bombs.append((i,j))

def ExplodeBomb():

    #게임진행
    while bombs:
        x, y = bombs.pop()
        board[x][y] = '.'

        for d_x, d_y in zip(dx, dy):
            nx = x + d_x
            ny = y + d_y
            ## 폭탄이 터지면 동서남북으로 피해가 간다.
            if not OOB(nx, ny) and board[nx][ny] == 'O':
                # 주변을 초토화시킴
                board[nx][ny] = '.'
def Print():
    for i in board: print(*i, sep = "")

r,c,time = map(int, input().split())
board = [list(input()) for _ in range(r)]
dx, dy = [1,0,-1,0],[0,1,0,-1]

# 가장 처음 1초는 입력한 것 (= 현재 상태) 출력
# 2초부터 게임 시작을 위해 -1
time -= 1
bombs = []


while time:
    # 여러 예제를 직접 그리다보면
    # 4초마다 결과가 순환된다는 것을 알 수 있음
    # 폭탄 위치를 기준으로 테두리가 생기고 그 테두리가 함께 터지는 과정이 반복되기 때문에

    time = 4 if not time % 4 else time % 4  # 설치 - 폭발 - 터진 자리 설치 - 폭발 - 기존 상태 의 반복


    # 폭탄 설치 (2초 경과) 및 터질 폭탄 기록
    SetBomb()
    time -= 1

    # 3초가 되었다면 폭탄 터트리고 주변 초토화
    if time:
        ExplodeBomb()
        time -= 1

Print()

