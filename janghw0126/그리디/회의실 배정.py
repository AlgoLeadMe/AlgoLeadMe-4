import sys
input = sys.stdin.readline

# 회의의 수 입력받기
N = int(input())

# 회의 시작시간과 끝나는 시간 입력받는 리스트 생성
meeting = []

# 회의의 시작시간과 끝나는 시간 입력받기
for _ in range(N):
    a, b = map(int, input().split())
    meeting.append([a, b])

# 회의가 끝나는 시간을 기준으로, 끝나는 시간이 같다면 시작 시간을 기준으로 정렬하기
meeting.sort(key=lambda x: (x[1], x[0]))

# 가능한 최대 회의 수를 세기 위한 변수
count = 0
# 마지막으로 선택된 회의의 끝나는 시간
end_time = 0

# 각 회의를 순회하면서 가능한 최대 회의 수 계산
for i in range(N):
    if meeting[i][0] >= end_time:
        # 현재 회의가 마지막으로 선택된 회의의 끝나는 시간 이후에 시작하면 선택
        end_time = meeting[i][1]
        count += 1

print(count)