import sys
input = sys.stdin.readline

n = int(input())  
m = int(input())  
sequence = input().rstrip()  

# 투 포인터 알고리즘을 위해서 좌우 포인터 선언
start, current = 0, 0
# 'IOI' 패턴을 찾은 횟수 선언
pattern_count = 0 

# 문자열 범위 내에서 반복
while current < m:
    # 현재 위치에서 'IOI' 패턴이 발견된 경우
    if sequence[current:current + 3] == 'IOI':
        # 패턴을 찾으면 포인터를 두 칸씩 이동
        current += 2 
        # 패턴의 길이가 'N'에 맞는 경우
        if current - start == 2 * n:
            # 패턴 카운트 증가
            pattern_count += 1
            # 패턴을 완성했으니 시작 포인터도 두 칸 이동
            start += 2
    else:
        # 패턴이 맞지 않으면 한 칸씩 이동
        current += 1
        # 시작 포인터를 현재 포인터 위치로 재설정
        start = current  

# 패턴 횟수 출력
print(pattern_count)