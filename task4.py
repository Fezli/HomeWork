x = int(input("Введите целое положительное число:"))
i = 0

while (x>0):
    if (x % 10 > i):
        i = x % 10
    x = x // 10

print(i)