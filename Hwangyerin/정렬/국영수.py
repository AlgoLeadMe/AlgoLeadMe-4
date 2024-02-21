import sys
input = sys.stdin.readline

n = int(input())

scoreList = [list(input().split()) for _ in range(n)]

    
scoreList.sort(key = lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for name in scoreList:
    print(name[0])
