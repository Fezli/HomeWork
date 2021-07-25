def summ_numbers():
    a = 1
    summ_var = 0
    while a == 1:
        my_list = input("Введите числа через пробел: ").split()
        for i in range(len(my_list)):
            if my_list[i] == "*":
                a = 0
                break
            else:
                summ_var = summ_var + int(my_list[i])
        print(summ_var)
summ_numbers()