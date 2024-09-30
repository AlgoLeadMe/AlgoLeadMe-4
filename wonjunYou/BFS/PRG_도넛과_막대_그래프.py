from collections import deque

def solution(edges):
    MAX_NUMBER = 1000001

    start = [[] for _ in range(MAX_NUMBER)]
    end = [[] for _ in range(MAX_NUMBER)]
    visited = [False] * (MAX_NUMBER)

    result = [0, 0, 0, 0]

    for a, b in edges:
        start[a].append(b)
        end[b].append(a)

    middle = -1
    for node in range(MAX_NUMBER + 1):
        if (len(end[node]) == 0 and len(start[node]) >= 2):
            middle = node
            break

    result[0] = middle

    def bfs(i):
        q = deque()
        q.append(i)

        visited[i] = True

        while q:
            node = q.popleft()

            if len(start[node]) == 2 and len(end[node]) == 2:
                result[3] += 1
                return

            if not start[node]:
                result[2] += 1
                return

            for next_node in start[node]:
                if not visited[next_node]:
                    visited[next_node] = 1
                    q.append(next_node)

        result[1] += 1

    for node in start[middle]:
        end[node].remove(middle)
        bfs(node)

    return result
