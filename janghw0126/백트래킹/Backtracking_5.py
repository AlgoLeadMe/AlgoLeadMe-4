# 재귀 함수를 이용하여 로또 번호 조합을 생성하는 함수를 정의한다.
def lotto(arr, s, index, cnt):
    # 로또 번호가 6개 선택되었을 때, 해당 조합을 출력한다.
    if cnt==6:
        print(*arr)  # arr 리스트의 요소를 공백으로 구분하여 출력한다.
        return  # 재귀 호출을 종료한다.
    
    # 입력 받은 s 리스트의 index부터 탐색을 시작한다.
    for i in range(index, len(s)):
        arr[cnt]=s[i]  # 현재 인덱스의 값을 arr에 할당한다.
        lotto(arr, s, i+1, cnt+1)  # 다음 요소를 선택하기 위해 재귀 호출을 하고 cnt를 1 증가시켜 선택된 숫자의 개수를 표시한다.
    

# 무한 반복문을 통해 여러 케이스를 입력받아 처리한다.
while True:
    s = list(map(int, input().split()))  # 공백으로 구분된 정수를 입력받아 리스트로 변환한다.
    if s[0]==0:  # 입력의 첫 번째 요소가 0이면 반복문을 종료한다.
        break
    arr=[0]*6  # 로또 번호를 저장할 리스트, 초기에는 모든 값을 0으로 설정한다.
    lotto(arr, s[1:], 0, 0)  # 재귀 함수를 호출하면서 s[1:]로 첫 번째 요소(숫자의 개수)를 제외한 리스트를 전달한다.
    print()  # 한 케이스가 끝날 때마다 빈 줄을 출력하여 구분한다.