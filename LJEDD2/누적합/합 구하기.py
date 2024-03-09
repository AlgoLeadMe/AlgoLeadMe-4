"""
주어진 배열의 누적합 구하기.
배열의 부분합을 구할 범위를 입력 받고 각 범위의 부분합 계산 
"""

N = int(input())
A = [0]+list(map(int, input().split()))
M = int(input())


cases = [list(map(int, input().split())) for _ in range(M)]

psum = [0] * (N+1)
# 부분합 계산해두기 : 배열의 i번째 요소부터 j번째 요소까지의 합
for i in range(1,N+1):
    psum[i] = psum[i-1] + A[i]

# 누적합 구함 
for x,y in cases:
    print(psum[y] - psum[x-1])