import math
# 1 задание
stotona = int(input())
print(f"Периметр: {4 * stotona} \nПлощадь: {stotona ** 2} \nДиагональ: {stotona * math.sqrt(2)}")

# 2 задание
a2, b2, c2 = map(int,input().split())
diskriminant = b2 ** 2 - 4 * a2 * c2
koren1 = (-b2 + math.sqrt(diskriminant)) / 2 * a2
koren2 = (-b2 - math.sqrt(diskriminant)) / 2 * a2

print(f"{koren1} \n{koren2}")

# 3 задание
first_string = input()
second_string = input()

print(f"{first_string.replace(first_string[0:2], second_string[0:2])}, {second_string.replace(second_string[0:2], first_string[0:2])}")

# 4 задание
way = r"C:\Users\kv.zhenihov\Downloads\Пикчи"
print(f"Название файла: {way[-5:]} \nНазвания диска: {way[0]} \nКорневая папка: {way[3:7]}")

# 5 задание
a5, b5 = map(int,input().split())
print(f"a + b = {a5 + b5} \na*b = {a5 * b5}")

# 6 задание
delit_string = ' ' + input()
delit_string_upgrade = delit_string[::2]
print(delit_string_upgrade[1:])

# 7 задание
tree_letters = input()
many_letters = input()
first_position = many_letters.find(tree_letters[0])
second_position = many_letters.find(tree_letters[1])
third_position = many_letters.find(tree_letters[2])
numbers_position = first_position, second_position, third_position
print(many_letters[min(numbers_position):max(numbers_position) + 1])