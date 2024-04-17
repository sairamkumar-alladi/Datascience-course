from utils.input_utils import take_choice
from utils.display_utils import (
    display_main_menu,
    display_admin_menu
)

def lms_entry():
    flag = True
    while flag:
        display_main_menu()
        choice = take_choice()
        if choice == 1:
            display_admin_menu()
        elif choice == 2:
            print("Teacher")
        elif choice == 3:
            print("Student")
        elif choice == 4:
            flag=False
            print("Thank you for visiting..... :)")
        else:
            print("Wrong input please select 1,2,3,4 only.")
