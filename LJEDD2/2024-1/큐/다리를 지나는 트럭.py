from collections import deque

def solution(bridge_length, weight, truck_weights):

    time = 0 
    total_w = 0

    # 다리 길이만큼 초깃값 설정
    bridge_deque = deque(bridge_length * [0]) 
    
    # 대기하고 있는 트럭
    waiting = deque(truck_weights) 
    
    # Queue 
    while True :
        
        # 대기 트럭과 이동 트럭이 없을 경우 time 출력 
        if not waiting and not total_w: 
            return time 
        
        total_w -= bridge_deque.popleft() # 다리 위 트럭이 건넘 

        # 새 트럭이 다리에 올라갈 수 있으면 (대기중인 트럭이 있고, 다리 무게가 넉넉하다면)
        if waiting and total_w + waiting[0] <= weight:

            # 대기 중인 트럭이 다리에 올라감  
            total_w += waiting[0] # 현재 무게 추가 
            bridge_deque.append(waiting.popleft()) 

        else: 
            # 트럭이 다리에 추가로 올라갈 수 없을 경우 무게 0
            bridge_deque.append(0)
            
        time += 1 