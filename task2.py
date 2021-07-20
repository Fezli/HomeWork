second = int(input("Введите кол-во секунд:"))
hour = second // 3600
minutes = (second % 3600) // 60
second_1 = second - (minutes * 60 + hour * 3600)

print(f"{second} секунд - это {hour}:{minutes}:{second_1}")