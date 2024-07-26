# 갓교황의 꿀팁 
# https://github.com/AlgoLeadMe/AlgoLeadMe-4/pull/41#discussion_r1468363953

def check(mid, times, n):
    # 주어진 시간(mid)에 n명 이상을 심사할 수 있는지 확인 
    checked = 0
    for time in times:
        checked += mid // time
        if checked >= n:
            return True   
    return False

def solution(n, times):
    answer = 0
    left, right = 1, max(times) * n 
    # 가장 긴 심사시간이 소요 : 
    # 심사관에게 n 명 모두 심사받는 경우
    
    while left <= right:
        mid = (left + right) // 2
        if check(mid, times, n):
            answer = mid
            right = mid - 1
        else:
            left = mid + 1
    
    return answer