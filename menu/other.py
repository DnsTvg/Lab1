import os
def read_file(filename):
    """
       Читає вміст файлу і повертає його текст.
       """
    # Отримуємо шлях до поточного каталогу
    current_dir = os.path.dirname(__file__)
    # Повний шлях до файлу
    file_path = os.path.join(current_dir, filename)

    try:
        with open(file_path, 'r' , encoding='utf-8') as file:
            text = file.read()
            return text
    except FileNotFoundError:
        print(f"Файл '{filename}' не знайдено.")
        return None

def set_filename():

    filename = input("Введіть назву файлу: ").split()

    return filename[0]

def set_radius():

    while True:
        try:
            radius = int(input("Введіть радіус: "))
            return radius
        except ValueError:
            print("Помилка значення")

    return filename[0]