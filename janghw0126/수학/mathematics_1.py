# M과 N을 받는다
M = int(input())
N = int(input())

# 이중 for문을 통해 비교할 수(i)와 2부터 자기 자신까지 반복할 수(j)를 구한다.
decimal = []
for i in range(M, N+1):
	for j in range(2, i+1):
    #j와 i가 같다면 소수이므로 decimal에 추가해준다.
		if j == i:
			decimal.append(i)
    #그렇지 않다면 i를 j에 나눈 나머지를 비교하여 나누어 떨어지면 소수가 아니게 되므로 break를 통해 빠져 나온다.
		if i % j == 0:
			break

#decimal이 false인 경우(아무 것도 없는 경우) -1을 출력하고, 그렇지 않으면 모든 리스트의 요소를 더한 값과 리스트의 0번째(가장 작은 값) 요소를 출력한다.
if not decimal:
	print(-1)
else:
	print(sum(decimal))
	print(decimal[0])