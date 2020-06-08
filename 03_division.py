# -*- coding: utf-8 -*-

# (цикл while)

# даны целые положительные числа a и b (a > b)
# Определить результат целочисленного деления a на b, с помощью цикла while,
# __НЕ__ используя стандартную операцию целочисленного деления (// и %)
# Формат вывода:
#   Целочисленное деление ХХХ на YYY дает ZZZ

a, b = 179, 37
# a, b = 179, 177
# # a, b = 177, 178
# a, b = 179, 0
# a, b = 155, 5


divider = 0
divedend = a
while a - b >= 0:
    if a - b >= 0 and b > 0:
        divider += 1
        a = a - b
    else:
        print('Division by 0 is impossible')
        break
if b > 0:
    print('Integer division of ', divedend, ' by ', b, ' gives ', divider)