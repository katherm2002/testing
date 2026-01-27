user_number=int(input("Enter a number: "))
if user_number <=1:
    print(f"{user_number} is not a prime number")
else:
    divisor = 2
    is_prime = True
    while divisor<user_number:
        if user_number%divisor==0:
            is_prime=False
            break
        divisor+=1

    if is_prime:
        print(f"{user_number} is a prime number")
    else:
        print(f"{user_number} is not a prime number")



