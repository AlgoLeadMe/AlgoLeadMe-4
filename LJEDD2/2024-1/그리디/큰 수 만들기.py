def solution(number, k):
    # 일단 저장! 큰 수가 나오면 빼!
    stack = []
    for i in number:
        if not stack:
            stack.append(i)
        else:
            while stack:
                    if i > stack[-1] and k > 0:
                        k -= 1
                        stack.pop()
                    else:
                        break
            stack.append(i)
    return''.join(stack[:len(number)-k])
