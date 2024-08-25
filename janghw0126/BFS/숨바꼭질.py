import sys
from collections import deque

def bfs_find_min_time(start, target, max_pos):
    # BFS를 위한 큐를 생성함
    queue = deque([start])
    
    while queue:
        current_pos = queue.popleft()
        
        # 현재 위치가 목표 위치와 같으면, 거리 배열에서 시간을 출력함
        if current_pos == target:
            print(time_taken[current_pos])
            return

        # 반복문을 통해 이동할 수 있는 세 가지 경우를 고려함
        for next_pos in (current_pos - 1, current_pos + 1, current_pos * 2):
            # 다음 위치가 범위 내에 있고 아직 방문하지 않은 위치일 경우
            if 0 <= next_pos <= max_pos and time_taken[next_pos] == 0:
                # 현재 위치에서 1초가 추가된 시간을 저장함
                time_taken[next_pos] = time_taken[current_pos] + 1
                # 다음 위치를 큐에 추가함
                queue.append(next_pos)

# 초기 설정을 함 (문제에서 주어진 최대 위치 값을 뜻함)
MAX_POSITION = 100000
# 수빈이의 시작 위치 n과 동생의 위치 k를 입력받음
n, k = map(int, sys.stdin.readline().split())
# 각 위치까지 걸리는 시간을 기록하는 배열을 초기화함
time_taken = [0] * (MAX_POSITION + 1) 

# BFS를 실행함
bfs_find_min_time(n, k, MAX_POSITION)