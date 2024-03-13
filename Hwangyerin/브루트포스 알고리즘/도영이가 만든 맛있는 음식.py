def recur(idx,sour, bitter, use):
    global answer

    if idx == N:
        if use == 0:
            return
        # 신맛 쓴맛의 차이(절댓값)
        result = abs(sour-bitter)
        # 신맛과 쓴맛의 차이가 가장 작은 요리의 차이
        answer = min(answer,result)
        print(result)
        return
    #재료를 사용하는 경우
    recur(idx+1, sour*ingredient[idx][0], bitter+ingredient[idx][1],use+1)
    #재료를 사용하지 않는 경우
    recur(idx+1 ,sour,bitter,use)

# main
N = int(input())
ingredient = [list(map(int,input().split()))for _ in range(N)]
answer = 999999999

recur(0,1,0,0)
print(answer)
