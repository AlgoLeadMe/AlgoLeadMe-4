# 더 간단한 풀이 ... (문자열)
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    cnt = 0
    s = input().rstrip()
    while "[]" in s:
        s = s.replace("[]", "")
        cnt += 1

    print(2**cnt)



# import sys

# input = sys.stdin.readline

# for _ in range(int(input())):
#     s = input().rstrip()  # 괄호 문자열

#     max_depth = 0  # 최대 깊이를 저장할 변수
#     tree = list()  # 현재 열린 괄호를 저장할 스택임

#     for i in s:
#         # 여는 괄호일 경우 스택에 열린 괄호 추가
#         if i == '[':
#             tree.append('[')
#             continue
#         # 닫는 괄호일 경우
#         max_depth = max(len(tree), max_depth)
#         # 현재 깊이와 최대 깊이 중 큰 값을 저장하고
#         tree.pop()  # 마지막 열린 괄호를 제거

#     print(2 ** max_depth)  # 쌍을 이룰때 가지 생성, 가지2-.1개씩 나눠가짐
#     # 결국엔 2의 depth승 