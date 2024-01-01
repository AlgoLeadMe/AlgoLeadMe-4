def solution(s):
    bracket = []
    for i in range(len(s)):
        if len(bracket) == 0 and s[i]==")":
            return False
        if s[i] == "(":
            bracket.append("(")
        elif s[i] == ")":
            if len(bracket)!=0:
                bracket.pop()
                
    if len(bracket)==0:
        return True
    else:
        return False

print(solution(input()))
