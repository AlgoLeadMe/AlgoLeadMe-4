import sys
input = sys.stdin.readline

def s(n):
    return int(n*(n+1)/2)

n = int(input())

i = 2 
if n == 1:
    print("%d/%d"%(1,1))
else: 
    while True:
        if s(i-1) < n and n <= s(i):
            line_num = i
            break
        else :
            i += 1

    row_num = s(i) - n

    if i%2 != 0:
        print("%d/%d"%(1+row_num,i-row_num))
    else :
        print("%d/%d"%(i-row_num,1+row_num))