import sys
import heapq

def solve():
    input = sys.stdin.readline
    T = int(input())
    
    for _ in range(T):
        min_heap = []   # 최소 힙
        max_heap = []   # 최대 힙 (음수로 변환하여 저장)
        count = int(input())  # 명령어 수
        status = [1] * count  # 작업 상태 추적 (1: 유효, 0: 삭제됨)
        
        for i in range(count):
            command, value = input().split()
            value = int(value)
            
            if command == "I":  # 삽입 연산
                heapq.heappush(min_heap, (value, i))
                heapq.heappush(max_heap, (-value, i))
            elif command == "D":  # 삭제 연산
                if value == -1:  # 최소값 삭제
                    if min_heap:
                        status[heapq.heappop(min_heap)[1]] = 0
                elif value == 1:  # 최대값 삭제
                    if max_heap:
                        status[heapq.heappop(max_heap)[1]] = 0
            
            # 유효하지 않은 값 제거
            while min_heap and status[min_heap[0][1]] == 0:
                heapq.heappop(min_heap)
            while max_heap and status[max_heap[0][1]] == 0:
                heapq.heappop(max_heap)
        
        # 결과 출력
        if not min_heap or not max_heap:
            print("EMPTY")
        else:
            print(-max_heap[0][0], min_heap[0][0])

if __name__ == "__main__":
    solve()