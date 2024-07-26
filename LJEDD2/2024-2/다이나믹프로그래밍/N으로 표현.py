def solution(N, number):
    # 기본 숫자와 목표 숫자가 같으면 1회컷 가능
    if N == number:
        return 1
    
    # 8개의 빈 집합 묶은 리스트 
    s = [set() for _ in range(8)]
    
    # N을 1번부터 8번 붙인 숫자를 각 집합에 추가
    # N=5일 때, 5, 55, 555, ..., 55555555
    for i, x in enumerate(s, start=1):
        x.add(int(str(N) * i))
    
    # N을 1번부터 8번까지 사용하는 모든 경우의 수 계산
    for i in range(1, 8):
        for j in range(i):
            for base_num in s[j]:
                for add_num in s[i-j-1]:
                    # 더하기 연산
                    s[i].add(base_num + add_num)
                    
                    # 빼기 연산 
                    if base_num - add_num >= 0:
                        s[i].add(base_num - add_num)
                    
                    # 곱하기 연산
                    s[i].add(base_num * add_num)
                    
                    # 나누기 연산
                    if base_num and add_num:
                        s[i].add(base_num // add_num)
        
        if number in s[i]:
            return i + 1  # 사용 횟수 반환 (인덱스 + 1)
    
    
    # 8번 이상 시도하면 실패 
    else:
        return -1  