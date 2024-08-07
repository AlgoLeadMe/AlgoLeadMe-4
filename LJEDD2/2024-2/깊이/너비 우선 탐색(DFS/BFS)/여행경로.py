from collections import defaultdict

def solution(tickets):
    ticket_dict = defaultdict(list)

    # 각 행 [a,b]는 a 공항에서 b 공항으로 가는 항공권
    
    for ticket in tickets:
        ticket_dict[ticket[0]].append(ticket[1])
        
    # 가능한 경로가 2개 이상일 경우 알파벳 순서가 앞서는 경로
    for key in ticket_dict.keys():
        ticket_dict[key].sort(reverse = True)
        
    
    # 주어진 항공권은 모두 한번씩 다 사용해야 한다.라는 조건 
    # -> 깊이 탐색? 
    # 스택 ! 
    stack = ["ICN"]
    path = []

    while stack: #  DFS(깊이 우선 탐색) 
    
        top = stack[-1] # 마지막 방문 공항
        
        # 현재 공항에서 갈 수 있는 다음 공항이 없다면 현재 공항 path에 추가
        if not ticket_dict[top] or not len(ticket_dict[top]):
            path.append(stack.pop())

        else:
            # 다음 방문할 공항을 스택에 추가
            stack.append(ticket_dict[top].pop()) 

    # 마지막에 방문한 공항이 마지막에 오도록 
    return path[::-1]