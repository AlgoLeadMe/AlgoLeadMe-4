import sys
from collections import deque

input = sys.stdin.readline
queue = deque()
cowNum = 1 
N = int(input()) # 줄에 설 소가 몇마리인지 입력받기
for _ in range(N):
    cmd = input().split()
    action, side = cmd[0], cmd[1]
    if action == "A":
        if side == "L":
            queue.appendleft(cowNum)
        else:
            queue.append(cowNum)
        cowNum += 1 
    else : # action == "D"
        K = cmd[2]
        if side == "L":
            for _ in range(int(K)):
                queue.popleft()
               
        else:
            for _ in range(int(K)):
                queue.pop()

print(*queue,sep="\n")