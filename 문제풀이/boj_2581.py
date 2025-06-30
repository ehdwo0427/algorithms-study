# M 이상 N 이하의 자연수 중 소수인 것을 모두 찾아 첫째 줄에 그 합을, 둘째 줄에 그 중 최솟값을 출력한다.
arr = []
M = int(input())
N = int(input())
for i in range(M, N + 1):
    if i % 2 != 0 and i % 3 != 0 and i % 5 != 0 and i % 7 != 0:
        arr.append(i)
if len(arr) == 0:
    print(-1)
    exit(0)
print(sum(arr))
print(arr[0])