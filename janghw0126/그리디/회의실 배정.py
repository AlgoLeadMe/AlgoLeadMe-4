import sys
input=sys.stdin.readline

# 회의의 수 입력받기
N=int(input())

# 회의 시작시간과 끝나는 시간 입력받는 리스트 생성
meeting=[]

# 회의의 시작시간과 끝나는 시간 입력받기
for i in range(N):
    a,b=map(int,input().split())
    meeting.append([a,b])

# 회의가 끝나는 시간을 기준으로 정렬하기
meeting.sort(key=lambda x:x[1])

# 최댓값을 찾기 위한 변수 선언
max=0

# 각 리스트를 순회하면서 각각 회의할 수 있는 갯수를 계산하고 최댓값 찾기
for i in range(N):
    # 회의할 수 있는 갯수를 세기 위한 변수
    count=0
    for j in range(N):
        if meeting[i][1]<meeting[j][0]:
            count+=1
            i=j
    if max<count:
        max=count
        print("max:",max)
            
print(max+1)