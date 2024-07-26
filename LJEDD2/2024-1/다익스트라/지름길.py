import sys
import heapq
input = sys.stdin.readline

INF = 1e9
n, d = map(int,input().split())
graph = [[] for _ in range(d+1)]

#  거리를 저장하기 위한 배열을 만들고 INF값으로 초기화
min_dist = [INF] * (d+1)
for i in range(d):
    graph[i].append((i+1, 1)) # 각 노드에 대해 거리 1로 연결된 간선 추가
    
# 간선 정보 입력 및 그래프에 추가
for _ in range(n):
    s, e, l = map(int,input().split())
    # 정점 간의 인접 리스트와 정점까지의 거리를 담은 배열을 입력받고 저장
    if e <= d:
        graph[s].append((e,l))

# 다익스트라 - 시작은 0부터
queue = []
heapq.heappush(queue, (0, 0))

# 초깃값
# 시작 노드의 최소 거리 초기화
min_dist[0] = 0

# 다익스트라 탐색
while queue:
    dist, nowX = heapq.heappop(queue)

    # 최소 경로를 가진 노드 찾고 업데이트하기
    if dist <= min_dist[nowX]:
        for next_step in graph[nowX]:
            # 현재 노드와 연결된 모든 노드에 대해 반복
            cost = dist + next_step[1]
            if cost < min_dist[next_step[0]]:
                # 새로운 거리가 기존의 최소 거리보다 작으면 업데이트하고 큐에 추가
                min_dist[next_step[0]] = cost
                heapq.heappush(queue, (cost, next_step[0]))

# 도착점 결과 출력
print(min_dist[d])



