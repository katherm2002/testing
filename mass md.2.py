talents = input("Enter your talents: ")
pounds = input("Enter your pounds: ")
lots = input("Enter your lots: ")

total_lots = talents * 20 * 32 + pounds * 32 + lots
total_grams =total_lots * 13.3
total_kilograms =int(total_grams //  1000)
grams=total_grams % 1000

print("The weight in modern units:")
print(kilograms, "kilograms and", grams, "grams.")