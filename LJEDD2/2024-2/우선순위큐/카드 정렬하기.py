import sys
import heapq
input = sys.stdin.readline

cards = list(int(input()) for _ in range(int(input().strip()))) # 데이터 입력받음
heapq.heapify(cards) # 리스트를 힙구조로 바꿔주는 함수

result = 0
while len(cards) > 1 : 
    f = heapq.heappop(cards) # 첫번째 뭉탱이
    s = heapq.heappop(cards) # 두번째 뭉탱이 
    
    result += f+s
    
    # 바꿔치기 횟수가 최소가 되게끔 
    heapq.heappush(cards, f+s)
    
print(result)