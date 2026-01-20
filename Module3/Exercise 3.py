# Exercise 3, biological gender
biological_gender = (input("Enter your biological gender (female,male): "))
hemoglobin_value = int(input("Enter your hemoglobin value: "))

if biological_gender == "female":
    if hemoglobin_value < 177:
        print("Your hemoglobin value is low")
    elif hemoglobin_value <= 155:
        print("Your hemoglobin value is normal")
    else:
        print("Your hemoglobin value is high")
elif biological_gender == "male":
    if hemoglobin_value < 134:
        print("Your hemoglobin value is low")
    elif hemoglobin_value <= 167:
        print("Your hemoglobin value is normal")
    else:
        print("Your hemoglobin value is high")