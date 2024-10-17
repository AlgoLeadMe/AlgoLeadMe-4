import sys
input = sys.stdin.readline

# 하나의 소수를 여러 번 더할 수 있다. -> 브루트포스 가능 
# 5보다 큰 임의의 홀수로 세 소수의 합이 되는지 
def search(n):
    for i in arr:
        for j in arr:
            for k in arr:
                if i+j+k == n:
                    return i, j, k

    else: # 안되면 0 
        return 0

# 에라토스테네스의 체 - 소수 판별 
prime = [True] * 1001

for i in range(2,101):
    if prime[i]:
        for j in range(i*2, 1001, i):
            prime[j] = False

# 소수 찾기 
arr = [i for i in range(2, 1001) if prime[i] == True]

t = int(input())
for _ in range(t):
    n = int(input())
    print(*search(n))