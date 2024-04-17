def take_choice() -> bool:
    choice = None
    flag = True
    while flag:
        try:
            choice = int(input("Please enter user type:"))
            return choice
        except ValueError as ve:
            print("User Please enter numbers 1,2,3,4")

    