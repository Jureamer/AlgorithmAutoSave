import sys
input = sys.stdin.readline

repeat = int(input())
arr = [0] * 10001

for _ in range(repeat):
  arr[int(input())] += 1


for i in range(1, 10001):
  if arr[i] != 0:
    for _ in range(arr[i]):
      print(i)