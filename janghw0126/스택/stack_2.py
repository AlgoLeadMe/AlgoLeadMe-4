import sys
input = sys.stdin.readline

#테스트 데이터의 갯수를 입력받는다.
T=int(input())

for i in range(T):
    stack = []
    #반복문을 통해 테스트 데이터를 입력받는다.
    #sys 모듈을 쓸 경우 개행문자도 문자열에 포함되기 때문에 rstrip()을 통해 제거해준다.
    for i in input().rstrip():
        #"("을 만났을 경우 stack에 추가한다.
        if i == "(":
            stack.append(i)
        #"("이 아닌 경우 else구문을 실행한다.
        else:
	    #오류가 발생할 가능성이 있는 코드->즉, ")"을 만났을 때 pop()을 통해 제거해준다.
            try:
                stack.pop()
	    #에러가 발생했을 경우 시행할 코드->즉, stack에 아무것도 없어서 pop()을 실행하지 못할 경우에 No를 출력해준다.
            except:
                print("NO")
                break
    #반복문을 통해 모든 테스트 데이터를 다 돌았을 때 시행한다.
    else:
        # 스택이 안 비어있는 경우에는 NO를 출력하고 아닌 경우 Yes를 출력한다.
        print("NO" if stack else "YES")