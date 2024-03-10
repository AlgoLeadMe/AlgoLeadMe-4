import sys
input = sys.stdin.readline

S = input().rstrip()
q = int(input())

# 각 인덱스별로 해당 문자가 몇 번 등장했는지를 누적합으로 저장하는 리스트를 생성합니다.
prefix = [0] * len(S)

# 누적합을 계산하는 함수를 정의합니다.
def prefixSum():
    if S[0] == alpha:
        prefix[0] = 1
    else :
        prefix[0] = 0
    for i in range(1, len(S)):
        prefix[i] = prefix[i - 1] + (S[i] == alpha)

# 주어진 질문에 대해 처리합니다.
for _ in range(q):
    alpha, lt, rt = input().split()
    lt, rt = int(lt), int(rt)
    prefixSum()
    
    # 구간 [lt, rt] 내에 해당 알파벳이 몇 번 등장했는지를 계산합니다.
    # lt - 1과 rt 인덱스의 값을 이용하여 첫 번째와 마지막 문자를 포함합니다.
    print(prefix[rt] - prefix[lt] + (S[lt]==alpha))
