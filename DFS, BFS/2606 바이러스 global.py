# 2606 global cnt
from collections import deque
import sys

n = int(input())
m = int(input())

graph = [[0] * (n + 1) for _ in range(n + 1)] 
visited = [0] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b]=graph[b][a]=1 

cnt = 0
def dfs(start):
    global cnt 
    visited[start] = 1
    for i in range(1, n+1):
        if visited[i]==0 and graph[start][i]==1:
            dfs(i)
            cnt += 1 
dfs(1)
print(cnt)
