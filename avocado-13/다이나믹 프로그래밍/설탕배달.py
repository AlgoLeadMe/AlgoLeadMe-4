x = int(input())
d = [n if n < 3 else 100 for n in range(x+1) ]
d[0] = d[1] = d[2] = 0
for i in range(3,x+1):
    if 3<i<5 or i<3 :
        d[i] = -1 
    if i%5 != 0:
        d[i] = min(d[i],d[i-3] + 1 )
    if i%5 == 0:
        d[i] = min(d[i], d[i//5] + 1)

print(d[x])