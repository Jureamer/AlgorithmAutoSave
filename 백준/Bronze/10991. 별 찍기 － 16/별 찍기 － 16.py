repeat = int(input())
for i in range(1, repeat + 1):
    print(" " * (repeat - i), end="")
    print(("* " * i).rstrip())