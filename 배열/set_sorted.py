
# numbers = [2, 1, 3, 4, 1]
# result = [2, 3, 4, 5, 6, 7]

# numbers에서 서로 다른 인덱스에 있는 2개의 수를 뽑아 더해 만들 수 있는 모든 수를 배열에 오름차순으로 담아 반환하는 함수를 완성하세요.


def solution(numbers):
    arr = []
    
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            arr.append(numbers[i] + numbers[j])
    
    arr = sorted(set(arr))
    return arr


print(solution([2, 1, 3, 4, 1]))