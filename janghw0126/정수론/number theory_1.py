MAX = 1000000
# 각 숫자의 약수의 합을 저장하는 리스트를 선언한다.
dp = [1] * (MAX + 1)
# dp 리스트의 누적 합을 저장하는 리스트를 선언한다.
s = [0] * (MAX + 1)
# 2부터 MAX까지의 수에 대해 반복문을 실행한다.
for i in range(2, MAX + 1):
    j = 1
    # 각 숫자 i에 대해 i의 배수들을 찾아가며 dp 리스트의 값을 업데이트한다.
    while i * j <= MAX:
        # 예를 들어 i가 2일 경우 dp[2], dp[4], dp[6], ... 등을 i만큼 증가시킵니다.
        dp[i * j] += i
        j+=1
# 1부터 MAX까지의 숫자에 대해 s 리스트를 누적합으로 계산한다.
for i in range(1, MAX + 1):
    s[i] = s[i-1] + dp[i]
iter = int(input())
ans = []
for k in range(iter):
    #입력으로 들어오는 iter 횟수만큼 반복문을 실행하면서 n 값을 입력받는다.
    n = int(input())
    # s[n] 값을 ans 리스트에 추가한다.
    ans.append(s[n])
# ans 리스트의 값을 줄바꿈으로 구분하여 출력한다.
print('\n'.join(map(str,ans)) + '\n')