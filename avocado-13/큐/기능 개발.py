from math import ceil
from collections import deque

def solution(progresses, speeds):
    answer = []
    period = deque([ceil((100 - p) / s) for p, s in zip(progresses, speeds)])

    while period:
        release_count = 0
        first_period = period.popleft()
        release_count += 1

        while period and period[0] <= first_period:
            period.popleft()
            release_count += 1

        answer.append(release_count)

    return answer
