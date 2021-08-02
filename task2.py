int_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
my_list = []
x = 0
def sort_list():
    for i in range(1, len(int_list)):
        if int_list[i] > int_list[i-1]:
            my_list.append(int_list[i])
    yield(my_list)
sort_ls = sort_list()
print(next(sort_ls))