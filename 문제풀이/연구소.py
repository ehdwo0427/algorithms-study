from collections import deque
import copy

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
max_cnt = 0

def bfs(arr, queue, visited):
    while queue:
        x, y = queue.popleft()
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and arr[nx][ny] == 0:
                visited[nx][ny] = True
                queue.append((nx, ny))
                arr[nx][ny] = 2
    
    cnt = 0
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 0:
                cnt += 1
    return cnt

def wall(board, x, y, wall_queue, virus_queue):
    global max_cnt
    if len(wall_queue) == 3:
        visited = [[False] * m for _ in range(n)]
        queue = virus_queue.copy()
        arr = copy.deepcopy(board)
        cnt = bfs(arr, queue, visited)
        if cnt > max_cnt:
            max_cnt = cnt
        return

    for i in range(x, n):
        for j in range(m):
            if board[i][j] == 0:
                wall_queue.append((i, j))
                board[i][j] = 1
                wall(board, i, j, wall_queue, virus_queue)
                board[i][j] = 0
                wall_queue.pop()

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
virus_queue = deque()
wall_queue = deque()

for i in range(n):
    for j in range(m):
        if board[i][j] == 2:
            virus_queue.append((i, j))

wall(board, 0, 0, wall_queue, virus_queue)
print(max_cnt)
