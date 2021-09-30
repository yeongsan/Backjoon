## 2468번: 안전 영역 DFS

from copy import deepcopy
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)


def dfs(x,y):
    d = [ (1,0),(-1,0),(0,1),(0,-1)]
    for dx,dy in d:
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < N and t[nx][ny] > k:
            t[nx][ny] = k
            dfs(nx,ny)

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
                dfs(i,j)
                cnt += 1
    max_cnt = max(max_cnt, cnt)
print(max_cnt)
    

