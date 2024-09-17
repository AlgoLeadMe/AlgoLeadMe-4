import sys, heapq

input = sys.stdin.readline
# 행렬의 크기를 입력받음
N = int(input())  
min_heap = []

for _ in range(N):
    row = list(map(int, input().split()))
    
    # 첫 번째 입력 시 힙을 초기화 함
    if not min_heap:
        for num in row:
            heapq.heappush(min_heap, num)
    else:
        for num in row:
            # 힙의 최솟값보다 현재 숫자가 크다면
            if min_heap[0] < num: 
                heapq.heappush(min_heap, num)
                # 힙의 크기를 N으로 유지함
                heapq.heappop(min_heap)  

# N번째 큰 수를 출력함
print(min_heap[0])