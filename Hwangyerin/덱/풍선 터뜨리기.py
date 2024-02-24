from collections import deque
import sys
input = sys.stdin.readline

# 입력 받기
balloon_count = int(input())
balloon_list = deque(enumerate([int(x) for x in input().split()],start=1))
result = []

idx, paper_number = balloon_list.popleft()
result.append(idx)

# 풍선 터뜨리는 과정
while balloon_list:
    if paper_number > 0:
        for _ in range(paper_number-1):
            balloon_list.append(balloon_list.popleft())
       
    elif paper_number < 0:
        for _ in range(abs(paper_number)):
            balloon_list.appendleft(balloon_list.pop())
    idx, paper_number = balloon_list.popleft()
    result.append(idx)

print(*result)

