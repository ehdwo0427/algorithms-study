# https://school.programmers.co.kr/learn/courses/30/lessons/1845

def solution(nums):
    answer = 0
    # 절반만 뽑으면 된다.
    # 절반중에 겹치지 않는 포켓몬이 절반 이상이면 절반 값 / 이하면 그 값을 출력한다.
    max_len = len(nums) / 2
    nums_len = len(set(nums))
    if max_len >= nums_len:
        answer = nums_len
    else:
        answer = max_len
    
    return answer


# 최대한 많은 종류의 폰켓몬을 포함해서 N / 2 마리를 선택하니까.

# max == 배열의 길이
# num_len == 배열의 집합
# 절반보다 크면 집합 값만큼 뽑고, 아니면 n / 2 값만큼만 뽑는다.