from config import lms


def take_input_choice(input_no:int) -> int:
    flag = True
    choice = None
    while flag:
        try:
            choice = int(input('Select choice:'))
            if choice <= input_no:
                flag = False
            else:
                print(f"Please enter numbers upto {input_no} only")
        except ValueError as ve:
            print("Please Enter Numbers Only")
    return choice

def take_login_details():
    print("Please Enter Credentials Below:")
    flag = True
    while flag:
        username = input("Enter User name:")
        password = input("Enter Password")
        if username in lms['Admin']:
            if lms['Admin'][username] == password:
                print("Your successfully logged in.")
                flag=False 
            else:
                print("Please Enter Correct Password.")

        else:
            print("Please Enter Correct username.")