#자연수 N과 M을 입력받는다.
N, M = map(int, input().split())
#숫자들을 입력받아 리스트에 저장한다.
numbers = [int(x) for x in input().split()]
#숫자들을 오름차순으로 정렬한다.
numbers.sort()

def backtracking(depth):
    #현재까지 선택한 숫자의 개수가 M과 같다면 수행할 문이다.
    if depth == M:
        #박스에 저장된 숫자들을 문자열로 변환하여 공백을 기준으로 결합하여 출력한다.
        print(' '.join(map(str,box)))
        return
    #0부터 N-1까지의 인덱스에 대해 반복한다.
    for i in range(N):
        #이미 선택된 숫자라면 건너뛴다.
        if numbers[i] in box:
            continue
        #숫자를 박스에 추가한다.
        box.append(numbers[i])
        #다음 자릿수의 숫자를 선택하기 위해 재귀적으로 backtracking 함수를 호출한다.
        backtracking(depth + 1)
        #함수 호출 후에는 해당 자릿수에서의 선택이 끝났으므로, 박스에서 마지막에 추가된 숫자를 제거한다.
        box.pop()
#선택한 숫자들을 저장할 리스트를 선언한다.
box = []
#백트래킹 함수를 호출하여 문제를 해결한다.
backtracking(0)
