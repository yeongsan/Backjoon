## 1012번: 유기농 배추

import sys
from collections import deque

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

T = int(input())
result_list = []

def make_graph(M,N,K):
    graph = [[0] * M for _ in range(N)]
    for _ in range(K):
        x, y = map(int, input().split())
        graph[y][x] = 1
    return graph

def bfs(y,x):

    queue = deque([])
    queue.append([y,x])

    while queue:
        y, x = queue.pop()
        for a in range(4):
            xx = dx[a] + x
            yy = dy[a] + y
            if 0 <= xx < M and 0 <= yy < N:
                if graph[yy][xx] == 1:
                    graph[yy][xx] = 0
                    queue.append([yy, xx])

                    
for _ in range(T):
    result = 0
    M, N, K = map(int, input().split())  # M:가로, N: 세로
    graph = make_graph(M, N, K)
    for i in range(N):   # 세로
        for j in range(M): # 가로
            if graph[i][j] == 1:
                bfs(i,j)
                result += 1
    result_list.append(result)

print(*result_list, sep='\n')





            
