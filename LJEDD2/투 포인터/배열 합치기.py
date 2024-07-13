n, m = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

a_idx = 0
b_idx = 0
result = []

# 최대 길이를 n,m 둘 다 달성하면 탈출 
while a_idx != n or b_idx != m:
    # 한쪽이 이미 정렬이 끝난 경우 
    if a_idx == n:
        result.append(b[b_idx])
        b_idx += 1
        continue

    elif b_idx == m :
        result.append(a[a_idx])
        a_idx += 1
        continue

    # 투포인터 정렬 

    if a[a_idx] < b[b_idx]:
        result.append(a[a_idx])
        a_idx += 1

    else:
        result.append(b[b_idx])
        b_idx += 1

print(*result)
