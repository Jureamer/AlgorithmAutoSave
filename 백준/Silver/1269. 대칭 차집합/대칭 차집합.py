n, m = map(int, input().split())

set1 = set(list(map(int, input().split())))
set2 = set(list(map(int, input().split())))

print(len(set1 - set2) + len(set2 - set1))