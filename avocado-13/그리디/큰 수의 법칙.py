
N,M,K = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort(reverse=True)

a = M//K
b = M%K
total = 0

if a<= b+1:
  total = a*K*arr[0] + b*arr[1]
else :
  b = a-1
  max_value = M-b
  total = max_value*arr[0] + b*arr[1]
print(total)