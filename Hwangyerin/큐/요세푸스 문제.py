from collections import deque
n,k=[int(x) for x in input().split()]
answer = []
queue=deque([i for i in range(1,n+1)])

while queue:
    for i in range(k-1):
        queue.append(queue.popleft())
    answer.append(queue.popleft())
answer = str(answer)[1:-1]
print("<" + answer + ">")
