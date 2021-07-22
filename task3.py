my_dict = {0 : "зима", 1 : "весна", 2 : "лето", 3 : "осень"}
my_list = ("зима", "весна", "лето", "осень")

i = int(input("Введите номер месяца: "))

if i == 12 or 1 or 2:
    print(my_dict[0])
    print(my_list[0])
elif i == 3 or 3 or 5:
    print(my_dict[1])
    print(my_list[1])
elif i == 6 or 7 or 8:
    print(my_dict[2])
    print(my_list[2])
elif i == 9 or 10 or 11:
    print(my_dict[3])
    print(my_list[3])
else:
    print("Такого месяца нет")
