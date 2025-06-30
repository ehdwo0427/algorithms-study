# https://school.programmers.co.kr/learn/courses/30/lessons/42577

def solution(phone_book):
    answer = True
    # 해시테이블 생성
    hashmap = {}
    # 해시테이블에 값 추가하기
    for st in phone_book:
        hashmap[st] = 1
    # phone_book에 있는 값 꺼내서 탐색하기.
    for st in phone_book:
        # 한글자씩 추가하며 확인 st랑 start_num이 같으면 pass
        start_num = ""
        if not answer:
            break
        for st_r in st:
            start_num += st_r
            # 접두사가 있으면 반환, 본인거랑 겹치면 안됨
            if start_num in hashmap and start_num != st:
                answer = False
                return answer
        
    return answer