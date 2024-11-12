def find_year(max_year1, max_year2, target_x, target_y):
    year = target_x
    while year <= max_year1 * max_year2:
        if (year - target_y) % max_year2 == 0:
            return year
        year += max_year1
    return -1

T = int(input())
for _ in range(T):
    max_year1, max_year2, target_x, target_y = map(int, input().split())
    print(find_year(max_year1, max_year2, target_x, target_y))