def solution(distance, rocks, n):
    rocks.sort()
    rocks.append(distance)
    left, right = 1, distance
    
    while left <= right:
        mid = (left+right) // 2
        current = 0
        removed_rocks = 0
        
        for rock in rocks:
            if rock-current < mid:
                removed_rocks += 1
            else:
                current = rock
                
        if removed_rocks > n:
            right = mid-1
        else:
            answer = mid
            left = mid+1
        
    return answer