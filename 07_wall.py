# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw as sd


# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for


initial_horizontal_point = sd.get_point(0, 50)
final_horizontal_point = sd.get_point(600, 50)
initial_vertical_point = sd.get_point(100, 0)
final_vertical_point = sd.get_point(100, 50)
vertical = 0
horizontal = 0
vertical_step = 50
horizontal_step = 100
vertical_offset = 0
horizontal_offset = 50
horizontal_offset_step = 50
vertical_offset_step = 50
while vertical <= 600:
    sd.line(start_point=initial_horizontal_point, end_point=final_horizontal_point, color=sd.COLOR_YELLOW, width=2)
    while horizontal <= 600:
        sd.line(start_point=initial_vertical_point, end_point=final_vertical_point, color=sd.COLOR_YELLOW, width=2)
        initial_vertical_point = sd.get_point(100 + horizontal, 0 + vertical_offset)
        final_vertical_point = sd.get_point(100 + horizontal, 50 + vertical_offset)
        horizontal = horizontal + horizontal_step
    initial_horizontal_point = sd.get_point(0, 50 + vertical)
    final_horizontal_point = sd.get_point(600, 50 + vertical)
    vertical = vertical + vertical_step
    horizontal = - horizontal_offset
    vertical_offset = vertical_offset + vertical_offset_step
    horizontal_offset = horizontal_offset + horizontal_offset_step
    print('horizontal_offset= ', horizontal_offset)
    # while horizontal <= 600:
    #     sd.line(start_point=initial_vertical_point, end_point=final_vertical_point, color=sd.COLOR_YELLOW, width=2)
    #     initial_vertical_point = sd.get_point(100 + horizontal, 0)
    #     final_vertical_point = sd.get_point(100 + horizontal, 50)
    #     horizontal = horizontal + horizontal_step



sd.pause()