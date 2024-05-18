n = int(input())
a = list(map(int,input().split()))
'''
브루트포스 X 누적합 활용법 익히기 
a, b, c, d의 숫자가 있다고 가정할 때,
a * b + a * c + a * d = ab + ac + ad = a(b+c+d) 로 표현 가능. 
'''
ans, sumv = 0, sum(a) # 누적합에서 시작 

for i in range(n):
    # (b+c+d) 는 sumv-a[i] 
    ans += a[i] * (sumv - a[i])

print(ans // 2)