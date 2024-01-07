def solution(n, lost, reserve):
    # 집합을 사용하여 여유분을 들고 왔지만 체육복을 잃어버린 사람 제거
    set_res = set(reserve) - set(lost)
    set_los = set(lost) - set(reserve)

    # 체육복 여분을 가져온 사람은
    for i in set_res:
        # 좌, 우로 체육복이 없는 사람에게 하나씩 기부
        if i - 1 in set_los:
            # 받은 사람은 lost 명단에서 제외
            set_los.remove(i - 1)
        elif i + 1 in set_los:
            set_los.remove(i + 1)

    # 체육복을 입을 수 있는 사람 수
    return n - len(set_los)