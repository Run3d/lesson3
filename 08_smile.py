# -*- coding: utf-8 -*-

# (определение функций)
import simple_draw as sd

# Написать функцию отрисовки смайлика в произвольной точке экрана
# Форма рожицы-смайлика на ваше усмотрение
# Параметры функции: кордината X, координата Y, цвет.
# Вывести 10 смайликов в произвольных точках экрана.


def smile(x, y, color):
    mouth_point_list = [sd.get_point(x-25, y), sd.get_point(x-7, y-15), sd.get_point(x+7, y-15), sd.get_point(x+25, y)]
    left_bottom_point = sd.get_point(x-35, y-30)
    right_top_point = sd.get_point(x+35, y+30)
    sd.ellipse(left_bottom=left_bottom_point, right_top=right_top_point, color=color, width=2)
    sd.lines(point_list=mouth_point_list, color=sd.COLOR_ORANGE, closed=False, width=2)
    left_eye_point =sd.get_point(x-15, y+5)
    right_eye_point= sd.get_point(x+15,y+5)
    sd.circle(center_position=left_eye_point, radius=3, color=sd.COLOR_YELLOW,width=0)
    sd.circle(center_position=right_eye_point, radius=3, color=sd.COLOR_YELLOW, width=0)



# smile(300, 300, sd.COLOR_ORANGE)
for _ in range(10):
    smile(sd.random_number(30, 570),sd.random_number(25, 575), sd.COLOR_GREEN)


sd.pause()