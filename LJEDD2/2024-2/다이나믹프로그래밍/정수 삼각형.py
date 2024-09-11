def solution(triangle):
    for row in range(1, len(triangle)):
        for col in range(row + 1):
            if col == 0:
                triangle[row][col] += triangle[row-1][col]  # 바로 위 행 같은 열
            elif col == row:
                triangle[row][col] += triangle[row-1][col-1]  # 바로 위 행의 왼쪽 열
            else:
                right, left = triangle[row-1][col], triangle[row-1][col-1]
                triangle[row][col] += max(right, left)  # 두 값 중 더 큰 값 
    
    answer = max(triangle[-1])
    return answer