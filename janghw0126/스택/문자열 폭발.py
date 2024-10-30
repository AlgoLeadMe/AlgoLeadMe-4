import sys
input=sys.stdin.readline

# 문자열 입력하기
string = input().strip()
# 폭발 문자열 입력하기
bomb_string = input().strip()

# 폭발 문자열 길이 계산하기
bomb_len=len(bomb_string)

# 결과 출력 리스트 선언
stack=[]

# stack에 쌓아두고, 폭발문자열이 있는 경우 pop
for str in string:
    stack.append(str)
    # 폭발 문자열과 stack 뒷부분이 같은 경우
    if ''.join(stack[-bomb_len:])==bomb_string:
        # 해당 문자열 pop
        for _ in range(bomb_len):
            stack.pop()

# 결과 출력
print(''.join(stack) if stack else "FRULA",end='')