import sys
input= sys.stdin.readline
# 재귀를 사용하기 위해 최대 깊이를 설정해준다.
sys.setrecursionlimit(1000)

# N을 입력받는다.
n=int(input())

# N개의 정수들을 행렬로 입력받는다.
matrix=[list(map(int,input().split())) for _ in range(n)]

# 종이의 갯수를 저장하는 리스트를 초기화한다.
cnt=[]

# 분할 정복을 시작한다.
def divide(x,y,n):
    # 현재 구간의 색깔을 저장한다.
    color=matrix[x][y]
    # 현재 구간 내의 모든 정수들을 반복하면서 색깔이 같은지 확인한다.
    for i in range(x,x+n):
        for j in range(y,y+n):
            # 색깔이 다른 경우 구간을 9개로 나누어 재귀적으로 divide 함수를 호출한다.
            if color != matrix[i][j]:
                # 9구간으로 나누기 위해 a와 b를 0부터 2까지 반복한다.
                for a in range(3):
                    for b in range(3):
                        # 현재 구간을 9개의 작은 구간으로 분할하기 위해 divide 함수를 재귀 호출한다.
                        divide(x+(n//3)*a,y+(n//3)*b,n//3)
                return
    # 색깔에 따라서 갯수를 추가해준다.
    if color==1:
        cnt.append(1)
    elif color==-1:
        cnt.append(-1)
    else:
        cnt.append(0)

divide(0,0,n)
# 종이의 갯수를 출력한다.
print(cnt.count(-1),cnt.count(0),cnt.count(1),sep="\n")