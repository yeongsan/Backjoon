## 7569번: 토마토(3차원)

from collections import deque  # pop(0)이 시간복잡도가 O(n)이고 popleft()가 O(1)
import sys

input = sys.stdin.readline

m , n , h= map(int,input().split())
# 토마토 받아서 넣기.
matrix = [[list(map(int,input().split())) for _ in range(n)] for _ in range(h)]

queue = deque([])

dx, dy, dz= [-1,1,0,0,0,0], [0,0,-1,1,0,0] , [0,0,0,0,-1,1]
res = 0 # 정답이 담길 변수

for i in range(h):
    for j in range(n):
        for l in range(m):
            if matrix[i][j][l]==1:
                queue.append((i,j,l))


def bfs():
    while queue:
        z, x, y = queue.popleft()
        for i in range(6):
            nx, ny, nz = dx[i] + x , dy[i] + y, dz[i] + z
            if 0<=nx<n and 0<=ny<m and 0<=nz<h:
                if matrix[nz][nx][ny]==0:
                    matrix[nz][nx][ny] = matrix[z][x][y] + 1
                    queue.append((nz,nx, ny))

bfs()

for i in matrix:
    for j in i:
        for k in j:
            # 다 찾아봤는데 토마토를 익히지 못했다면 -1 출력
            if k ==0:
                print(-1)
                exit(0)
    # 다 익혔다면 최댓값이 정답
        res = max(res, max(j))
# 처음 시작을 1로 표현했으니 1 빼줌
print(res-1)
