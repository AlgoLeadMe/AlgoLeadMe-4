N, M = map(int, input().split())
numbers = [int(x) for x in input().split()]

numbers.sort()

def backtracking(depth):
    if depth == M:
        print(' '.join(map(str,box)))
        return

    for i in range(N):
        if numbers[i] in box:
            continue
        box.append(numbers[i])
        backtracking(depth + 1)
        box.pop()

box = []
backtracking(0)