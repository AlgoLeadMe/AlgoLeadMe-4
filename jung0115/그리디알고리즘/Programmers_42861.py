# 24차시 2024.11.09.토 : 프로그래머스 - 섬 연결하기(Lv.3)
def solution(n, costs):
  answer = 0
  
  graph = [[] for _ in range(n)]
  for cost in costs:
    u, v, w = cost
    graph[u].append((w, v))
    graph[v].append((w, u))

  connect = set() # 연결된 섬
  connect.add(0)
  
  edges = graph[0] # 다리
  edges.sort()     # 비용을 기준으로 오름차순 정렬
  
  while len(connect) < n:
    w, v = edges.pop(0)
    
    # 이미 연결된 섬
    if v in connect:
      continue
    
    # 다리 건설
    answer += w
    connect.add(v)
    
    for edge in graph[v]:
      if edge[1] not in connect:
        edges.append(edge)
    
    edges.sort()
  
  return answer