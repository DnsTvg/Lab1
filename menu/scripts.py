import gcodeGenerator.generate
import menu.other as o
import time


def show():
    print(o.read_file("menu.txt"))
    choice = input("Оберіть пункт меню: ")
    if choice == "1":
        gcodeGenerator.generate.rectangle(o.set_filename())
        show()
    elif choice == "2":
        gcodeGenerator.generate.circle(o.set_filename(), o.set_radius())
        show()
    elif choice == "3":
        gcodeGenerator.generate.cube(o.set_filename())
        show()
    elif choice == "4":
        exit_program()
        return
    else:
        print("Error input, choose number from 1 to 4\n")
        show()

def exit_program():
    print("Closing ", end="")
    time.sleep(0.25)
    print(". ", end="")
    time.sleep(0.25)
    print(". ", end="")
    time.sleep(0.25)
    print(". ", end="")
    return




