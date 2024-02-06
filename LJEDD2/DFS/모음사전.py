def solution(word):
    words = "AEIOU"
    result = [] 
    
    def dfs(cnt,tmp):
        if cnt == 5:
            return
            
        for i in words:
            result.append(tmp+i)
            dfs(cnt+1, tmp+i)
            
    dfs(0,"")
    return result.index(word) + 1