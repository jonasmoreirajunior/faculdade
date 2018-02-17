x = int(input())
y = x
while y != 0:
    if x % y == 0:
        print(int(x/y))
    y = y - 1