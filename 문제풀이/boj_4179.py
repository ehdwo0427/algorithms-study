from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def search_exit(r, c, grid, visited):
    queue = deque()
    start = None
    fire = []
    visited_fire = [[False] * c for _ in range(r)]
    # 지훈이랑 불 위치 찾기.
    for i in range(r):
        for j in range(c):
            # 사용자와 불 찾기.
            if grid[i][j] == 'J':
                start = (i, j, 'J')
                visited[i][j] = True
                grid[i][j] = '0'
            elif grid[i][j] == 'F':
                fire.append((i, j))
                visited_fire[i][j] = True
    if start is None:
        print("IMPOSSIBLE")
        return
    queue.append(start)
    for fx, fy in fire:
        queue.append((fx, fy, 'F'))
    
    while queue:
        
        x, y, t = queue.popleft()
        # 지훈이 일 경우
        if t == 'J':
            if grid[x][y] == 'F':
                continue
            for d in range(4):
                nx, ny = x + dx[d], y + dy[d]
                if 0 > nx or nx >= r or 0 > ny or ny >= c:
                    print(int(grid[x][y]) + 1)
                    return
                elif grid[nx][ny] == '.' and not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append((nx, ny, 'J'))
                    grid[nx][ny] = str(int(grid[x][y]) + 1)
        elif t == 'F':
            for d in range(4):
                nx, ny = x + dx[d], y + dy[d]
                if 0 <= nx < r and 0 <= ny < c and grid[nx][ny] != '#' and grid[nx][ny] != 'F' and not visited_fire[nx][ny]:
                    grid[nx][ny] = 'F'
                    queue.append((nx, ny, 'F'))
                    visited_fire[nx][ny] = True
    print("IMPOSSIBLE")
    return


if __name__ == "__main__":
    r, c = map(int, input().split())
    grid = [list(input().strip()) for _ in range(r)]
    visited = [[False] * c for _ in range(r)]
    search_exit(r, c, grid,  visited)