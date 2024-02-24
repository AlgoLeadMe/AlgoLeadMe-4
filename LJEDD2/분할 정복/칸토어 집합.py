def Cantorian(start, size):
    if size == 1:
        return

    # 실패 코드 
    # s[size : size // 3 * 2] = ' ' * (size // 3)

    # 3등분해서 가운데부분만 빈칸으로 바꿔주기
    s[start + size//3 : start + (size)// 3 *2] = ' ' * (size//3)

    # 1/3과 3/3 부분에 대해서도 똑같이 3등분해서 빈칸 만들어주는 것을 반복해야 함
     
    Cantorian(start,  size // 3)  # 왼쪽 - 재귀 호출
    Cantorian(start +  size // 3 * 2,  size // 3)  # 오른족 - 재귀 호출 

while True:
    try:
        size = 3 ** int(input())
        s = ['-'] * size

        # '-' * 3*n , ' '*3*n , '-' *3*n
        Cantorian(0, size)
        
        print(''.join(s))

    except Exception as e:
        break