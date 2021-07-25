def my_func(a, b, c):
    x = [a, b, c]
    x.sort()
    return x[-1] + x[-2]
print(my_func(10, 21, 19))