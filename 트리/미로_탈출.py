# https://school.programmers.co.kr/learn/courses/30/lessons/159993

from collections import deque

def bfs(maps, start, target):
    N, M = len(maps), len(maps[0])
    visited = [[False]*M for _ in range(N)]
    queue = deque([(start[0], start[1], 0)])
    visited[start[0]][start[1]] = True

    while queue:
        x, y, dist = queue.popleft()
        if maps[x][y] == target:
            return dist
        for dx, dy in [(-1, 0),(1, 0),(0, -1),(0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and maps[nx][ny] != 'X':
                visited[nx][ny] = True
                queue.append((nx, ny, dist + 1))
    return -1

def solution(maps):
    N, M = len(maps), len(maps[0])
    s = l = e = None
    for i in range(N):
        for j in range(M):
            if maps[i][j] == 'S': s = (i, j)
            elif maps[i][j] == 'L': l = (i, j)
            elif maps[i][j] == 'E': e = (i, j)

    dist1 = bfs(maps, s, 'L')
    if dist1 == -1: 
        return -1

    dist2 = bfs(maps, l, 'E')
    if dist2 == -1:
        return -1

    return dist1 + dist2


'''
	•	맵은 S(시작), L(레버), E(출구), O(빈 칸), X(벽)으로 구성된 2차원 격자입니다.
	•	S → L → E 순서로 이동해야 하며, 상하좌우로 한 칸 이동하면 1초, 벽(X)은 통과 불가.
	•	레버나 출구에 도달할 수 없으면 -1을 반환해야 합니다.



'''