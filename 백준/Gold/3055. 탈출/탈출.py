import sys
from collections import deque

input = sys.stdin.readline
r, c = map(int, input().split())
maps = []
direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]
visit = [[0] * c for _ in range(r)]
answer = 0

for i in range(r):
    maps.append(list(input()))
    

q = deque()

for i in range(r):
    for j in range(c):
        if maps[i][j] == '*':
            q.append((i, j, 0, '*'))
            visit[i][j] = 1
            continue
        
        if maps[i][j] == 'S':
            visit[i][j] = 1
            q.append((i, j, 0, 'S'))
            continue
isFind = False

def checkHedgehogCondition(x, y):
    return 0 <= x < r and 0 <= y < c and maps[x][y] != 'X' and maps[x][y] != '*' and visit[x][y] == 0

def checkWaterCondition(x, y):
    return 0 <= x < r and 0 <= y < c and maps[x][y] != 'X' and maps[x][y] != 'D' and visit[x][y] == 0

q = deque(sorted(q, key=lambda x: x[3]))

while q:
    x, y, count, thing = q.popleft()
    
    if thing == 'S':
        for i in range(4):
            dx = direction[i][0] + x
            dy = direction[i][1] + y

            if checkHedgehogCondition(dx, dy):
                if maps[dx][dy] == 'D':
                    answer = count + 1
                    isFind = True
                    break
                
                if maps[dx][dy] == '.':
                    visit[dx][dy] = 1
                    maps[dx][dy] = 'S'
                    maps[x][y] = '.'
                    q.append((dx, dy, count+1, 'S'))
                    
    if thing == '*':
        for i in range(4):
            dx = direction[i][0] + x
            dy = direction[i][1] + y

            if checkWaterCondition(dx, dy):
                if maps[dx][dy] == '.':
                    visit[dx][dy] = 1
                    maps[dx][dy] = '*'
                    q.append((dx, dy, count+1, '*'))

    if isFind:
        break
if answer != 0:
    print(answer)
else:
    print("KAKTUS")