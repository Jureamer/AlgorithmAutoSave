a , b = map(int, input().split())

rateOfDefence = a - (a * b / 100);

if rateOfDefence >= 100:
    print(0)
else:
    print(1)