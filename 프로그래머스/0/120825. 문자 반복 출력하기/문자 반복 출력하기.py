def solution(my_string, n):
    answer = ''
    for string in my_string:
        for i in range(n):
            answer += string
    return answer