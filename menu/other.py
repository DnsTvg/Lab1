import os
import logging


def read_file(filename):
    """
    Читає вміст файлу і повертає його текст.
    """
    current_dir = os.path.dirname(__file__)
    file_path = os.path.join(current_dir, filename)

    try:
        with open(file_path, 'r' , encoding='utf-8') as file:
            text = file.read()
            logging.info(f"Файл '{filename}' успішно прочитано")
            return text
    except FileNotFoundError:
        logging.error(f"Файл '{filename}' не знайдено.")
        print(f"Файл '{filename}' не знайдено.")
        return None

def set_filename():
    """
    Встановлює назву файлу.
    """
    try:
        filename = input("Введіть назву файлу: ").split()[0]
        logging.info(f"Вказана назва файлу: {filename}")
        return filename
    except IndexError:
        logging.error("Невірний формат назви файлу")
        print("Невірний формат назви файлу")
        return None

def set_radius():
    """
    Встановлює радіус.
    """
    while True:
        try:
            radius = int(input("Введіть радіус: "))
            logging.info(f"Вказаний радіус: {radius}")
            return radius
        except ValueError:
            logging.error("Помилка введення радіуса")
            print("Помилка значення")

