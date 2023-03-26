import sys
input = sys.stdin.readline

def findParents(parents, x):
    if parents[x] != x:
        parents[x] = findParents(parents, parents[x])
    return parents[x]

def unionParents(parents, a, b):
    a = findParents(parents, a)
    b = findParents(parents, b)
    if a < b:
        parents[b] = a
    else:
        parents[a] = b

def solution():
    N = int(input())
    M = int(input())
    answer = 0
    parents = [i for i in range(N+1)]
    
    edges = []
    
    for i in range(M):
        s, e, d = map(int, input().split())    
        edges.append((d, s, e))
    
    edges.sort()
    
    # 종료 조건: 모든 노드가 연결되었을 때
    for distance, start, end in edges:
        if findParents(parents, start) == findParents(parents, end):
            continue
        else:
            unionParents(parents, start, end)
            answer += distance
    return answer

print(solution())