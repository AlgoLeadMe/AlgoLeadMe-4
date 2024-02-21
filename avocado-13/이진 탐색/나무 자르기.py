n, m = map(int, input().split())
trees = list(map(int, input().split()))

start, end = 0, max(trees)  # 시작 높이는 0, 최대 높이는 나무 중 최대 높이로 설정

result = 0

while start <= end:
    mid = (start + end) // 2  # 중간 높이 계산

    total = 0
    for tree in trees:
        # 중간 높이보다 나무가 높으면 잘라야 하는 부분을 더해줌
        if tree > mid:
            total += tree - mid

    # 잘라야 하는 나무의 합이 목표치보다 크거나 같으면 높이를 높여서 확인
    if total >= m:
        result = mid  # 현재 높이를 기록
        start = mid + 1  # 다음 높이는 현재 높이보다 큰 부분에서 찾음
    else:
        end = mid - 1  # 목표치에 도달하지 못했으므로 높이를 줄여서 확인

print(result)
