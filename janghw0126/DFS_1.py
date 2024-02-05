#행의 수인 R과 열의 수인 C를 입력받는다.
R, C = map(int, input().split())
#R개의 줄에 걸쳐 C개의 문자를 입력받아 2차원 리스트 arr에 저장한다.
arr = [list(input()) for _ in range(R)]
#x의 이동 방향을 나타내는 리스트를 작성한다.
directx = [-1, 0, 1]
#y의 이동 방향을 나타내는 리스트를 작성한다.
directy = [1, 1, 1]
#파이프라인이 연결된 경우를 카운트하기 위한 변수를 선언한다.
cnt = 0
#깊이 우선 탐색(DFS)을 수행하는 함수를 작성한다. 현재 위치를 (x, y)로 받는다.
def dfs(x, y):
    #cnt 변수를 전역 변수로 사용하기 위해 선언한다.
    global cnt
    #현재 위치가 마지막 열에 도달한 경우인 파이프라인이 연결된 경우이다.
    #cnt를 1 증가시키고 True를 반환한다.
    if y == C - 1:
        cnt += 1
        return True
    #x의 이동거리와 y의 이동거리를 갱신하기 위해 directx와 directy를 순회한다.
    for k in range(3):
        #현재 위치에서 dx와 dy를 갱신한다.
        dx, dy = x + directx[k], y + directy[k]
        #갱신한 위치가 범위 내에 있고, 빈 공간인 경우에만 탐색을 진행한다.
        if 0 <= dx < R and 0 <= dy < C and arr[dx][dy] == '.':
        #갱신한 위치를 'x'로 바꿔준다.-> 해당 위치에 파이프라인이 연결된 경우이다.
            arr[dx][dy] = 'x' 
            #재귀적으로 다음 위치를 탐색한다.-> 다음 위치에서 파이프라인이 연결된 경우 True를 반환한다.
            if dfs(dx, dy):
                #모든 탐색을 진행했음에도 파이프라인이 연결되지 않은 경우 False를 반환한다.
                return True
    return False
#각 행에 대해 dfs 함수를 첫 번째 열부터 시작해서 호출한다.
for i in range(R):
    #i번째 행의 첫 번째 열에서부터 탐색을 시작한다.
    dfs(i, 0)
#파이프라인이 연결된 갯수를 출력한다.
print(cnt)