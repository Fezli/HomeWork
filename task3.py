oklad_info = open("text3.txt", "r", encoding="utf-8")
oklad_info_list = oklad_info.readlines()
sred_oklad = 0

for i in range(len(oklad_info_list)):
    if int(oklad_info_list[i].split()[1]) < 20000:
        print(f"Оклад меньше 20 тыс. у: {oklad_info_list[i].split()[0]}")
    sred_oklad = sred_oklad + int(oklad_info_list[i].split()[1])
print(sred_oklad // len(oklad_info_list))


oklad_info.close()