#The if-elif-else Chain

'''
For example, consider an amusement park that charges different rates for
different age groups:
•	 Admission for anyone under age 4 is free.
•	 Admission for anyone between the ages of 4 and 18 is $25.
•	 Admission for anyone age 18 or older is $40.
'''

age = 12

if age <= 4:
    print('Your entry fee is $0.')
elif age > 4 and age <=18:
    print('Your entry fee is $25.')
else:
    print('Your entry fee is $40.')

#alternate method

age = 12
if age < 4:
  price = 0
elif age < 18:
  price = 25
else:
  price = 40
print(f"Your admission cost is ${price}.")