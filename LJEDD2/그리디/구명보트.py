# 1차 시도 
from collections import deque

def solution(people, limit):
    answer = 0
    # 1) 오름차순 정렬 
    people = deque(sorted(people))
    
    while people: # 사람 하나씩 구출할 것 
        
        # 2) 제일 무거운 사람부터 차례로 구출 
        if people[-1] + people[0] > limit:
            people.pop() 
            answer += 1       

        # 3) 추가로 구출 가능한 사람이 더 있는지 가벼운 사람부터 검사
        # 가벼운 사람이 얼마나 더 들어갈 수 있느냐를 봐야하기 때문에 왼쪽부터 비교 
        else: 
            # 무거운 사람 + 가벼운 사람 한명 더 데려갈 수 있을 경우 
            if len(people) > 1:
                people.popleft() 
                people.pop()
                answer += 1
            else:
                # 남아 있는 1명 추가하고 break
                return answer + 1 
    # 더 구출할 사람이 없다면 
    return answer

# 2차 시도 (코드 최적화) 
def solution(people, limit):
    answer = 0
    
    # 1) 오름차순 정렬 
    people = deque(sorted(people))
    
    while people: # 사람 하나씩 구출할 것 
        saved = people.pop() 
        
        # 2) 제일 가벼운 사람 쪽에서 다른 사람과 같이 구출될 수 있는지 판단 
        # 가벼운 사람이 얼마나 더 들어갈 수 있느냐를 봐야하기 때문에 왼쪽과 비교 
        if people and saved + people[0] <= limit: 
            people.popleft()
            
        # 3) 비교할게 없으면 1팀 추가    
        answer += 1 
            
    return answer



