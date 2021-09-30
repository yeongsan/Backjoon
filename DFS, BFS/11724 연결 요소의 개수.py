## 11724번: 연결 요소의 개수
import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

N, M = map(int,input().split())
graph = [ [] for _ in range(N+1)]
visited = [0] * (N+1)

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

def dfs(start, visited):
    visited[start] = 1
    for i in graph[start]:
        if visited[i] == 0:
            dfs(i, visited)

count = 0

for i in range(1,N+1):
    if visited[i] == 0:
        count += 1
        dfs(i,visited)

print(count)
    
