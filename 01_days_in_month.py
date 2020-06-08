# -*- coding: utf-8 -*-

# (if/elif/else)

# По номеру месяца вывести кол-во дней в нем (без указания названия месяца, в феврале 28 дней)
# Результат проверки вывести на консоль
# Если номер месяца некорректен - сообщить об этом

# Номер месяца получать от пользователя следующим образом
i = 1
while i == 1:
    user_input = input("Введите, пожалуйста, номер месяца: ")
    month = int(user_input)
    if isinstance(month, int) and 0 < month < 13:
        print('your month number is ', month)
        break
    else:
        month = None
        print('Your input is incorrect')
        continue




# if isinstance(month, int) and 0 < month < 13:
#     print('your month number ', month)
# else:
#     month = None
#     print('Your input is incorrect')

if month == 1:
    days = 31
elif month == 2:
    days = 28
elif month == 3:
    days = 31
elif month == 4:
    days = 30
elif month == 5:
    days = 31
elif month == 6:
    ays = 30
elif month == 7:
    days = 31
elif month == 8:
    days = 31
elif month == 9:
    days = 30
elif month == 10:
    days = 31
elif month == 11:
    days= 30
elif month == 12:
    days = 31
else:
    days = None
    print('Somthing going wrong')
print('Your month number ', month, ' contains ', days, ' days.')

