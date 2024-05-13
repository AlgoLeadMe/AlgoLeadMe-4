import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
board = [list(input().strip()) for _ in range(N)]

def painting(color):
    prefix_sum = [[0] * (M + 1) for _ in range(N + 1)]

    for i in range(N):
        for j in range(M):
            # 컬러를 비교하여 color와 같은면은 1 다른면은 0으로 표시
            if (i + j) % 2:
                target = int(board[i][j] != color)
            else:
                target = int(board[i][j] == color)
            # 그림으로 설명 가능 이전 행, 이전 열, 이전 대각선 위치의 숫자들의 합 + 흑백 여부 누적합 계산
            prefix_sum[i+1][j+1] = prefix_sum[i][j+1] + prefix_sum[i+1][j] - prefix_sum[i][j] + target

    count = 1e9

    # K×K 체스판일 때의 구간합
    for i in range(1, N-K+2):
        for j in range(1, M-K+2):
            count = min(count,
                        # kxK만큼 잘라 최소로 되는 개수 저장
                        # Range(x1, y1, x2, y2) = S(x2, y2) - S(x1, y2) - S(x2, y1) + S(x1, y1)
                        prefix_sum[i+K-1][j+K-1] - prefix_sum[i+K-1][j-1] - prefix_sum[i-1][j+K-1] + prefix_sum[i-1][j-1])

    return count

print(min(painting('B'), painting('W')))