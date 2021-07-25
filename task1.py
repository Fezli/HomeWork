def my_func(x, y):
    if y <= 0:
        return
    return x / y

x = int(input("Первое число"))
y = int(input("Второе число"))
print(my_func(x, y))