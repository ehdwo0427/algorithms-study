from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
queue = deque()

n = int(input())
grid = [list(input().strip()) for _ in range(n)]
visited = [[False] * n for _ in range(n)]

answer = []
for i in range(n):
    for j in range(n):
        if grid[i][j] == '1' and not visited[i][j]:
            cnt = 1
            queue.append((i, j))
            visited[i][j] = True
            while queue:
                x, y = queue.popleft()
                for d in range(4):
                    nx, ny = x + dx[d], y + dy[d]
                    if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == '1' and not visited[nx][ny]:
                        queue.append((nx, ny))
                        visited[nx][ny] = True
                        cnt += 1
            answer.append(cnt)
answer.sort()
print(len(answer))
for i in answer:
    print(i)