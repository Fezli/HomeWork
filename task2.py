my_list = []
el = None
i = 0

while (el != "-"):
    el = input("Напишите что вы хотите добавить в список: ") #eсли хотите перестать добавлять элементы, напишите "-"
    if el == "-":
        break
    my_list.append(el)
    print(my_list)

if len(my_list) % 2 == 0:
    while i < len(my_list):
        my_list[i], my_list[i+1] = my_list[i+1], my_list[i]
        i += 2
else:
    copy1 = my_list[-1] #занесение последнего элемента в переменную
    my_list.remove(copy1) #удаление последнего элемента
    while i < len(my_list):
        my_list[i], my_list[i+1] = my_list[i+1], my_list[i]
        i += 2
    my_list.append(copy1) #востановление последнего элемента
print(my_list)