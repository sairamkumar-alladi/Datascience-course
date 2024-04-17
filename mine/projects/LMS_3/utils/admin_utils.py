from utils.display_utils import (
    display_admin_menu, 
    display_books_menu
)
from utils.input_utils import (
    take_choice,
    take_book_details
)
from utils.book_utils import (
    add_book,
    get_books
)

def admin_entry():
    flag = True
    while flag:
        display_admin_menu()
        choice = take_choice(4)

        if choice == 1:
            display_books_menu()
            book_choice = take_choice(3)
            if book_choice == 1:
                book_name,book_id = take_book_details()
                add_book(book_name,book_id)
            elif book_choice == 2:
                get_books()
        elif choice == 2:
            print("Teacher section")
        elif choice == 3:
            print("Student Section")
        elif choice == 4:
            flag = False
            print("Your Successfully logged out.")
