# BOJ2252 줄 세우기
from collections import deque

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
indegree = [0] * (n + 1) # 진입 차수 저장할 리스트

for i in range(m):
    s,e = map(int, input().split())
    graph[s].append(e) # zz
    indegree[e] += 1 # 진입 차수 데이터를 저장

# B를 하기 위해 A라는 작업을 먼저 해야 하는 구조가 있을 때, 
# 그 작업 순서를 구해주는 것 = 위상정렬 

queue = deque()
for i in range(1, n + 1):
    if not indegree[i]:
        queue.append(i)

while queue: # 위상 정렬 수행 , 진입 차수 없애!
    now = queue.popleft()
    print(now, end=' ')

    for next in graph[now]:
        indegree[next] -= 1 # 진입 차수 0인 정점 큐에 삽입
        if not indegree[next]:
            queue.append(next)