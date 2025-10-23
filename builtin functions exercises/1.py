list = list(map(int, input().split()))
x = 1
i = 0
while i < len(list):
    x = x * list[i]
    i = i + 1
print(x)