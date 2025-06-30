# https://school.programmers.co.kr/learn/courses/30/lessons/42576

def solution(participant, completion):
    hashmap = {}
    hash_sum = 0
    for i in participant:
        hashmap[hash(i)] = i
        hash_sum += hash(i)
    
    for comp in completion:
        hash_sum -= hash(comp)
    answer = hashmap[hash_sum]
    return answer