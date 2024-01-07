def solution(s):
    #스택 초기화
    bracket = []
    for i in range(len(s)):
        #스택이 비어있고 닫힌괄호가 들어오는 경우 False return 
        if len(bracket) == 0 and s[i]==")":
            return False
        
        #열린 괄호가 들어오는 경우 스택에 append
        if s[i] == "(":
            bracket.append("(")
            
        #스택이 비어있지 않고 닫힌괄호가 들어오는 경우 pop
        elif len(bracket)!=0 and s[i] == ")":
            bracket.pop()

    #스택이 비어있으면 True 아니면 False            
    if len(bracket)==0:
        return True
    else:
        return False
    
# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(solution(input()))
