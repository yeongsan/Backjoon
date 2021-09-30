## 10026번: 적록색약 DFS

import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

def dfs(x,y):
    d = [(1,0),(-1,0),(0,1),(0,-1)]
    visited[x][y] = True
    for dx,dy in d:
        nx, ny = x+dx, y+dy
        if 0<=nx<N and 0<=ny<N:
            if visited[nx][ny] == False:
                if graph[nx][ny] == graph[x][y]:
                    visited[nx][ny] = True
                    dfs(nx,ny)

                        
N = int(input())
graph = [list(input().rstrip()) for _ in range(N)]
visited = [[False] * N for _ in range(N)]
three_cnt , two_cnt = 0,0



# 정상인 경우

for i in range(N):
    for j in range(N):
        if visited[i][j] == False:
            dfs(i,j)
            three_cnt += 1

# 적록색약 인 경우 ( R을 G로 바꾸어준다)
for i in range(N):
    for j in range(N):
        if graph[i][j] == 'R':
            graph[i][j] = 'G'

visited = [[False] * N for _ in range(N)]

for i in range(N):
    for j in range(N):
        if visited[i][j] == False:
            dfs(i,j)
            two_cnt += 1

print(three_cnt, two_cnt)
