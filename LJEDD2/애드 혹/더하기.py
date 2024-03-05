n = int(input())
n_list = list(map(int,input().split()))
diff = sum(n_list[1::2]) - sum(n_list[::2])

# N=3이고 홀수합이 더 많다면 불가능
if n == 3 and diff < 0 :
    print(-1)
# 그 외에는 절댓값의 차이 만큼 +1
else:
    print(abs(diff))