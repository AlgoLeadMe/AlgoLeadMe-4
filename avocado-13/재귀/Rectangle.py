n, m = map(int,input().split())


def rec(row,col):
    
    num, deno = max(row,col), min(row,col)
    if deno == 0:
        return 0 
    return num//deno + rec(num%deno,deno)

print(rec(n,m))