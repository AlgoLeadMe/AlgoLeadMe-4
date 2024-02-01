#피보나치 함수
def fibonacci(n):
    if n == 0: #0번째 피보나치 수는 0
        return 0
    elif n == 1: #1번째 피보나치 수는 1
        return 1
    else: #2번째부터는 바로 앞 두 피보나치 수의 합
        return fibonacci(n-1) + fibonacci(n-2)
n = int(input())
print(fibonacci(n))
