import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    print(1 if n&(-n) == n else 0)