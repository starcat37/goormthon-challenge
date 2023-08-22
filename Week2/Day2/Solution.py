# DFS
dy = (-1, -1, -1, 1, 1, 1, 0, 0)
dx = (-1, 0, 1, -1, 0, 1, -1, 1)

def dfs(y, x):
    for i in range(8):
       ny = y + dy[i]
       nx = x + dx[i]
       if 0 <= ny < N and 0 <= nx < N:
        if not visited[ny][nx] and board[ny][nx] == 1:
            visited[y][x] += 1

# 입력 받기
board = []
N, K = map(int, input().split(" "))
for _ in range(N):
  *row, = map(int, input().split(" "))
  board.append(row)

# 실행
visited = [[0] * N for _ in range(N)]
for i in range(N):
  for j in range(N):
    if not visited[i][j] and board[i][j] == 0:
      dfs(i, j)

# 출력
print(sum(visited, []).count(K))
