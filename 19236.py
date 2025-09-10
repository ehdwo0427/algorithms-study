# -----------------------------------------------------------------------------
# BOJ 19236 청소년 상어 — 문제 요약 및 구현 포인트
# -----------------------------------------------------------------------------
# ■ 문제 요약
# - 4x4 격자. 각 칸: [물고기번호(1~16), 방향(1~8)].
# - 상어는 (0,0)의 물고기를 먹고 시작하며, 먹은 물고기의 '방향'을 이어받는다.
# - 매 턴:
#   1) 물고기 1→16번 순서로 이동:
#      - 현재 방향에서 최대 8번까지 시계방향 회전하며 이동 가능 칸 탐색.
#      - 격자 밖 or 상어 위치면 이동 불가. 가능한 칸이면 그 칸과 "자리 교환".
#   2) 상어 이동:
#      - 자신의 방향으로 1~3칸 직진.
#      - 물고기가 있는 칸으로만 이동 가능. 빈칸은 통과 가능하지만 도착 불가.
# - 상어가 더 이상 먹을 물고기가 없으면 종료.
# - 목표: 상어가 먹은 물고기 번호 합의 최댓값 출력.
#
# ■ 입력 형식
# - 4줄, 각 줄에 8개 정수: (물고기번호, 방향) * 4
# - 방향은 1~8로 주어짐. 내부에선 0~7로 변환.
#
# ■ 핵심 구현 포인트
# - 상태 복제: 상어가 이동해 분기할 때 보드를 deepcopy로 복사해 백트래킹.
# - 물고기 이동은 "자리 바꿈"이며, 이동한 물고기의 방향을 회전 반영.
# - 상어는 도착 칸의 물고기를 먹고 그 물고기의 방향을 상속.
# - DFS 종료 조건: 상어가 갈 수 있는 물고기 칸이 없을 때 현재 합을 반환.
#
# ■ 실수 방지 체크리스트
# - 물고기 찾기: 이미 먹힌 물고기는 건너뛴다(번호 0).
# - 회전: (현재방향 + k) % 8, k=0..7.
# - 상어 위치로 물고기 이동 금지.
# - 상어 이동은 1~3칸 중 "물고기가 있는 칸"으로만 착지.
# - (중요) 방향 인덱스는 0~7, DXY는 ↑↖←↙↓↘→↗ 순서.
#
# ■ 시간 복잡도
# - 상태공간이 작아 깊은 복사 + 완전탐색으로 해결 가능.
# -----------------------------------------------------------------------------


# BOJ 19236 청소년 상어 — 가독성 개선 + 주석
import sys
import copy

input = sys.stdin.readline

# 8방향 (상부터 시계방향)
DXY = [(-1, 0), (-1, -1), (0, -1), (1, -1),
       (1, 0), (1, 1), (0, 1), (-1, 1)]


def read_board() -> list[list[list[int]]]:
    """
    보드 셀 구조: [물고기번호, 방향]
    - 물고기번호: 0이면 빈칸
    - 방향: 0~7 (DXY 인덱스)
    """
    board = [[0] * 4 for _ in range(4)]
    for i in range(4):
        row = list(map(int, input().split()))
        for j in range(4):
            num = row[2 * j]
            d = row[2 * j + 1] - 1  # 입력은 1~8, 내부는 0~7
            board[i][j] = [num, d]
    return board


def find_fish(board: list[list[list[int]]], target: int) -> tuple[int, int]:
    """번호가 target인 물고기의 좌표를 찾는다. 없으면 (-1, -1)."""
    for x in range(4):
        for y in range(4):
            if board[x][y][0] == target:
                return x, y
    return -1, -1


def move_all_fish(board: list[list[list[int]]], sx: int, sy: int) -> None:
    """
    1~16번 물고기를 차례로 이동.
    - 각 물고기는 최대 8번까지 방향을 회전하며 이동 가능 칸을 탐색.
    - 상어가 있는 칸(sx, sy)으로는 이동 불가.
    - 빈칸 또는 다른 물고기와는 '자리 바꿈'.
    """
    for fish in range(1, 17):
        x, y = find_fish(board, fish)
        if x == -1:  # 이미 먹힌 물고기
            continue

        d = board[x][y][1]
        for k in range(8):
            nd = (d + k) % 8
            nx, ny = x + DXY[nd][0], y + DXY[nd][1]

            # 범위를 벗어나거나 상어 위치면 스킵
            if not (0 <= nx < 4 and 0 <= ny < 4):
                continue
            if nx == sx and ny == sy:
                continue

            # 자리 바꿈(빈칸 포함)
            target = board[nx][ny]          # [num, dir]
            board[nx][ny] = [fish, nd]      # 이동하는 물고기의 새 위치/방향
            board[x][y] = target            # 원래 자리는 대상이 차지
            break


def dfs(board: list[list[list[int]]], sx: int, sy: int, score: int) -> int:
    """
    백트래킹(DFS):
    - 현재 칸의 물고기를 먹고(점수 추가, 번호 0으로), 물고기 전부 이동.
    - 상어는 현재 방향으로 1~3칸 전진하며 물고기가 있는 칸만 선택 가능.
    - 더 이상 갈 곳이 없으면 현재 점수를 반환.
    """
    # 1) 현재 칸 물고기 섭취
    fish_num, sdir = board[sx][sy]
    score += fish_num
    # 상어가 선 점은 '빈칸' 처리하되, 칸의 방향은 상어 진행 방향으로 유지
    board[sx][sy] = [0, sdir]

    # 2) 물고기 이동
    move_all_fish(board, sx, sy)

    # 3) 상어 이동 시도
    best = score
    dx, dy = DXY[board[sx][sy][1]]
    for step in range(1, 4):
        nx, ny = sx + dx * step, sy + dy * step
        if not (0 <= nx < 4 and 0 <= ny < 4):
            break
        if board[nx][ny][0] == 0:  # 물고기 없는 칸은 스킵
            continue

        # 분기: 보드 깊은 복사 후 재귀
        next_board = copy.deepcopy(board)
        best = max(best, dfs(next_board, nx, ny, score))

    return best


def main():
    board = read_board()
    # 시작: (0,0)에서 먹고 시작하는 로직이 dfs 내부에 포함되어 있으므로 score=0으로 시작
    print(dfs(board, 0, 0, 0))


if __name__ == "__main__":
    main()
