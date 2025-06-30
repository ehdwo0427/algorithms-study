# https://school.programmers.co.kr/learn/courses/30/lessons/42579

def solution(genres, plays):
    answer = []
    hash_map = {}
    for i in range(len(genres)):
        if genres[i] in hash_map:
            hash_map[genres[i]].append((plays[i], i))
        else:
            hash_map[genres[i]] = [(plays[i], i)]
    
    for genres in hash_map:
        hash_map[genres].sort(key=lambda x: (-x[0], x[1]))
    
    sorted_hash_map = dict(sorted(hash_map.items(), key=lambda x: -sum(play[0] for play in x[1])))
    
    for genre in sorted_hash_map:
        answer.extend([index for _, index in hash_map[genre][:2]])
    
    return answer