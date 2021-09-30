## 2468번: 안전 영역 BFS

from copy import deepcopy
from collections import deque
import sys
input = sys.stdin.readline


def bfs(x,y):
    q = deque()
    d = [ (1,0),(-1,0),(0,1),(0,-1)]
    q.append([x,y])
    while q:
        x, y = q.popleft()
        for dx,dy in d:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N and t[nx][ny] > k:
                t[nx][ny] = k
                q.append([nx,ny])

N = int(input())
matrix = [ list(map(int,input().split())) for _ in range(N)]
max_cnt = 1

for k in range(1, max(map(max,matrix))+1 ):  # copy 해야하는 이유?
    t = deepcopy(matrix)
    cnt = 0
    for i in range(N):
        for j in range(N):
            if t[i][j] > k:
                t[i][j] = k
                bfs(i,j)
                cnt += 1
    max_cnt = max(max_cnt, cnt)
print(max_cnt)
    


