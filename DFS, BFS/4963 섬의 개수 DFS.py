## 4963번: 섬의 개수_DFS

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)


dx = [1,-1,0,0,1,-1,1,-1]
dy = [0,0,1,-1,1,1,-1,-1]


def dfs(x,y):
    field[x][y] = 0
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < h and 0 <= ny < w and field[nx][ny] == 1:
            dfs(nx,ny)   


while True:
    w, h = map(int,input().split())
    if w == 0 and h == 0:
        break
    field = []
    count = 0
    for _ in range(h):
        field.append(list(map(int,input().split())))
    for i in range(h):
        for j in range(w):
            if field[i][j]== 1:
                dfs(i,j)
                count += 1
    print(count)
