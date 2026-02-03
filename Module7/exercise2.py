names= set()
user_input=input("Enter names 'empty to quit': ")
while user_input != '':
    if user_input in names:
        print("Existing name")
    else:
        print("New name")
        names.add(user_input)
    user_input = input("Enter names 'empty to quit': ")
for name in names:
    print(name)