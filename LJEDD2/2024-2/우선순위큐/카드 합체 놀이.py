import heapq
n, m = map(int,input().split())

#힙 구조로 변환 
numbers = list(map(int,input().split()))
heapq.heapify(numbers)

for _ in range(m):
    
    x = heapq.heappop(numbers)
    y = heapq.heappop(numbers)
    
    # x와 y 둘 다 값 교체 
    heapq.heappush(numbers, x+y)
    heapq.heappush(numbers, x+y)

print(sum(numbers))
