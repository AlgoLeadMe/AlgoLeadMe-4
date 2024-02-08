#n 변수에는 컴퓨터의 수를 입력받고, m 변수에는 연결된 간선의 수를 입력받는다.
n = int(input())		
m = int(input())		

#그래프를 표현하기 위해 컴퓨터의 수(n)에 맞게 graph 리스트를 생성한다.
graph = [[] for _ in range(n+1)]
#m번 반복하면서 연결된 간선 정보를 입력받고, 해당 간선 정보를 graph에 추가한다
for _ in range(m):		
    #graph[x]에는 y를, graph[y]에는 x를 추가하여 양방향 그래프를 생성한다.			
    x, y = map(int, input().split())		
    graph[x].append(y)
    graph[y].append(x)
#각 컴퓨터의 방문 여부를 나타내기 위해 visited 리스트를 작성한다.
visited = [0] * (n+1)	
#깊이 우선 탐색을 수행하는 함수인 dfs 함수를 작성한다.
def dfs(graph, v, visited):
    #현재 노드 v를 방문 처리하고, graph[v]에 연결된 노드들을 탐색한다. 
    visited[v] = 1
    for i in graph[v]:
        #해당 노드가 아직 방문되지 않은 경우, 해당 노드를 방문하도록 재귀 호출한다.
        if visited[i] == 0:
            dfs(graph, i, visited)
    return True
#visited 리스트에서 바이러스에 감염된 컴퓨터의 수를 구하기 위해 1의 개수를 세어준다.
dfs(graph, 1, visited)
#최종 결과를 출력해주는데 여기서 -1을 해주는 이유는 시작 노드인 1번 컴퓨터를 제외하기 위해서이다.
print(sum(visited)-1)