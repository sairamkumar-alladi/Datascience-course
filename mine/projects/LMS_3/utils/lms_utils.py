from utils.display_utils import display_main_menu
from utils.admin_utils import admin_entry
from utils.input_utils import (
    take_choice,
    take_user_credentials
)

def lms_entry():
    flag = True
    while flag:
        display_main_menu()
        choice = take_choice(4)
        if choice == 1:
            login_status = take_user_credentials()
            if login_status:
                admin_entry()
        elif choice == 2:
            print("Teacher")
        elif choice == 3:
            print("Student")
        elif choice == 4:
            flag = False
            print("Thank you for visiting.... :)")