import sys
input = sys.stdin.readline

city = int(input()) #도시의 수
bus = int(input()) #버스 노선의 수

#2차원 테이블
INF = int(1e9) #무한
graph = [[INF]*(city+1) for _ in range(city+1)]

#출발 도시와 도착 도시가 동일한 경우 0으로 초기화
for x in range(1,city+1) :
    graph[x][x] = 0

# 간선 정보
for _ in range(bus) :
    # 버스는 사용할 때 비용이 든다.
    # 입력값 중복 .. / 더 싼 노선의 비용으로 입력
    start, end, cost = map(int,input().split())
    graph[start][end] = min(cost, graph[start][end])

#플로이드-워셜 알고리즘
for middle in range(1,city+1) : # 경유점
    for start in range(1,city+1) : # 시작점
        for end in range(1,city+1) : # 도착점
            # 최단경로 테이블에는 다양한 경로의 값이 누적
            # 직행보다 오히려 경유노선이 최단경로일 수 있다
            # dp가 사용된다.
            if graph[start][middle] != 1e9 and graph[middle][end] != 1e9:
                cost = graph[start][middle] + graph[middle][end]
                graph[start][end] = min(graph[start][end], cost) # 직행이냐 경유냐 비교해서 최단경로 업데이트

for x in range(1, city+1):
    for y in range(1, city+1):
        if graph[x][y] == INF:
            print(0, end=' ')
        else:
            print(graph[x][y], end=' ')
    print()