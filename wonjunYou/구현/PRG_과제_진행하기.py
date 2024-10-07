def solution(plans):
    stack = []
    result = []

    plans.sort(key=lambda x: x[1])

    for i in range(len(plans) - 1):
        current_start_time = plans[i][1]
        next_start_time = plans[i + 1][1]

        playtime_difference = calculateDifference(current_start_time, next_start_time)

        if int(plans[i][2]) > playtime_difference:
            stack.append([plans[i][0], int(plans[i][2]) - playtime_difference])
        else:
            result.append(plans[i][0])
            remaining_time = playtime_difference - int(plans[i][2])

            while stack and remaining_time > 0:
                previous_task, previous_time = stack.pop()
                if previous_time > remaining_time:
                    stack.append([previous_task, previous_time - remaining_time])
                    remaining_time = 0
                else:
                    result.append(previous_task)
                    remaining_time -= previous_time

    result.append(plans[-1][0])

    while stack:
        result.append(stack.pop()[0])

    return result

def calculateDifference(current_time, next_time):
    h1, m1 = map(int, current_time.split(":"))
    h2, m2 = map(int, next_time.split(":"))

    current_minutes = h1 * 60 + m1
    next_minutes = h2 * 60 + m2

    return next_minutes - current_minutes
