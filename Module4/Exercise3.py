smallest= None
largest= None

while True:
    user_input= input("Enter a number (empty to quit): ")

    if user_input == "":
        break
    number=float(user_input)
    if smallest is None or number < smallest:
        smallest= number
    if largest is None or number > largest:
        largest= number
print("smallest is ",smallest)
print("largest is ",largest)
