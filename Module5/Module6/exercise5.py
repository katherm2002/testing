def numbers(lst):
    even_numbers=[]
    for i in lst:
        if i % 2==0:
           even_numbers.append(i)
    return even_numbers
number=[1,2,3,4,5,6,7,8,9,10,12,13]
result=numbers(number)
print(f"The original list is {number}")
print(f"The cut-down list is {result}")
