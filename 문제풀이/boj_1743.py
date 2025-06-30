from collections import deque

N, M, K = map(int, input().split())

grid = [[0] * M for _ in range(N)]
visited = [[False] * M for _ in range(N)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
max_cnt = 0

for k in range(K):
    r , c = map(int, input().split())
    grid[r - 1][c - 1] = 1

for i in range(N):
    for j in range(M):
        if not visited[i][j] and grid[i][j] == 1:
            cnt = 1
            queue = deque()
            queue.append((i, j))
            visited[i][j] = True
            while queue:
                x, y = queue.popleft()
                for d in range(4):
                    nx, ny = x + dx[d], y + dy[d]
                    if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and grid[nx][ny] == 1:
                        queue.append((nx, ny))
                        cnt += 1
                        visited[nx][ny] = True
                if cnt > max_cnt:
                    max_cnt = cnt
print(max_cnt)