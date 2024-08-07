import sys
input = sys.stdin.readline

# 학생의 수 N 입력
N = int(input())

# 학생들이 각각 가지고 있는 숫자를 리스트로 선언
num = [int(input()) for _ in range(N)]

# 각 숫자의 등장 횟수를 세기 위한 딕셔너리
count = [0 for _ in range(max(num)+1)]
for c in num:
    count[c]+=1

# 학생들이 쓴 숫자들에 대해 약수로 갱신
for i in range(N):
    x = num[i]
    result = 0
    for j in range(1, int(x ** 0.5) + 1):       
        if x % j == 0:
            if j*j!=x: 
                result += count[j] + count[x//j]
            else:
                result += count[j]   
    print(result-1)