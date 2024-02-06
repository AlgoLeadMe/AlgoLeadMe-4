import sys
input=sys.stdin.readline

# 명령의 수 N을 선언한다.
N=int(input())

# 정수를 저장하는 큐를 선언한다.
command_queue=[]

# N번 반복하면서 각 명령들을 수행한다.
for _ in range(N):
    # 명령을 입력받을 리스트를 선언한다.
    command=input().rstrip().split() 
    # 명령의 첫번째 요소가 push이면 해당 문을 수행한다.
    if command[0]=="push":
        command_queue.append(command[1])
    # 명령의 첫번째 요소가 pop이면 해당 문을 수행한다.
    elif command[0]=="pop":
        print(command_queue.pop(0) if command_queue else -1)
    # 명령의 첫번째 요소가 size이면 해당 문을 수행한다.
    elif command[0]=="size":
        print(len(command_queue))
    # 명령의 첫번째 요소가 empty이면 해당 문을 수행한다.
    elif command[0]=="empty":
        print(0 if command_queue else 1)
    # 명령의 첫번째 요소가 front이면 해당 문을 수행한다. 
    elif command[0]=="front":
        print(command_queue[0] if command_queue else -1)
    # 명령의 첫번째 요소가 back이면 해당 문을 수행한다. 
    elif command[0]=="back":
        print(command_queue[-1] if command_queue else -1)


