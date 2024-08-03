import sys
from collections import deque
input = sys.stdin.readline

def topological_sort_and_compute_times(n, task_times, dependencies):
    # 그래프와 진입 차수 초기화
    graph = {i: [] for i in range(1, n + 1)}
    indegree = [0] * (n + 1)
    completion_time = [0] * (n + 1)
    
    # 작업 시간 초기화
    for i in range(1, n + 1):
        completion_time[i] = task_times[i]
    
    # 그래프와 진입 차수 설정
    for a, b in dependencies:
        graph[a].append(b)
        indegree[b] += 1
    
    # 진입 차수가 0인 노드를 큐에 추가
    queue = deque()
    for i in range(1, n + 1):
        if indegree[i] == 0:
            queue.append(i)
    
    # 위상 정렬과 작업 완료 시간 계산
    while queue:
        current = queue.popleft()
        for neighbor in graph[current]:
            completion_time[neighbor] = max(completion_time[neighbor], completion_time[current] + task_times[neighbor])
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)
    
    return max(completion_time[1:])

n = int(input().strip())
task_times = [0] * (n + 1)
dependencies = []

# 작업 시간 입력
for i in range(1, n + 1):
    data = list(map(int, input().split()))
    task_times[i] = data[0]
    m = data[1]
    for j in range(m):
        dependencies.append((data[2 + j], i))

print(topological_sort_and_compute_times(n, task_times, dependencies))
