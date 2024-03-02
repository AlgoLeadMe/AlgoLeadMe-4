# 자연수 N과 N개의 정수를 입력받을 A 리스트, 자연수 M과 M개의 수들을 입력받을 arr리스트를 선언한다.
N = int(input())
A = list(map(int, input().split()))
M = int(input())
arr = list(map(int, input().split()))
# A를 정렬한다.
A.sort()			

# arr의 각 원소별로 이분탐색을 한다.
for num in arr:
    # lt는 맨 앞, rt는 맨 뒤를 의미한다.
    lt, rt = 0, N - 1	
    # 찾음 여부를 확인하기 위한 변수를 선언한다.
    isExist = False	

    # 이분탐색을 시작한다.
    # lt가 rt보다 커지면 반복문을 탈출하도록 한다.
    while lt <= rt:	
        # mid는 lt와 rt의 중간값을 의미한다.
        mid = (lt + rt) // 2
        # num(목표값)이 A[mid]값과 같다면 즉, 목표값 존재여부를 알았다면 해당되는 문이다.
        if num == A[mid]:
            # isExist True를 변경한다.
            isExist = True
            # 1을 출력하고 반복문을 탈출한다.
            print(1)		
            break		
        # A[mid]가 num보다 작으면 lt를 높인다.
        elif num > A[mid]:	
            lt = mid + 1	
        # A[mid]가 num보다 크다면 rt를 낮춘다.
        else:		
            rt = mid - 1	
    # 존재하지 않은 경우 0을 출력한다.
    if not isExist:		
        print(0)		