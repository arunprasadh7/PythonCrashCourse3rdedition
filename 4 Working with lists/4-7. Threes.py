"""
Threes: Make a list of the multiples of 3, from 3 to 30. Use a for loop to
print the numbers in your list."""

threes = []

for num in range(3,31):
    if num%3==0:
        threes.append(num)

print(threes)