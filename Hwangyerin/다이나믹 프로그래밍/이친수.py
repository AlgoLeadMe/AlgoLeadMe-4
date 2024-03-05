def fib(n, dic={}):
    if n in dic:
        return dic[n]
    if n <= 1:
        return n
    else:
        dic[n] = fib(n-1) + fib(n-2)
        return dic[n]
    
n = int(input())
print(fib(n))
