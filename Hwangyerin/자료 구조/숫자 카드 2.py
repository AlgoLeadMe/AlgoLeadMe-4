import sys
input = sys.stdin.readline
n = int(input())
numCards = [int(x) for x in input().split()]
m = int(input())
countCards = [int(x) for x in input().split()]

cardDic = {}

for i in range(n):
    if numCards[i] in cardDic:
        cardDic[numCards[i]] += 1
    else:
        cardDic[numCards[i]] = 1

for i in range(m):
    if countCards[i] not in cardDic:
        print(0, end=' ')
    else:
        print(cardDic[countCards[i]], end=' ')
