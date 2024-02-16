import sys
input=sys.stdin.readline
#행의 수인 R과 열의 수인 C를 입력받는다.
R,C=map(int,input().split())
#R개의 줄에 걸쳐 C개의 문자를 입력받아 2차원 리스트에 저장한다.
line=[list(input().strip())for _ in range(R)]
#이동방향을 나타내는 리스트를 작성한다.
D=(-1,0,1)
#스택을 초기화하고 파이프라인의 갯수를 세는 변수 count를 초기화한다. 
stack,count=[],0
#행의 수인 R만큼 반복한다.
for i in range(R):
    #현재 행의 위치를 선언한다.
    Ci=i
    #현재 열의 위치를 선언한다. 초기값은 마지막 열인 C-1이다.
    Cj=j=C-1
    #무한루프를 반복한다.
    while True:
        #현재 열의 위치가 1 이하면 파이프라인의 끝에 도착했다는 뜻이다.
        if Cj<1:
            while stack:
                #스택에 남아있는 좌표를 하나씩 꺼내면서 line 리스트에서 해당 위치를 'o'로 바꾼다.
                line[Ci][Cj]='o'
                Ci,Cj=stack.pop()
            #현재 위치 ci와 cj도 'o'로 바꾸고, 파이프라인의 개수인 count를 증가시킨다.
            line[Ci][Cj]='o'
            count+=1
            #반복문을 종료한다.
            break
        #이동 가능한 방향이 있는지를 나타내는 변수인 direction을 초기화한다.
        direction=False
        #line 리스트에서 이동 방향을 하나씩 가져온다.
        for k in range(3):
            #만약 이동한 위치가 행렬 범위 내에 있고, 해당 위치가 '.'인 경우에는 이동이 가능하다.
            if 0<=Ci+D[k]<R and line[Ci+D[k]][Cj-1]=='.':
                # direction를 True로 변경하고, 스택에 현재 위치를 추가한다.
                direction=True
                # Ci와 Cj를 갱신하여 이동한 위치로 업데이트한다.
                stack.append((Ci,Cj))
                Ci,Cj=Ci+D[k],Cj-1
                break
        #이동 가능한 방향이 없는 경우
        if not direction:
            # 현재 위치 list[ci][cj]를 '_'로 바꾼다.
            line[Ci][Cj]='_'
            #스택에서 좌표를 꺼내온다.
            try:
                Ci,Cj=stack.pop()
            # 만약 스택이 비어있다면, 더 이상 이동할 수 없으므로 반복문을 종료한다.
            except:
                break
            
print(count)