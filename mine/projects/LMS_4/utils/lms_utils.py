from utils.display_utils import (
    display_main_menu, 
    display_admin_menu
 )
from utils.input_utils import take_input_choice
from utils.admin_utils import admin_entry


def lms_entry():
    flag = True
    while flag:
        display_main_menu()
        choice = take_input_choice(4)
        if choice == 1:
            admin_entry()
        elif choice == 2:
            print("Teacher")
        elif choice == 3:
            print("Student")
        elif choice == 4:
            print("Thank you for visiting...:)")
            flag = False