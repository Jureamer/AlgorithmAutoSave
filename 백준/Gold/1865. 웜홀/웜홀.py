for _ in range(int(input())):
    
    def bf():
        distance = [INF] * (N+1)
        for i in range(N):
            for j in range(1, N+1):
                for k in range(len(roads[j])):
                    next, dist = roads[j][k]
                    # print(f'next: {next}, dist: {dist}, distance: {distance}')
                    if distance[next] > distance[j] + dist:
                        distance[next] = distance[j] + dist
                        
                        if i == N-1:
                            return True
                for k in range(len(wormholes[j])):
                    next, dist = wormholes[j][k]
                    # print(f'next: {next}, dist: {dist}, distance: {distance}')
                    if distance[next] > distance[j] + dist:
                        distance[next] = distance[j] + dist
                        
                        if i == N-1:
                            return True
        return False
    N, M, W = map(int, input().split()) # 지점, 도로, 웜홀
    INF = int(1e9)
    roads = [[] * (N+1) for _ in range(N+1)]
    wormholes = [[] * (N+1) for _ in range(N+1)]
    
    
    
    for _ in range(M): # 도로는 양방향
        s, e, t = map(int, input().split()) # 시작, 도착, 시간

        roads[s].append((e, t))
        roads[e].append((s, t))
        
    for _ in range(W): # 웜홀은 단방향
        s, e, t = map(int, input().split()) # 시작, 도착, 시간
        
        wormholes[s].append((e, -t))
    if bf():
        print('YES')
    else:
        print('NO')