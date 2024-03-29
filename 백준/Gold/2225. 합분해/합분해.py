N, K = map(int, input().split())
dp = [[0] * (K + 1) for _ in range(N + 1)]
MOD = 1000000000

for j in range(K+1):
    dp[0][j] = 1
    
for i in range(1, N + 1):
    for j in range(1, K + 1):
        dp[i][j] = (dp[i][j-1] + dp[i-1][j]) % MOD

print(dp[N][K])