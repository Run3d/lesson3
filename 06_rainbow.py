# -*- coding: utf-8 -*-

# (цикл for)

import simple_draw as sd

rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)


# Нарисовать радугу: 7 линий разного цвета толщиной 4 с шагом 5 из точки (50, 50) в точку (350, 450)

# initial_point = sd.get_point(50, 50)
# final_point = sd.get_point(350, 450)
# # list_lines = [initial_point, final_point]
# step = 10
# for line_color in rainbow_colors:
#     sd.line(start_point=initial_point, end_point=final_point, color=line_color, width=8)
#     # sd.lines(point_list=list_lines, color=line_color, closed=True, width=4)
#     initial_point = sd.get_point(50 + step, 50)
#     final_point = sd.get_point(350 + step, 450)
#     step += 10

# sd.line(sd.get_point(0, 50), sd.get_point(400, 450), color=sd.COLOR_ORANGE, width=4)
# sd.line(sd.get_point(5, 50), sd.get_point(405, 450), color=sd.COLOR_YELLOW, width=4)

# Усложненное задание, делать по желанию.
# Нарисовать радугу дугами от окружности (cсм sd.circle) за нижним краем экрана,
# поэкспериментировать с параметрами, что бы было красиво

point = sd.get_point(300, -100)
radius = 300
step_radius = 18
for line_color in rainbow_colors:
    sd.circle(center_position=point, radius=radius, color=line_color, width=16)
    radius += step_radius

sd.pause()