text_file = open("text2.txt", "r")
amount_str = text_file.readlines()
print(f"Количество строк в файле: {len(amount_str)}")
for i in range(len(amount_str)):
    print(f"В {i+1} строчке: {len(amount_str[i].split())}")
text_file.close()