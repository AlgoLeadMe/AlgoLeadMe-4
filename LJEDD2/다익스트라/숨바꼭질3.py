# 다익스트라 
import heapq
import sys
input = sys.stdin.readline

INF = float('inf')
n, k = map(int,input().split())

# 시작 위치 초기화
board = [INF] * 100001
def OOB(x):
    return not(0 <= x <= 100000)

# 다익스트라
def dijkstra(start):
    q = []

    # 시작 노드로 가기 전 최단 경로를 0으로 설정, 큐 삽입
    heapq.heappush(q,(0,start))
    board[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        # 이미 갱신된 적이 있는 노드일 경우 무시
        if board[now] < dist:
            continue

        for jump, time in [(now*2, dist),(now+1, dist+1),(now-1, dist+1)]:
            if not OOB(jump) and board[jump] > time:
                board[jump] = time
                heapq.heappush(q,(time,jump))

dijkstra(n)
print(board[k])

# BFS 
from collections import deque

def bfs(x):
    board = [-1] * 100001
    queue = deque([x])
    board[x] = 0

    while queue:
        c_x = queue.popleft()
        if c_x == k:
            return board[c_x]

        # 0초 이동 먼저
        # x + 1을 x - 1보다 먼저 넣으면 순간이동한 경우보다 빠르게 도착할 수 있기 때문에 오답 
        for n_x in [c_x*2, c_x-1, c_x+1]:
            if 0 <= n_x <= 100000 and board[n_x] == -1:
                board[n_x] = board[c_x] + (0 if n_x == c_x*2 else 1)
                queue.append(n_x)

print(bfs(n))