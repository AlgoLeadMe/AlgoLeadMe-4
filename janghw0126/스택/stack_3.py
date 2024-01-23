#n개의 정수를 입력받는다.
n=int(input())
#스택이 저장될 리스트를 초기화한다.
stack=[]
#result로 저장될 리스트를 초기화한다.
result=[]
count=0
#표현이 불가능할 경우에는 NO로 나오도록 X를 선언한다.
X=True

#n 변수로 n개의 반복을 돌릴 수 있도록 반복문을 이용한다.
for _ in range(n):
    num=int(input())
    
    #반복문을 이용해서 count가 입력받은 num보다 작을 때 돌아가게 한다.
    while count<num:
        #스택이 비어있을 경우를 대비해서 count를 1 증가시켜준다.
        count+=1
        stack.append(count)\
        #stack이 push된 것이니까 "+"를 append 해준다.
        result.append("+")

    #stack의 맨 꼭대기에 있는 것이 num과 같다면 if문을 실행해준다.
    if stack[-1]==num:
        #그 수를 빼주고 result에는 "-"를 추가해준다.
        stack.pop()
        result.append("-")
    #맨 꼭대기의 수가 num과 같지 않으면 False로 해주고 반복문을 빠져나간다.
    else:
        X=False
        break
#만약 표현이 불가능할 경우에는 "NO"를 출력해준다.
if X==False:
    print("NO")
#아닐 경우에는 result 리스트에 저장된 요소를 차례로 출력해준다.
else:
    for i in result:
        print(i)

