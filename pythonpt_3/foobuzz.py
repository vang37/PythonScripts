arr = []
for x in range(1, 101):
    if (x % 21 == 0):
        arr.append("foobuzz")
    elif (x % 7 == 0):
        arr.append("buzz")
    elif (x % 3 == 0):
        arr.append("foo")
    else:
        arr.append(str(x))
print(arr)