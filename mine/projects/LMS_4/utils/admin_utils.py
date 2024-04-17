from utils.display_utils import display_admin_menu
from utils.input_utils import (
    take_input_choice, 
    take_login_details
)

def admin_entry():
    take_login_details()
    flag = True
    while flag:
        display_admin_menu()
        choice = take_input_choice(4)
        if choice == 1:
            print('Books section')
           
        elif choice == 2:
            print('Student section')
        elif choice == 3:
             print('Teacher section')
        elif choice == 4:
            print('You are successfully logged out.')
            flag = False
