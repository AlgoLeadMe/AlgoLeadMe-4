import sys
from collections import deque

input = sys.stdin.readline
t = int(input())  

for _ in range(t):
    commands = input().strip()  # 명령어 문자열
    num_elements = int(input())  # 배열의 원소 개수
    elements = input().strip()[1:-1]  # 대괄호를 제거하고 배열 요소를 가져오기

    # 덱 초기화: 빈 문자열이 아니면 쉼표로 구분하여 덱으로 변환
    if elements:
        dq = deque(elements.split(','))
    else:
        dq = deque()

    is_reversed = False  # 배열의 순서를 뒤집었는지 여부를 나타냄
    error_occurred = False  # 오류가 발생했는지를 나타냄

    # 명령어를 순차적으로 처리
    for command in commands:
        if command == 'R':
            # R 명령어가 나오면 뒤집기 플래그를 반전
            is_reversed = not is_reversed
        elif command == 'D':
            # D 명령어 처리
            if not dq:
                # 덱이 비어있으면 에러 출력
                print("error")
                error_occurred = True
                break
            if is_reversed:
                # 뒤집힌 상태에서는 덱의 끝에서 제거
                dq.pop()
            else:
                # 정상 상태에서는 덱의 앞에서 제거
                dq.popleft()

    if error_occurred:
        continue  # 에러가 발생하면 다음 테스트 케이스로 넘어감

    if is_reversed:
        # 최종 상태가 뒤집힌 경우 덱을 뒤집음
        dq.reverse()
 
    # 덱을 문자열로 변환하여 출력
    print("[" + ",".join(dq) + "]")