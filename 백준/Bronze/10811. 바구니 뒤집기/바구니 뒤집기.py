n, m = map(int, input().split())
arr = [i+1 for i in range(n)]

for _ in range(m):
    i, j = map(int, input().split())
    
    arr = arr[:i-1] + arr[i-1:j][::-1] + arr[j:]
    
print(*arr)