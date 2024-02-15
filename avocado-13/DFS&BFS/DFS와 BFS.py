from collections import deque
# bfs 메서드 정의
def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    result = [start] # 방문한 노드를 저장할 리스트
    while queue:
        v = queue.popleft()
        for i in sorted(graph[v]): # 작은 번호부터 방문하기 위해 정렬
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                result.append(i) # 방문한 노드를 리스트에 저장
    return result

# dfs 메서드 정의
def dfs(graph,start,visited):
    visited[start] = True
    result = [start] # 방문한 노드를 저장할 리스트
    for i in sorted(graph[start]): # 작은 번호부터 방문하기 위해 정렬
        if not visited[i]:
            result.extend(dfs(graph,i,visited)) # 재귀 호출 결과를 리스트에 추가
    return result

# 양방향 리스트 만들기
n,m,start = map(int,input().split())
graph = [[] for i in range(n+1)]
for _ in range(m):
    a,b= map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
    
dfs_visited = [False] * (n+1)
bfs_visited = [False] * (n+1)


print(*dfs(graph, start, dfs_visited)) # 리스트를 언패킹하여 출력
print(*bfs(graph, start, bfs_visited)) # 리스트를 언패킹하여 출력
