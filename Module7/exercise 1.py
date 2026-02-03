seasons=("spring", "summer","autumn", "winter")
print("Welcome!")
number_month=int(input(" 1 = January"
                       "\n 2 = February"
                       "\n 3 = March \n 4 = April \n 5 = May \n 6 = June \n 7 = July"
                       "\n 8 = August \n 9 = September \n 10 = October \n 11 = November"
                       "\n 12 = December \nSelect number of the month: "))
print(f"You have selected month {number_month}.")
if number_month == 12 or number_month == 1 or number_month == 2:
    print(f"Season is {seasons[3]}")
elif number_month == 3 or number_month == 4 or number_month == 5:
    print(f"Season is {seasons[0]}")
elif number_month == 6 or number_month == 7 or number_month == 8:
    print(f"Season is {seasons[1]}")
elif number_month == 9 or number_month == 10 or number_month == 11:
    print(f"Season is {seasons[2]}")
else:
    print("Invalid month")