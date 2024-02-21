x = int(input())
d = [-1 if num == 4 or num == 7 else 0 for num in range(x+1)]


for i in range(3,x+1):
    if i%5 == 0:
        d[i] = d[i-5] + 1 
    elif i%5 != 0 and i!= 4 and i!= 7 :
        d[i] = d[i-3] + 1 
    

print(d[x])