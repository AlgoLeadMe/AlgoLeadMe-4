n = int(input())
graph = input()
cnt = 1

for i in range(1,n):
    if graph[i]=='E' and graph[i-1]=='W':
        cnt += 1
print(cnt)