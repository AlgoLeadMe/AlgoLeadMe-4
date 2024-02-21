n = int(input())
board = [list(map(int,input().split())) for _ in range(n)]
scores = {-1:0,0:0,1:0}

def search(r,c,size):
    prev = board[r][c]
    for i in range(r, r+size):
        for j in range(c, c+size):

            # 이전 값이랑 다르면 9개로 분할해서 각각 비교
            if board[i][j] != prev:

                # row와 col를 3등분하여 총 9등분
                d = size // 3

                for k in range(3):
                    # 예를 들자면, 81 -> 9 -> 1 ... 순으로 
                    # 9개의 면으로 9등분한 뒤 각각 탐색하여 모든 칸이 같은 숫자로 저장된 종이가 있는지 확인
                    search(r + (d*k), c , d)
                    search(r + (d*k), c + d, d)
                    search(r + (d*k), c + (2 * d), d)
                return
            
    # 더 이상 분할되지 않으면 ( = 저장된 모든 값들이 같은 값일 경우 or 모두 다를 경우 1x1칸 짜리의 개수)
    # 저장된 숫자 카운트
    scores[prev] += 1

search(0,0,n)
print(*scores.values(), sep='\n')