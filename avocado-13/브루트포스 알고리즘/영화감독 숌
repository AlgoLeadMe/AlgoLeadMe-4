import sys

input = sys.stdin.readline

n, m = map(int, input().split())
ice = [[False for _ in range(n)] for _ in range(n)]
for i in range(m):
    i1, i2 = map(int, input().split())
    ice[i1 - 1][i2 - 1] = True
    ice[i2 - 1][i1 - 1] = True

result = 0

for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            if not ice[i][j] and not ice[i][k] and not ice[j][k]:
                result += 1

print(result)