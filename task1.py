text_file = open("text1.txt", "w", encoding="utf-8")

while True:
    text = input("Ввевдите то, что хотите ввести в файл: ")
    if text == "":
        break
    else:
        text_file.writelines(text + "\n")

text_file.close()