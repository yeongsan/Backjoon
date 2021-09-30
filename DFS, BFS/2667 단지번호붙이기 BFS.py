## 2667번: 단지번호 붙이기 BFS
# https://kangmin1012.tistory.com/30

import sys
from _collections import deque

def BFS(map, visit, i, j, N):
    post_que = deque([])
    directions = ((1,0) , (-1,0), (0,1), (0,-1)) # 상, 하, 좌, 우
    post_que.append([i,j])
    count = 0

    while post_que:
        info = post_que.popleft() #[x,y]
        # 방문했음을 표시
        if visit[info[0]][info[1]] == 0:
            visit[info[0]][info[1]] = 1
            count += 1
        else:
            continue

        for x,y in directions:
            dir_x = info[0] + x
            dir_y = info[1] + y
            if 0 <= dir_x <= N-1 and 0 <= dir_y <= N-1:
                if visit[dir_x][dir_y] == 0 and map[dir_x][dir_y] == 1:
                    post_que.append([dir_x,dir_y])
    return count


N = int(input())
post_list = []
map = []
visit = [[0] * N for _ in range(N)]
# 지도 만들기
for _ in range(N):
    a = input()
    li = []
    for i in a:
        li.append(int(i))
    map.append(li)

for i in range(N):
    for j in range(N):
        if map[i][j] == 1 and visit[i][j]==0:
            post_list.append(BFS(map,visit,i,j,N))

post_list.sort()


print(len(post_list))
for post in post_list :
    print(post)


















    
