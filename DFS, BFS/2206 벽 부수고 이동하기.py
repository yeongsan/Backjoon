## 2206번: 벽 부수고 이동하기
#https://nearhome.tistory.com/46

from collections import deque
import sys
#input = sys.stdin.readline

N, M = map(int,input().split())

matrix = [list(map(int,input())) for _ in range(N)]



def bfs():
    
    dx, dy = [1,-1,0,0], [0,0,1,-1]
    queue = deque()
    visited = [[ [0]*2 for _ in range(M)] for _ in range(N)]
    visited[0][0][True] = 1
    queue.append([0,0,True])

    while queue:
        x, y, chance = queue.popleft()
        if x==N-1 and y==M-1:
            return visited[x][y][chance]
        

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if (0<=nx<N) and (0<=ny<M):
                if chance and matrix[nx][ny] :
                    visited[nx][ny][False] = visited[x][y][True] + 1
                    queue.append([nx,ny,False])
                elif not matrix[nx][ny] and not visited[nx][ny][chance]:
                    visited[nx][ny][chance] = visited[x][y][chance] + 1
                    queue.append([nx,ny,chance])
    return -1

print(bfs())


        
