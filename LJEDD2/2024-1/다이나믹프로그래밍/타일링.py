while True:
    try:
        n = int(input())
        dp = [0] * 251

        # n의 범위가 0부터라서 아무것도 없는 경우 1가지 추가
        # 덮개가 최대 2*2 크기 직사각형 형태라서 2까지 미리 입력 
        dp[0:3] = [1,1,3]

        for i in range(3,n+1):
            # 2*1을 채울 것인지(i-1), 2*2 또는 2*1 두 개로 채워넣을 것인지(i-2)
            dp[i] = dp[i-1] + dp[i-2] + dp[i-2]
        print(dp[n])
    except:
        break