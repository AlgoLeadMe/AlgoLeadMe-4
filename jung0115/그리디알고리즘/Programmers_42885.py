# 23차시 2024.11.02.토 : 프로그래머스 - 구명보트(Lv.2)
from collections import deque

def solution(people, limit):
  answer = 0
  people.sort(reverse = True)
  queue = deque(people)
  
  while len(queue) > 1 :
    if queue[0] + queue[-1] <= limit :
      queue.pop()
      queue.popleft()
      answer += 1
    else :
      queue.popleft()
      answer += 1
  
  if len(queue) > 0 :
    answer += 1
  
  return answer