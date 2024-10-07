# 전역 변수로 최대 양의 수를 저장
max_count = 0

def solution(info, edges):
    # 각 노드의 자식 노드를 저장할 리스트 초기화
    child = [[] for _ in range(len(info))]

    # edges에 따라 부모-자식 관계를 설정
    for p, c in edges:
        child[p].append(c)

    # 깊이 우선 탐색(DFS)을 수행하는 재귀 함수 정의
    def dfs(node, sheep, wolf, next_nodes):
        global max_count

        # 늑대 수가 양 수보다 많아지면 탐색 중지
        if wolf >= sheep:
            return

        # 최대 양의 수를 갱신
        max_count = max(max_count, sheep)

        # 현재 노드의 자식 노드들을 탐색 가능 노드 리스트에 추가
        next_nodes.extend(child[node])

        # 다음으로 이동할 수 있는 노드들을 순회
        for next_node in next_nodes:
            # 다음 노드가 현재 위치가 아닌 경우에만 이동
            new_next_nodes = [n for n in next_nodes if n != next_node]
            # 다음 노드에 늑대가 있는 경우
            if info[next_node]:
                dfs(next_node, sheep, wolf + 1, new_next_nodes)
            # 다음 노드에 양이 있는 경우
            else:
                dfs(next_node, sheep + 1, wolf, new_next_nodes)

    # 루트 노드(0번)에서 DFS 시작 (처음에 양 1마리가 있음)
    dfs(0, 1, 0, child[0])

    return max_count