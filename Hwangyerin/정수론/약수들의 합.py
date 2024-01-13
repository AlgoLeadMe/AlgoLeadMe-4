while True:
    L =[]
    num = int(input())
    if num == -1:
        break
    else:
        for j in range(1, num//2 + 1):
            if num%j == 0:
                L.append(j)
        if sum(L) == num:
            print(num, end=' = ')
            print(*L,sep=' + ')
        else:
            print(num,'is NOT perfect.')
