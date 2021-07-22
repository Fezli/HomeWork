my_list = []
print(my_list)
while True:
    i = int(input("Введите число, что бы добавить его в рейтинг: "))
    my_list.append(i)
    my_list.sort()
    my_list.reverse()
    print(my_list)