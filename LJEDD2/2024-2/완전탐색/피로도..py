# 첫 번째 코드 
def solution(k, dungeons):
    
    def DFS(k, cnt):
        nonlocal answer
    
        answer = max(answer, cnt)
        for i in range(len(dungeons)):
            # 던전 = ["최소 필요 피로도", "소모 피로도"] 
            min_fatigue, use_fatigue = dungeons[i][0], dungeons[i][1]

            # 현재 피로도가 해당 던전을 방문하기 위한 최소 피로도보다 클 때
            if not visited[i] and k >= min_fatigue:    
                visited[i] = True

                # 백트래킹 : 이전 노드로 다시 back할 때, 
                # 해당 노드를 방문하기 전의 피로도로 다시 복구
                DFS(k-use_fatigue, cnt+1)
                visited[i] = False

    answer = 0
    visited = [False] * len(dungeons) # visited 
    DFS(k, 0)     
    
    return answer


# 개선된 코드 
def solution(k, dungeons):
    def dfs(k, cnt):
        #  함수 내부에서 값을 갱신할 수 있는 비전역 변수로 선언 
        nonlocal answer
        
        answer = max(answer, cnt)
        
        # enumerate()를 활용하여 각 던전의 인덱스와 값을 동시에 반복
        for i, (min_fatigue, use_fatigue) in enumerate(dungeons):
            
            if not visited[i] and k >= min_fatigue:
                
                visited[i] = True
                dfs(k - use_fatigue, cnt + 1)
                visited[i] = False
    
    answer = 0
    visited = [False] * len(dungeons)
    dfs(k, 0)
    
    return answer