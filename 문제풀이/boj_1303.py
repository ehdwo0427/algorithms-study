from collections import deque

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

M, N = map(int, input().split())

arr = [list(str(input().strip())) for _ in range(N)]

visited = [[False] * M for _ in range(N)]

w_cnt, b_cnt = 0, 0

for i in range(N):
    for j in range(M):
        if not visited[i][j]:
            queue = deque()
            # queue = []
            queue.append((i, j))
            visited[i][j] = True
            cnt = 1
            while queue:
                x, y = queue.popleft()
                # x, y = queue.pop(0)
                for d in range(4):
                    nx, ny = x + dx[d], y + dy[d]
                    if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == False and arr[nx][ny] == arr[i][j]:
                        queue.append((nx, ny))
                        visited[nx][ny] = True
                        cnt += 1
            if arr[i][j] == 'W':
                w_cnt += cnt * cnt
            elif arr[i][j] == 'B':
                b_cnt += cnt * cnt

print(w_cnt, b_cnt)