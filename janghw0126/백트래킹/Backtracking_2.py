import sys

def dfs(c):
  if len(s) == m:
    for j in s:
      print(j, end=" ")
    print()
    return
  for i in range(c, n + 1):
    if i not in s:
      s.append(i)
      dfs(i)
      s.pop()

input = sys.stdin.readline
n, m = map(int, input().split())
s = []
a = []
dfs(1)