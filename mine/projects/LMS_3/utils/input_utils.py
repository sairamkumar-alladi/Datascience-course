from config import (
    LMS,
    department_mapper,
    year_mapper,
    sem_mapper
    )

from utils.display_utils import (
    display_branches,
    display_years,
    display_sems
)
def take_choice(n:int) -> int:
    flag = True
    while flag:
        choice = None
        try :
            choice = int(input("Select Input:"))
            if choice <= n:
                return choice
            else:
                print(f"Please select numbers upto {n} only.")
        except ValueError as ve:
            print("Please Enter numbes only.")

def take_user_credentials() -> bool:
    user_name = input('Enter user name:')
    password = input('Enter password:')

    for admin in LMS['admin']:
        if user_name == admin['user'] \
        and password == admin['password']:
            print("Loggin Successful!")
            return True 
    return False


def take_dept():
    display_branches()
    dept_choice = take_choice(2) 
    return department_mapper[dept_choice]

def take_year():
    display_years()
    year_choice = take_choice(2) 
    return year_mapper[year_choice]
def take_semister():
    display_sems()
    sem_choice = take_choice(2)
    return sem_mapper[sem_choice]

def take_book_details():
    book_name = input("Book name:")
    book_id = input("Book_id:")
    return book_name,book_id