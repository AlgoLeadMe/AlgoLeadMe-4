import sys
input=sys.stdin.readline
K, N = map(int, input().split())
lan = [int(input()) for _ in range(K)]
start, end = 1, max(lan) #이분탐색 처음과 끝위치

# 주어진 랜선 길이(mid)에 대해 목표한 랜선 개수(N)를 만족하는지 확인하는 함수
def check(lan, N, mid): 
    lines = 0
    for i in lan:
        lines += i // mid
    return lines >= N

while start <= end:
    mid = (start + end) // 2
    
    if check(lan, N, mid):
        start = mid + 1
    else:
        end = mid - 1
        
print(end)
