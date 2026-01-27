numbers=[]
user_number=(input("Enter a number (empty to quit): "))
while user_number!='':
    number = int(user_number)
    numbers.append(int(user_number))
    user_number = (input("Enter a number (empty to quit): "))

numbers.sort(reverse=True)
top_five= numbers[:5]

for n in top_five:
    print(n)