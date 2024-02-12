import math

import logging

width = 150
height = 100
layer_height = 0.2
print_speed = 180

def rectangle(filename):
    """
    Генерує G-код для друку прямокутника з вказаними розмірами і параметрами.
    """

    logging.debug('Called rectangle')
    filename = filename.replace(".gcode","") + ".gcode"
    # Відкриваємо файл для запису G-коду
    with open(filename, 'w') as f:
        # Заголовок G-коду
        f.write("; Налаштування\n")
        f.write("M107 ; Вимкнути вентилятор\n")
        f.write("G21 ; Встановити одиниці в мм\n")
        f.write("G90 ; Встановити абсолютні координати\n")
        f.write("G92 E0 ; Встановити нульову позицію для екструдера\n")
        f.write("\n")

        # Друк прямокутника
        f.write("; Друк прямокутника\n")
        f.write("G1 Z0 F{:.2f}\n".format(layer_height))  # Піднімання до висоти першого шару
        f.write("G1 X0 Y0 F{:.2f}\n".format(print_speed))  # Переміщення до початкової точки
        f.write("G1 Z{:.2f} F{:.2f}\n".format(layer_height, print_speed))  # Опускання до поверхні
        f.write("G1 X{:.2f} F{:.2f}\n".format(width, print_speed))  # Друк по X
        f.write("G1 Y{:.2f} F{:.2f}\n".format(height, print_speed))  # Друк по Y
        f.write("G1 X0 F{:.2f}\n".format(print_speed))  # Повернення до початку по X
        f.write("G1 Y0 F{:.2f}\n".format(print_speed))  # Повернення до початку по Y
        f.write("G1 Z{:.2f} F{:.2f}\n".format(layer_height * 2, print_speed))  # Піднімання після друку
        f.write("\n")

def cube(filename):
    """
    Генерує G-код для друку куба з вказаним розміром і параметрами.
    """
    filename = filename.replace(".gcode", "") + ".gcode"
    size = 5
    # Відкриваємо файл для запису G-коду
    with open(filename, 'w') as f:
        # Заголовок G-коду
        f.write("; Налаштування\n")
        f.write("M107 ; Вимкнути обдув\n")
        f.write("G21 ; Встановити одиниці в мм\n")
        f.write("G90 ; Встановити абсолютні координати\n")
        f.write("G92 E0 ; Встановити нульову позицію для екструдера\n")
        f.write("\n")

        # Друк куба
        f.write("; Друк куба\n")
        for i in range(4):  # Прохід по 4-х поверхах куба
            z = i * size  # Значення Z-координати для поточного шару
            f.write("G1 Z{:.2f} F{:.2f}\n".format(z, print_speed))  # Піднімання до висоти поточного шару

            # Вершина куба
            f.write("G1 X{:.2f} Y{:.2f} F{:.2f}\n".format(0, 0, print_speed))
            f.write("G1 X{:.2f} Y{:.2f} F{:.2f}\n".format(size, 0, print_speed))
            f.write("G1 X{:.2f} Y{:.2f} F{:.2f}\n".format(size, size, print_speed))
            f.write("G1 X{:.2f} Y{:.2f} F{:.2f}\n".format(0, size, print_speed))
            f.write("G1 X{:.2f} Y{:.2f} F{:.2f}\n".format(0, 0, print_speed))  # Замкнення куба

            f.write("\n")


def circle(filename, radius):
    """
    Генерує G-код для друку кола з вказаним радіусом і параметрами.
    """
    filename = filename.replace(".gcode", "") + ".gcode"
    # Відкриваємо файл для запису G-коду
    with open(filename, 'w') as f:
        # Заголовок G-коду
        f.write("; Налаштування\n")
        f.write("M107 ; Вимкнути обдув\n")
        f.write("G21 ; Встановити одиниці в мм\n")
        f.write("G90 ; Встановити абсолютні координати\n")
        f.write("G92 E0 ; Встановити нульову позицію для екструдера\n")
        f.write("\n")

        # Друк кола
        f.write("; Друк кола\n")
        f.write("G1 Z0 F{:.2f}\n".format(layer_height))  # Піднімання до висоти першого шару
        f.write("G1 X0 Y0 F{:.2f}\n".format(print_speed))  # Переміщення до початкової точки
        f.write("G1 Z{:.2f} F{:.2f}\n".format(layer_height, print_speed))  # Опускання до поверхні

        # Розрахунок точок для навколишнього кола
        num_points = 50  # Кількість точок
        for i in range(num_points + 1):
            angle = 2 * math.pi * i / num_points
            x = radius * math.cos(angle)
            y = radius * math.sin(angle)
            f.write("G1 X{:.2f} Y{:.2f} F{:.2f}\n".format(x, y, print_speed))  # Друк точки кола

        f.write("G1 Z{:.2f} F{:.2f}\n".format(layer_height * 2, print_speed))  # Піднімання після друку
        f.write("\n")

        print("ВСЕ ОК")