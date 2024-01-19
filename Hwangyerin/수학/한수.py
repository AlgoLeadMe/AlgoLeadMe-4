n = int(input())
if n<100:
    print(n)
else:
    hansu = 99
    for i in range(100,n+1):
        numList = list(map(int,str(i)))
        if numList[0]-numList[1] == numList[1]-numList[2]:
            hansu += 1
    print(hansu)
