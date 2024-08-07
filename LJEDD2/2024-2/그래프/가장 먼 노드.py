from collections import deque

def solution(n, edge):
    graph = [[] for _ in range(n + 1)]
    visited = [0] * (n + 1)    
    
    # 인접 리스트 방식의 그래프 구현
    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)
    
    queue = deque([(1)]) 
    visited[1] = 1 
    
    while queue:
        x = queue.popleft() 
        for nx in graph[x]:
            if not visited[nx]: # 방문한 적이 없는 경우
                visited[nx] = visited[x] + 1 # 거리 계산 
                queue.append(nx)
    
    max_value = max(visited)
    return visited.count(max_value) # 최댓값을 가지는 요소의 개수