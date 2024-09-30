import sys, heapq
input = sys.stdin.readline

n = int(input())
heap = []

for _ in range(n):
    for number in map(int, input().split()):
        
        if len(heap) < n: # 비교 대상이 모자랄 경우 
            heapq.heappush(heap, number) #그대로 추가 
            
        else:
            if number > heap[0]: # 제일 작은것보다 크면 
                heapq.heapreplace(heap, number) #작은거 빼고 큰거 넣어줌 
                
print(heap[0]) # 맨앞에 있는게 N번째로 큰놈 