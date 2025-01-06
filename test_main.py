from field_text_vizial import print_string
from neighbors import neighbors

num = input("Введите число!")
num1 = neighbors(num)
num2 = neighbors(int(num) // 2)
num3 = num1 + num2
print_string(num3)
