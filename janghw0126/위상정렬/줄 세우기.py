import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())

# 그래프와 진입 차수 리스트를 초기화함
graph = [[] for _ in range(n + 1)]
deg = [0] * (n + 1)
q = deque()
res = []

# 비교 관계 입력과 그래프를 구성함
for _ in range(m):
    u, v = map(int, sys.stdin.readline().rstrip().split())
    # u가 v 앞에 서야 함
    graph[u].append(v)
    # v의 진입 차수를 증가시킴
    deg[v] += 1

# 진입 차수가 0인 노드 큐에 삽입함
for i in range(1, n + 1):
    if deg[i] == 0:
        q.append(i)

# 위상 정렬을 시작함
while q:
    # 진입 차수가 0인 노드를 큐에서 꺼냄
    cur = q.popleft()
    # 결과 리스트에 추가함
    res.append(cur) 
    
    # 현재 노드 뒤에 서야 하는 노드들의 진입 차수를 감소시킴
    for next_node in graph[cur]:
        deg[next_node] -= 1
        # 진입 차수가 0이 되면 큐에 추가함
        if deg[next_node] == 0:
            q.append(next_node)

print(*res)