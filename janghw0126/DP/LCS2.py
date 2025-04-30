import sys
input = sys.stdin.readline

# 문자열 입력 받기
string1 = list(input().rstrip())  
string2 = list(input().rstrip())  

# LCS 길이 및 LCS 문자열 저장을 위한 DP 테이블 초기화
dp_table = [[""] * (len(string2) + 1) for _ in range(len(string1) + 1)]

# DP로 LCS 계산
for i in range(1, len(string1) + 1):
    for j in range(1, len(string2) + 1):
        # 현재 문자가 같으면 이전 LCS에 해당 문자를 추가
        if string1[i - 1] == string2[j - 1]:
            dp_table[i][j] = dp_table[i - 1][j - 1] + string1[i - 1]
        else:
            # 현재 문자가 다를 경우 더 긴 LCS를 선택
            if len(dp_table[i - 1][j]) >= len(dp_table[i][j - 1]):
                dp_table[i][j] = dp_table[i - 1][j]
            else:
                dp_table[i][j] = dp_table[i][j - 1]

# 최종 LCS 문자열
lcs_result = dp_table[-1][-1]
# 공통 부분 수열이 없는 경우
if len(lcs_result) == 0:
    # 결과 출력
    print(0)
else:
    # 결과 출력
    print(len(lcs_result))
    print(lcs_result)  