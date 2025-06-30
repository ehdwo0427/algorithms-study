# https://school.programmers.co.kr/learn/courses/30/lessons/77486

def solution(enroll, referral, seller, amount):
    # 결과 배열 초기화
    result = [0] * len(enroll)
    # 이름 → 인덱스 매핑
    idx = {name: i for i, name in enumerate(enroll)}
    # referral 관계 저장, "-"는 -1 인덱스로
    parent = [idx[ref] if ref != '-' else -1 for ref in referral]

    def distribute(person_idx, money):
        if person_idx == -1 or money == 0:
            return
        commission = money // 10  # 뗄 금액
        result[person_idx] += money - commission
        distribute(parent[person_idx], commission)

    # 판매 기록 처리
    for s, cnt in zip(seller, amount):
        distribute(idx[s], cnt * 100)

    return result