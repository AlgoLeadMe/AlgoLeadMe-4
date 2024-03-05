import sys
from collections import Counter
input = sys.stdin.readline

# 수의 개수 n
n = int(input())

# n개의 정수들을 리스트에 저장
num_list = []
for i in range(n):
    num_list.append(int(input()))
num_list.sort()

# 산술평균
print(round(sum(num_list)/n))

# 중앙값
print(num_list[n//2])

# 최빈값
cnt_list = Counter(num_list).most_common()
if n == 1:
    print(num_list[0])
elif cnt_list[0][1] == cnt_list[1][1]:
    print(cnt_list[1][0])
else:
    print(cnt_list[0][0])

# 범위
print(num_list[-1]-num_list[0])
