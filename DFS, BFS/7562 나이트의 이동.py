## 7562: 나이트의 이동

from collections import deque
import sys

input= sys.stdin.readline

dx = (2, 1, -1, -2, -2, -1, 1, 2)
dy = (1, 2, 2, 1, -1, -2, -2, -1)


def bfs():
    q = deque()
    q.append((sx, sy))
    while q:
        x, y = q.popleft()
        if x == ex and y == ey:
            print(d[x][y])
            return
        for i in range(8):
            nx, ny = x+dx[i] , y+dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if not d[nx][ny]:
                d[nx][ny] = d[x][y] + 1
                q.append((nx, ny))
        





N = int(input())

for i in range(N):
    n = int(input())
    sx, sy = map(int, input().split())
    ex, ey = map(int, input().split())
    d = [[0]*n for _ in range(n)]
    bfs()
