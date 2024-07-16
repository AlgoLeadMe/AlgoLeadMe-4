# 소요시간 2시간 (규칙찾기 20분 + 식 세우기 30분 + 문제풀기 50분 + 해결x 답보고 이해 10분)
n = int(input())
dp = [0]*31
dp[2] = 3

for i in range(4,31,2):
    dp[i] = (dp[i-2] * 3)
    # 4일때는 3x2 0개 / 6일때는 3x2가 3가지 경우 * 2개 ... 
    for j in range(i-4,0,-2):
        dp[i] += dp[j] * 2
    dp[i] += 2
print(dp[n])


# 잘못 접근 
# n = int(input())
# dp = [0]*10001
# dp[2] = 3
#
# for i in range(4,31,2):
#     dp[i] = (dp[i-2] * 3)
# 단순히 양쪽에 2개씩인 줄 알았으나 왼쪽에 3x2 타일을 두게 되면 중복처리가 되어버림 
#     for j in range(i-2,0,-2):
#         dp[i] += dp[j] * 2
#     dp[i] += 2
# print(dp[n])
