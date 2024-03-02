# def fib(n, dic={}):
#     if n in dic:
#         return dic[n]
#     if n <= 1:
#         return n
#     else:
#         dic[n] = fib(n-1) + fib(n-2)
#         return dic[n]
    
# n = int(input())
# print(fib(n))

for i in range(32,100):
    if bin(i)[2] != 0 and '11' not in bin(i)[2:]:
        print(bin(i)[2:])
