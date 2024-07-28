# 사용자 입력 받기: N, row, col
N, row, col = map(int, input().split())

# 정답 변수 초기화
result = 0

# N이 0이 될 때까지 반복
while N != 0:
    N -= 1

    # 2사분면
    if row < 2 ** N and col < 2 ** N:
        result += (2 ** N) * (2 ** N) * 0  # 2사분면은 추가값이 없음

    # 1사분면
    elif row < 2 ** N and col >= 2 ** N:
        result += (2 ** N) * (2 ** N) * 1  # 1사분면은 첫 번째 사분면의 추가값
        col -= (2 ** N)  # 열 인덱스 조정

    # 3사분면
    elif row >= 2 ** N and col < 2 ** N:
        result += (2 ** N) * (2 ** N) * 2  # 3사분면은 두 번째 사분면의 추가값
        row -= (2 ** N)  # 행 인덱스 조정

    # 4사분면
    else:
        result += (2 ** N) * (2 ** N) * 3  # 4사분면은 세 번째 사분면의 추가값
        row -= (2 ** N)  # 행 인덱스 조정
        col -= (2 ** N)  # 열 인덱스 조정

# 최종 결과 출력
print(result)