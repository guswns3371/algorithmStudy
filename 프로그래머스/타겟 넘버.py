"""
타겟 넘버 https://programmers.co.kr/learn/courses/30/lessons/43165
dfs
"""
from collections import deque


def solution(numbers, target):
    answer = 0
    q = deque([(0, 0, "")])  # index, value
    while q:
        index, value, string = q.pop()
        print(f"index={index},value={value}, {string}")
        if value == target and index == len(numbers):
            answer += 1
            print("-----------------")
            continue
        if index >= len(numbers):
            print("end")
            continue

        q.append((index + 1, value + numbers[index], string + f"+{numbers[index]}"))
        q.append((index + 1, value - numbers[index], string + f"-{numbers[index]}"))
    return answer


def solution2(numbers, target):
    if not numbers and target == 0:
        return 1
    elif not numbers:
        return 0
    else:
        return solution(numbers[1:], target - numbers[0]) \
               + solution(numbers[1:], target + numbers[0])


print(solution([1, 1, 1, 1, 1], 3))
