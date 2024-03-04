import sys
input = sys.stdin.readline
N = int(input())
dairy_product = sorted([int(input()) for _ in range(N)],reverse=True)

ans = sum(dairy_product)

for i in range(2,N,3):
    ans-= dairy_product[i]

print(ans)
