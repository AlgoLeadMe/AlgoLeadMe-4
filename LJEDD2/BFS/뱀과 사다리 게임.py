from collections import deque

def BFS():
    queue = deque([[1, 0]])
    visited[1] = True
    while queue:
        cur_x, dice_count = queue.popleft()

        if cur_x == 100:
            print(dice_count)
            exit()

        for d in range(1, 7):
            next_x = cur_x + d

            if next_x <= 100 and not visited[next_x]:
                # 뱀과 사다리 지역을 만나면 일단 이동 먼저 해야 한다. (주의)
                if next_x in jump:
                    next_x = jump[next_x] # 텔레포트 !
                    
                if not visited[next_x]:
                    visited[next_x] = True
                    queue.append([next_x, dice_count+ 1])

# 사다리와 뱀
n,m = map(int,input().split())
visited = [False for _ in range(101)]
jump = {}
for _ in range(n+m):
    loc = list(map(int, input().split()))
    # 텔레포트!
    jump[loc[0]] = loc[1]
BFS()