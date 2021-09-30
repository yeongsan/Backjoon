## 2606: 바이러스

import sys
input = sys.stdin.readline


n = int(input())
m = int(input())

graph = [[False] * (n+1) for _ in range(n+1)]
visited = [False] * (n+1)

for _ in range(m):
    x, y = map(int, input().split())
    graph[x][y] = graph[y][x] = 1
    
    



result= []
def dfs(v):
    visited[v] = 1
    for i in range(1, n+1):
        if (visited[i] == 0 and graph[v][i] == 1):
            result.append(i)
            dfs(i)
    return len(result)

print(dfs(1))
