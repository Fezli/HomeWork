my_goods = []
i = 1 # номер товара
n = 0 # счетчик циклов
copy_analis_goods = {}

while True:
    answer = input("Вы хотите добавить товар?").lower()
    if answer == "да":
        name = input("Введите название товара: ")
        price = int(input("Введите цену товара: "))
        amount = int(input("Введите кол-во товара: "))
        ed = input("Введите единицы товара товара: ")

        my_dict = {"название": name, "цена": price, "количество": amount, "ед": ed}
        my_tuple = (i, my_dict)
        i += 1
        n += 1
        my_goods.append(my_tuple)
        print(my_goods)
    elif answer == "нет":
        print(my_goods)
        break
    else:
        print("Ответ не распознан")

name_a_a = []
price_a_a = []
amount_a_a = []
ed_a_a = []
for x in range(n):
    name_a = my_goods[x][1]["название"]
    name_a_a.append(name_a)

    price_a = my_goods[x][1]["цена"]
    price_a_a.append(price_a)

    amount_a = my_goods[x][1]["количество"]
    amount_a_a.append(amount_a)

    ed_a = my_goods[x][1]["ед"]
    ed_a_a.append(ed_a)

my_goods_analis = {'название': name_a_a, 'цена': price_a_a, 'количество': amount_a_a, 'ед': ed_a_a}
print(my_goods_analis)