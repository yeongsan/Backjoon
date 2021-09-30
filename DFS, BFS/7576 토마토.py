## 7576번: 토마토
# https://jae04099.tistory.com/entry/%EB%B0%B1%EC%A4%80-7576-%ED%86%A0%EB%A7%88%ED%86%A0-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%ED%95%B4%EC%84%A4%ED%8F%AC%ED%95%A8?category=890007

from collections import deque  # pop(0)이 시간복잡도가 O(n)이고 popleft()가 O(1)

m , n = map(int,input().split())
# 토마토 받아서 넣기.
matrix = [list(map(int,input().split())) for _ in range(n)]

queue = deque([])

dx, dy = [-1,1,0,0], [0,0,-1,1]
res = 0 # 정답이 담길 변수

for i in range(n):
    for j in range(m):
        if matrix[i][j]==1:
            queue.append([i,j])


def bfs():
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = dx[i] + x , dy[i] + y
            if 0<=nx<n and 0<=ny<m and matrix[nx][ny]==0:
                matrix[nx][ny] = matrix[x][y] + 1
                queue.append([nx, ny])

bfs()

for i in matrix:
    for j in i:
        # 다 찾아봤는데 토마토를 익히지 못했다면 -1 출력
        if j ==0:
            print(-1)
            exit()
    # 다 익혔다면 최댓값이 정답
    res = max(res, max(i))
# 처음 시작을 1로 표현했으니 1 빼줌
print(res-1)
