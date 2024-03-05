import sys
# 점 N개와 선분 M개를 입력받는다.
n, m = map(int, sys.stdin.readline().split())
# 점의 좌표를 입력받는다.
dot = list(map(int, sys.stdin.readline().split()))
#이진 탐색을 수행하기 위해서 점들을 정렬한다.
dot.sort()

# 선분 중 가장 작은 점을 구한다.
def dot_min(a):
    start = 0
    end = n - 1
    while start <= end:
        mid = (start + end) // 2

        if dot[mid] < a:
            start = mid + 1
        else:
            end = mid - 1
    return end + 1

# 선분 중 가장 큰 점을 구한다.
def dot_max(b):   
    start = 0
    end = n - 1
    while start <= end:
        mid = (start + end) // 2

        if b < dot[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return end

# 선분의 갯수만큼 반복하면서 선분의 범위 중 큰 점의 인덱스와 작은 점의 인덱스를 뺀 값에 +1을 해주면 주어진 점의 갯수를 출력할 수 있다.
for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    print(dot_max(b) - dot_min(a) + 1)