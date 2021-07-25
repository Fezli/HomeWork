# вариант решения с "**"
# def my_func(x, y):
#     return x ** y
# print(my_func(x=int(input("Введите положительное число: ")), y=int(input("Введите отрицательное число: "))))


def my_func(x, y): # вариант решения с циклом
    i = 1
    while i < abs(y):
        i += 1
        x = x * x
    return (1 / x)
print(my_func(x=int(input("Введите положительное число: ")), y=int(input("Введите отрицательное число: "))))