import sys
input = sys.stdin.readline

#가로 블럭 수, 세로 블럭 수, 인벤토리 블럭 수
row, col, inventory = map(int, input().split())

#땅의 높이 리스트
blocks = []
for i in range(row):
    blocks += list(map(int, input().split()))


min_time = float('inf') #최소시간 초기화
ans_height = blocks[0] #최대높이 초기화
blocks_out = sum(blocks) #놓여진 땅의 높이의 총 합

#가장 높은 땅부터 순환
for target_h in range(max(blocks), min(blocks)- 1, -1):
    # (주어진 총 블럭수 + 인벤토리 블럭 수)가 (현재 높이*가로*세로 블럭 개수)보다 많거나 같을 때
    if blocks_out + inventory >= target_h * row * col:
        #걸리는 시간 초기화
        time = 0
        for b in blocks:
            #현재 위치 블럭개수와 기준 높이와의 차
            diff = b - target_h
            #기준 높이보다 블럭개수가 많을 때
            if diff > 0:
                time += diff * 2
            #기준 높이보다 블럭개수가 적을 때
            elif diff < 0:
                time -= diff * 1
        #최소시간과 걸린 시간 비교
        if time < min_time:
            min_time = time
            ans_height = target_h
#출력
print(min_time, ans_height)
