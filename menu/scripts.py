import time
def start():
    print("1 - ....\n 2 - .... \n 3 - ....\n")
    choiсe_handler(input())

def choiсe_handler(choice):
    if choice == "1":
        pass
    elif choice == "2":
        pass
    elif choice == "3":
        pass
    elif choice == "4":
        exit_program()
    else:
        print("Error input, choose number from 1 to 4\n")

def exit_program():
    print("Closing ", end="")
    time.sleep(0.25)
    print(". ", end="")
    time.sleep(0.25)
    print(". ", end="")
    time.sleep(0.25)
    print(". ", end="")
    exit()