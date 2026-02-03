print("Welcome to airport data!")
airport={}


while True:
    user_input = int(input("What do you want to do? \n 1 to enter a new airport "
                       "\n 2 to fetch the information of existing airport \n 3 to quit"
                       "\nChoose number: "))
    print(f"You choose option {user_input}")
    if user_input == 1:
        code=input("Enter ICAO code: ")
        name=input("Enter name airport: ")
        airport[code]=name
    elif user_input == 2:
        code = input("Enter ICAO code: ")
        if code in airport:
                print(f"The name of {code} is {airport[code]}")
        else:
            print("ICAO not found")

    elif user_input == 3:
        print("Program ended")
        break
    else:
        print("Invalid option")
print(f"Airport data consist of: {airport}")




