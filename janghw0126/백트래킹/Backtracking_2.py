N,M=map(int,input().split())
lst=[]

def dfs(start):
    #탈출 조건에 해당한다.
    if len(lst)==M: 
        print(''.join(map(str,lst)))
        return
    
    for i in range(start,N+1):
        if i not in lst:
            lst.append(i)
            dfs(i+1)
            lst.pop()

dfs(1)