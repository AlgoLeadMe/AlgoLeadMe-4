#테스트 케이스의 갯수를 입력한다.
T=int(input())

#테스트 케이스의 갯수만큼 반복한다.
for _ in range(T):
    #문서의 갯수와, 몇 번째로 인쇄되었는지 궁금한 문서가 현재 몇번째에 놓여있는지 나타내는 정수 M을 입력받는다.
    N,M=map(int,input().split())
    #N개 문서의 중요도를 입력받고 리스트로 입력받는다.
    data=list(map(int,input().split()))

    #문서가 몇번째로 인쇄되는지 확인하기 위해서 변수를 초기화한다.
    result=1
 
    #문서가 없어질 때까지 초기화한다.
    while data:
        #0번째 문서의 중요도가 중요도의 최대크기보다 작다면 수행할 문이다.
        if data[0]<max(data):
            #0번째 문서를 pop하고 리스트 뒤에 추가한다.
            data.append(data.pop(0))
        #0번째 문서의 중요도가 max라면 수행할 문이다.
        else:
            #리스트에 max밖에 없을 경우 이 문을 빠져나간다.
            if M==0:
                break
            #0번째 데이터를 pop하고 몇번째로 출력되는지 확인하는 result변수를 1씩 더한다.
            data.pop(0)
            result+=1
        #현재 궁금한 문서의 위치인 M을 업데이트한다.
        #M이 0보다 큰 경우 현재위치에서 1씩 감소시키고 아닌 경우 현재 위치를 M에 할당한다.
        M=M-1 if M>0 else len(data)-1
    #문서가 몇 번째로 인쇄되는지 출력한다.
    print(result)
