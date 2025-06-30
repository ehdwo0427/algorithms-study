# https://school.programmers.co.kr/learn/courses/30/lessons/12981

def solution(n, words):
    answer = []
    used_words = set()
    prev_word = words[0][0]
    
    for i, word in enumerate(words):
        if word in used_words or word[0] != prev_word:
            return [(i % n) + 1, (i // n) + 1]
        
        used_words.add(word)
        prev_word = word[-1]

    return [0, 0]


# set을 사용하여 시간 복잡도는 O(1) 이므로 최종은 O(N)이다.