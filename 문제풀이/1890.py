# 0,0 시작
# 0, 0 만나면 끝
from collections import deque

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
queue = deque([])
queue.append((0, 0))
cnt = 0

while queue:
    x, y = queue.popleft()
    num = arr[x][y]
    if 0 <= (x + num) < N and 0 <= y < N:
        if arr[x + num][y] == 0:
            cnt += 1

        else:
            queue.append((x + num, y))

    if 0  <= x < N and 0 <= (y + num) < N:
        if arr[x][y + num] == 0:
            cnt += 1

        else:
            queue.append((x, y + num))

print(cnt)