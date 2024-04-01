import sys
input = sys.stdin.readline

# K: 수강가능인원, L: 대기목록의 길이
K, L = map(int,input().split())

#대기목록 key:학생의 학번, value: 순서
waiting = {}

# 학생의 학번을 키로 순서는 인덱스로
# 즉 두 번 이상 클릭한 학생은 자연스럽게 인덱스가 뒤로 넘어감
for i in range(L):
    student = input().rstrip()
    waiting[student] = i

# 순서(value)대로 정렬
final_list = sorted(waiting.items(), key = lambda item: item[1])

# 제한인원보다 신청인원이 적을 경우 제한인원을 신청인원으로 초기화
if K > len(final_list):
    K = len(final_list)

# 수강신청에 성공한 학생의 학번을 출력
for i in range(K):
    print(final_list[i][0])