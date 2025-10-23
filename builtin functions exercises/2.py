string = str(input())
i = 0
upper = 0
lower = 0
while i < len(string):
    if string[i].isupper():
        upper = upper + 1
    elif string[i].islower():
        lower = lower + 1
    i = i + 1
print( "Upper case:", upper)
print("Lower case:", lower)