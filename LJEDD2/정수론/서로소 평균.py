N = int(input())
A = list(map(int, input().split()))
X = int(input())

# 유클리드호제법
def gcd(a, b):
    # a를 b로 나눈 몫이 0이 될 때까지
    while b:
        a, b = b, a % b
    return a

total, cnt = 0, 0

for num in A:
    if gcd(X, num) == 1:
        total += num
        cnt += 1

print(total / cnt)

# 파이썬 내장함수 사용
# from math import gcd
#
# N = int(input())
# A = list(map(int, input().split()))
# X = int(input())
#
# total, cnt = 0, 0
#
# for num in A:
#     if gcd(X, num) == 1:
#         total += num
#         cnt += 1
#
# print(total / cnt)
