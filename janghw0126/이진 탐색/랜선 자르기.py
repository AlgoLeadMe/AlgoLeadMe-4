import sys

# 입력 처리
K, N = map(int, sys.stdin.readline().strip().split())
cables = [int(sys.stdin.readline().strip()) for _ in range(K)]

# 이진 탐색 범위 설정
low, high = 1, max(cables)

while low <= high:
    mid = (low + high) // 2
    # mid 길이로 자른 랜선 개수 합산
    count = sum(cable // mid for cable in cables)

    if count >= N:
        low = mid + 1
    else:
        high = mid - 1

# 최대 길이 출력
print(high)