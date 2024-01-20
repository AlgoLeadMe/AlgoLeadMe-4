import sys

# 명령의 수 N을 선언한다.
N = int(input())

# 정수를 저장하는 스택을 구현한다.
stack = []

for _ in range(N):
    # 해야 할 명령을 정수 형태로 입력으로 받는다.
    x = list(map(int, sys.stdin.readline().split()))

    # 1 X: 정수 X를 스택에 넣는다. (1 ≤ X ≤ 100,000)
    if x[0] == 1:
        stack.append(x[1])
    # 2: 스택에 정수가 있다면 맨 위의 정수를 빼고 출력한다. 없다면 -1을 대신 출력한다.
    elif x[0] == 2:
        print(stack.pop() if stack else -1)
    # 3: 스택에 들어있는 정수의 개수 리스트의 길이를 이용해 출력한다.
    elif x[0] == 3:
        print(len(stack))
    # 4: 스택이 비어있으면 1, 아니면 0을 출력한다.
    elif x[0] == 4:
        print(1 if not stack else 0)
    # 5: 스택에 정수가 있다면 맨 위의 정수를 출력한다. 없다면 -1을 대신 출력한다.
    elif x[0] == 5:
        print(stack[-1] if stack else -1)