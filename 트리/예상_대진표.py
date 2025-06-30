# https://school.programmers.co.kr/learn/courses/30/lessons/12985

def solution(n, a, b):
    round = 0
    while a != b:
        a = (a + 1) // 2
        b = (b + 1) // 2
        round += 1
    return round