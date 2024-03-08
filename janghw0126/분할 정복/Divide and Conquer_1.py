import sys
input = sys.stdin.readline

def cut_paper(r,c,n):
    num = paper[r][c]
    for i in range(r,r+n):
        for j in range(c,c+n):
            if paper[i][j] != num:
                for k in range(3):
                    for l in range(3):
                        cut_paper(r+k*(n//3),c+l*(n//3),n//3)
                return

    if num == -1:
        ans[0] += 1
    elif num == 0:
        ans[1] += 1
    else:
        ans[2] += 1

n = int(input())
paper = [list(map(int,input().split())) for _ in range(n)]
ans = [0,0,0]

cut_paper(0,0,n)
print(*ans,sep='\n')