input = open(0).readline
board = [list(map(int, input().split())) for _ in range(5)]
visited = [[col == -1 for col in row] for row in board]
r,c = map(int,input().split())

offset = [(-1,0),(0,1),(1,0),(0,-1)]
visited[r][c] = True

def out_of_bound(x: int, y: int) -> bool:
    return not(0 <= x <= 4 and 0 <= y <= 4)

def dfs(x: int, y: int, step: int = 0, apple: int = 0) -> bool:

    # 1 과 0의 경우를 판단
    if apple >= 2 and step <= 3: # 사과 2개를 3 스텝 이내에 먹었다면 참
        return True
    if apple < 2 and step > 3: # 3 스텝이 지날 동안 사과 2개도 못먹었다면 거짓
        return False

    # 4방향 탐색
    for dx, dy in offset:
        nx, ny = x + dx, y + dy

        if out_of_bound(nx, ny) or visited[nx][ny]:
            continue
        visited[nx][ny] = True

        # 이 다음 호출에서 반환되는 값이 참이면 return
        if dfs(nx, ny, step + 1, apple + board[nx][ny]):
            return True

        # 되돌아옴
        visited[nx][ny] = False

    # 만족스러운 답을 찾지 못했을 경우 False 리턴
    return False

print(int(dfs(r, c)))









