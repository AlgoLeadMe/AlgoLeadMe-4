import sys

# 깊이 우선 탐색 함수
def dfs(node, cnt):
    # 방문 표시
    check[node] = 1
    # 현재 노드와 연결된 모든 노드에 대해
    for n in graph[node]:
        # 방문하지 않았다면
        if check[n] == 0:
            # 깊이 우선 탐색을 수행하며 연결된 노드의 수를 증가시킴
            cnt = dfs(n, cnt+1)
    return cnt

# 테스트 케이스 수 만큼 반복
for _ in range(int(sys.stdin.readline())):
    # 국가의 수 N과 비행기의 종류 M 입력
    N, M = map(int, sys.stdin.readline().split())
    # 그래프 초기화
    graph = [[] for _ in range(N+1)]
    # 비행 스케줄 입력
    for _ in range(M):
        u, v = map(int, sys.stdin.readline().split())
        graph[u].append(v)
        graph[v].append(u)
    # 방문 여부 체크를 위한 리스트 초기화
    check = [0]*(N+1)
    # 첫 번째 노드 방문 표시
    check[1] = 0
    # 깊이 우선 탐색 수행하여 필요한 비행기 종류 수 계산
    cnt = dfs(1, 0)
    # 결과 출력
    print(cnt)
