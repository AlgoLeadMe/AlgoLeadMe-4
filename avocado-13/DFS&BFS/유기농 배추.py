import sys
sys.setrecursionlimit(10**6)

t = int(input())

def dfs (x,y):
    
    if x<= -1 or x >= m or y <= -1 or y >=n :
        return False
    if cabbage[x][y] == 1 :
        cabbage[x][y] = 0
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x,y-1)
        dfs(x,y+1)
        return True
    return False

for i in range(t):
    m,n,k = map(int,input().split())
    cabbage = [[0 for _ in range(n)] for _ in range(m)]
    for _ in range(k):
        a,b = map(int,input().split())
        cabbage[a][b] = 1
    result = 0
    for i in range(m):
        for j in range(n):
            if dfs(i,j) == True:
                result += 1
    print(result)
