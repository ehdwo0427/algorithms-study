'''
BOJ 16236 아기상어

- N x N 크기에 물고기 M마리 아기 상어 1마리
- 상하좌우로 인접한 한 칸씩 이동
- 아기 상어는 자신보다 큰 물고기가 있는 칸은 지나갈 수 없고, 나머지 칸은 모두 지나갈 수 있음
- 더 이상 먹을 수 있는 물고기가 공간에 없으면 엄마 상어에게 도움 요청
- 먹을 수 있는 물고기가 1마리라면, 그 물고기를 먹으러 간다.
- 먹을 수 있는 물고기가 1마리보다 많으면, 거리가 가장 가까운 물고기를 먹으러 간다.
	- 이동 시 최솟값으로 이동
	- 거리가 가까운 물고기가 많으면 가장 위에 있는 물고기, 그러한 물고기가 여러마리면, 가장 왼쪽에 있는 물고기를 먹는다.
- 아기 상어는 자신의 크기와 같은 수의 물고기를 먹을 때 마다 크기가 1 증가한다.(크기가 2인 아기 상어는 물고기 2마리를 먹으면 3이 됨)


입력
N
N x N 리스트 입력

0 : 빈칸
1, 2, 3, 4, 5, 6 : 칸에 있는 물고기의 크기
9: 아기 상어의 위치

물고기부터 탐색 : 물고기 크기별로 해서 위치 정보를 정렬한다.
아기 상어 위치 계속해서 트래킹 -> 정렬기준 잘 확인해서 자신보다 작거나 같고 거리가 가까운 물고기를 탐색하여 먹는다.
'''
from collections import deque

time = 0
n = int(input())
board = []
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for _ in range(n):
    board.append(list(map(int, input().split())))
    
for i in range(n):
    for j in range(n):
        # 상어 위치 찾기
        if board[i][j] == 9:
            sx, sy = i, j
            
# 상어 초기 크기
ss = 2
# 상어 위치 초기화
board[sx][sy] = 0

# BFS 탐색
def bfs(sx, sy, ss):
    min_d = 10000
    global board
    
    q = deque()
    q.append((sx, sy, ss, 0))
    candidate = []
    visited = set((sx, sy))
    
    while q:
        x, y, s, d = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            # 범위 내에 있고 방문하지 않은 곳
            if 0 <= nx < n and 0 <= ny < n and (nx, ny) not in visited:
                visited.add((nx, ny))
                if board[nx][ny] <= s:
                    q.append((nx, ny, s, d + 1))
                # 먹을 수 있는 물고기 발견
                if 0 < board[nx][ny] < ss:
                    if min_d >= d + 1:
                        min_d = d + 1 # 최소 거리 갱신
                        candidate.append((nx, ny, s, d + 1))
    if candidate:
        candidate.sort(key=lambda x: (x[0], x[1]))
        return candidate[0]
    else:
        return [-1, -1, -1, -1]

cnt = 0 # 먹은 물고기 수
while True:
    sx, sy, ss, d = bfs(sx, sy, ss)
    if sx == -1:
        break
    cnt += 1
    if cnt == ss:
        ss += 1
        cnt = 0
    time += d
    board[sx][sy] = 0

print(time)