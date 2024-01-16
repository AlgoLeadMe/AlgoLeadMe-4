towerCount = int(input())
towerList = list(map(int, input().split()))
stack = [0]
result = []

for i in range(towerCount):
    while stack and towerList[i] >= towerList[stack[-1]]:
        stack.pop()

    if not stack:
        result.append(0)
    else:
        result.append(stack[-1] + 1)

    stack.append(i)
print(' '.join(map(str, result)))
