import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

n, m, k, x = map(int, input().split())

graph = [[] for _ in range(n + 1)]
distance = [INF] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)  # 인접 리스트로 그래프 구성

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for next_node in graph[now]:
            cost = dist + 1  # 모든 간선의 거리가 1이므로
            if cost < distance[next_node]:
                distance[next_node] = cost
                heapq.heappush(q, (cost, next_node))

dijkstra(x)

result = [str(i) for i in range(1, n + 1) if distance[i] == k]  # 최단 거리가 k인 도시 번호 리스트

if result:
    print('\n'.join(result))
else:
    print(-1)
