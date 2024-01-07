N = int(input())  # 시험 본 과목의 개수 N 입력
scores = list(map(int, input().split()))  # 세준이의 현재 성적 입력

max_score = max(scores)  # 최고 점수 찾기

# 모든 성적을 새로운 기준으로 변환
new_scores = [(score / max_score) * 100 for score in scores]

# 새로운 기준으로 변환된 성적들의 평균 계산
average = sum(new_scores) / N

# 결과 출력
print(average)
