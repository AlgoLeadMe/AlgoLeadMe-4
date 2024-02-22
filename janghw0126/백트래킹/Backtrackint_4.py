import sys
input = sys.stdin.readline

#재귀 함수를 호출한다.
def dfs():
    #만약 리스트의 크기가 m이라면 모두 고른 것이 되므로 ans 리스트의 요소들을 출력한다.
    if len(ans) == m:
        print(*ans)
        return
    #자릿수가 아직 다 안찼으므로 반복문을 수행한다.
    for i in range(1, n+1):
        #ans 리스트에 해당 숫자를 추가한다.
        ans.append(i)
        #다음 자릿수의 숫자를 넣기 위해 재귀적으로 dfs함수를 호출한다.
        dfs()
        #함수 호출 후에는 해당 자릿수에서의 선택이 끝났으므로, ans 리스트에서 마지막에 추가된 숫자를 제거한다.-> 다음 자릿수의 반복문을 실행해야 되므로
        ans.pop()

n, m = map(int, input().split())
ans = []
#dfs함수를 이용해서 모든 경우의 수를 찾는다.
dfs()