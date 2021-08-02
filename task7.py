from math import factorial

el = int(input("До какого числа генерировать факториал: "))

def fact():
    for i in range(1, el+1):
        yield factorial(i)
for el in fact():
    print(el)