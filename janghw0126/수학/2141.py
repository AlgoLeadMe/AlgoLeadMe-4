import sys
N = int(sys.stdin.readline())

circle, result = [0]*N, [0]*N
for i in range(N):
    circle[i] = int(sys.stdin.readline())

matrix = [0 for _ in range(max(circle)+1)]
for c in circle:
    matrix[c]+=1

for n in range(N):
    k = 1
    while (k*k <= circle[n]):
        if circle[n] % k == 0: # k가 circle[n]의 약수이면 다음 2가지 경우로 나눠 생각
            if k*k != circle[n]: # 1) circle[n]과 k**2이 같지 않을 때 : 약수 k와 circle[n]//k의 개수를 더한다. 
                result[n] += matrix[k] + matrix[circle[n]//k]
            else: # 2) circle[n]과 k**2이 같을 때 : k의 제곱과 같으면 약수는 k 하나이므로 matrix[k] 하나만 더한다. 
                result[n] += matrix[k]
        k += 1

answer = ""
for r in result:
    answer += str(r-1)+"\n" # -1은 while 문에서 자기 자신을 배수로 취급하여 센 것을 빼기 위해서이다. 
print(answer)