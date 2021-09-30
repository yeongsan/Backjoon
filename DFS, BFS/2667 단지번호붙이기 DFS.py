## 2667번: 단지번호붙이기 DFS
# https://resilient-923.tistory.com/209

import sys
input = sys.stdin.readline

n = int(input())
data = []
for _ in range(n):
    data.append(list(input()))


dx = [1,-1,0,0]
dy = [0,0,1,-1]

num_list = []

def dfs(x,y):
    global cnt
    cnt += 1
    data[x][y] = '0'
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<n and 0<=ny<n:
            if data[nx][ny] == '1':
                dfs(nx,ny)

for i in range(n):
    for j in range(n):
        if data[i][j] == '1':
            cnt = 0
            dfs(i,j)
            num_list.append(cnt)

num_list.sort()
print(len(num_list))
for i in num_list:
    print(i)
