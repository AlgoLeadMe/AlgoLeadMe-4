# BOJ1766 문제집
# 위상정렬 + 우선순위 큐 
 
import heapq

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
indegree = [0] * (n + 1)  # 진입 차수 리스트

for i in range(m):
    s, e = map(int, input().split())
    graph[s].append(e)
    indegree[e] += 1  # 진입 차수 데이터 저장

# 문제에서 가능한 앞 번호의 문제부터 풀어야 함 -> 우선순위큐,,?
# 1~N의 난이도 순 대로

queue = []

# 순서
for i in range(1, n + 1):
    if indegree[i] == 0:
        heapq.heappush(queue, i) # 진입차수가 0인거 먼저 난이도랑 저장

while queue:
    now = heapq.heappop(queue)
    print(now, end=' ')

    for i in graph[now]: # 위상 정렬 수행 , 진입 차수 없애!
        indegree[i] -= 1

        if indegree[i] == 0:
            heapq.heappush(queue, i)