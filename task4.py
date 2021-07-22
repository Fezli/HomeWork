string_ = input("Введите желаемую строку: ")
my_list = (string_.split(" "))
i = 0
n = 1

while i < len(my_list):
     if len(my_list[i]) > 10:
          print(f"{n}-ое слово:{my_list[i][:10:]}")
          i += 1
          n += 1
     else:
          print(f"{n}-ое слово: {my_list[i]}")
          i += 1
          n += 1