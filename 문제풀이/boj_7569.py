from collections import deque

m, n, h = map(int, input().split())

arr = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]

queue = deque()

visited = [[[False] * m for _ in range(n)] for _ in range(h)]

dx = [-1, 1, 0, 0, 0, 0]
dy = [0 , 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

for k in range(h):
    for i in range(n):
        for j in range(m):
            if arr[k][i][j] == 1:
                arr[k][i][j] = 1
                queue.append((k, i, j))
                visited[k][i][j] = True


while queue:
    z, x, y = queue.popleft()
    for d in range(6):
        nx, ny, nz = x + dx[d], y + dy[d], z + dz[d]
        if 0 <= nx < n and 0 <= ny < m and 0 <= nz < h and not visited[nz][nx][ny] and arr[nz][nx][ny] == 0:
            visited[nz][nx][ny] = True
            queue.append((nz, nx, ny))
            arr[nz][nx][ny] = arr[z][x][y] + 1

max_day = 0
for k in range(h):
    for i in range(n):
        for j in range(m):
            if arr[k][i][j] == 0:
                print(-1)
                exit()
            if arr[k][i][j] > max_day:
                max_day = arr[k][i][j]
print(max_day - 1)
