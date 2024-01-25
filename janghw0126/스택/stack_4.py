import sys
input = sys.stdin.readline
 
while True:
    s = input().rstrip()
    #온점으로 끝날 경우, 입력의 종료조건이므로 반복문을 빠져나간다.
    if s == '.':  
        break
    
    #stack을 선언한다.
    stack = []
    #짝이 이루어지는지 판별하는 변수를 선언한다.
    flag = True    
 
    #입력의 길이만큼 반복문을 돌린다.
    for i in range(len(s)):
        #처음 여는 괄호인 경우 stack에 추가해준다.
        if s[i] == '(' or s[i] == '[':
            stack.append(s[i])
        
        #stack이 있고 닫는 괄호가 나올 경우 pop을 실행해준다.
        elif stack and (s[i] == ')' or s[i] == ']'): 
            if s[i] == ')' and stack[-1] == '(':
                stack.pop()
            elif s[i] == ']' and stack[-1] == '[':
                stack.pop()
            # (]) 인 경우 False를 반환한다.
            else:   
                flag = False

        # stack에 아무것도 없으면서 닫힌 괄호가 나오는 경우 False를 반환한다.
        elif not stack and (s[i] == ')' or s[i] == ']'): 
            flag = False
 
    #flag가 True이고 스택에 아무것도 없는 경우 yes를 출력한다.
    if flag and not stack:
        print('yes')
    #아닌 경우 no를 출력한다.
    else:
        print('no')