S = int(input())
hap = 0
cnt = 0
for i in range(1,S+1):
    hap+=i
    cnt+=1
    if hap > S:
        cnt -= 1
        break

print(cnt)
