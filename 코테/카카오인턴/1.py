def solution(s):
    engs = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    nums = [str(i) for i in range(10)]

    for i in range(10):
        if engs[i] in s:
            s = s.replace(engs[i], nums[i])

    return int(s)


print(solution("one4seveneight"))
