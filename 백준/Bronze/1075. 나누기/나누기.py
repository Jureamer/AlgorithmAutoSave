n = int(input())
m = int(input())
n = n // 100 * 100

for i in range(100):    
    if (n + i) % m == 0:
        print(str(i).zfill(2))
        break