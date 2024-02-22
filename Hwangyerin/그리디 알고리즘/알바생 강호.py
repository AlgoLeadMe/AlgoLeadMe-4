def hap_tips(tip_list):
    tip_list.sort(reverse=True)  #내림차순으로 정렬
    total_tip = 0
    for i, tip in enumerate(tip_list):
        total_tip += max(tip - i, 0)  #팁에서 순서값을 뺀 값 중에 양수인 것만 누적 합
    return total_tip

n = int(input()) #스타박스 앞에 서 있는 사람의 수 N
tip_list = [int(input()) for _ in range(n)] #총 N개의 줄에 각 사람이 주려고 하는 팁 리스트

print(hap_tips(tip_list))