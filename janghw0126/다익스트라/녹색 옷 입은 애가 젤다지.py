# 양방향 큐 모듈을 불러온다.
from collections import deque  
# 문제 번호를 세기 위한 count와, 상하좌우 이동을 위한 dx, dy 배열을 정의한다.
count, dx, dy = 0, [0, 0, 1, -1], [1, -1, 0, 0] 

# 너비 우선 탐색(BFS) 함수를 정의한다.
def bfs(): 
    queue = deque() 
    # 시작점을 queue에 추가한다.
    queue.append([0, 0])  
    # 시작점의 비용을 초기화한다.
    cost[0][0] = field[0][0]  
    # queue에 요소가 있는 동안 반복한다.
    while queue:  
        # queue에서 요소를 하나 꺼내 x, y에 할당한다.
        x, y = queue.popleft() 
        # 상하좌우 네 방향에 대해 반복한다.
        for i in range(4):  
            # 현재 위치에서 이동할 새로운 위치를 계산한다.
            nx, ny = x + dx[i], y + dy[i] 
             # 새로운 위치가 범위 내에 있는지 확인한다.
            if -1 < nx < n and -1 < ny < n: 
                # 새로운 위치로 이동하는 비용이 더 저렴한지 확인하고 더 저렴한 경우 비용을 갱신한 후 갱신된 위치를 queue에 추가한다.
                if cost[y][x] + field[ny][nx] < cost[ny][nx]: 
                    cost[ny][nx] = cost[y][x] + field[ny][nx] 
                    queue.append([nx, ny]) 
    # 목적지까지의 최소 비용을 반환한다.
    return cost[n-1][n-1]  


while True:
    n = int(input())  
    if n == 0: 
        break  
    # 문제 번호를 1 증가시킨다.
    count += 1
    # 지도 정보를 저장할 리스트를 초기화한다.
    field = []  
    # 지도 정보를 입력받아 field에 저장한다.
    for i in range(n): field.append(list(map(int, input().split()))) 
    # 각 위치까지의 최소 비용을 저장할 리스트를 무한대로 초기화한다.
    cost = [[1e9 for j in range(n)] for i in range(n)]  
    # 각 테스트 케이스의 결과를 출력한다.
    print(f"Problem {count}: {bfs()}")  
