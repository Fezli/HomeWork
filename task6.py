import itertools
i1 = int(input("Введите число от которого выодить числа: "))
i2 = int(input("Введите число до которого выодить числа: "))
for i in range(i1, i2+1):
    print(i)

my_list =[1, 2, 3, True, "name"]
a = int(input("Ведите сколько хотит вывести элементов цикла: "))
count = 0
for x in itertools.cycle(my_list):
    if count >= a:
        break
    print(x)
    count += 1