input_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
format_list = []
for i in range(len(input_list)):
    if input_list.count(input_list[i]) == 1:
        format_list.append(input_list[i])
    else:
        pass
print(format_list)