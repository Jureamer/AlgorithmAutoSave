import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int,input().split())

big_arr = [[] for _ in range(N+1)]  # index보다 큰 수
small_arr = [[] for _ in range(N+1)]  # index보다 작은 수
mid = (N+1)/2 #개수 기준 중간값

for i in range(M):  #값 입력후 배열
    a,b=map(int,input().split())
    big_arr[b].append(a)
    small_arr[a].append(b)

def bfs(arr, start):
    cnt = 0
    visited[start] = True
    stack = deque()
    stack.append(start)
    
    while stack:
        x = stack.popleft()
        
        for i in arr[x]:
            if not visited[i]:
                cnt += 1
                visited[i] = True
                stack.append(i)
    return cnt
    
answer = 0
for i in range(1,N+1):
    visited=[False] * (N+1)
    if bfs(big_arr,i) >= mid:
        answer += 1
    if bfs(small_arr,i) >= mid:
        answer += 1
print(answer)