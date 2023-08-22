# Tuples in python
"""A tuple looks just like a list, except you use parentheses instead of square
brackets. Once you define a tuple, you can access individual elements by
using each item’s index, just as you would for a list."""

dimensions = (200, 50)
print(dimensions)
print(dimensions[0])
print(dimensions[1])

"""If you want to define a tuple with one element, you
need to include a trailing comma:"""
my_t = (3,)
print(my_t)

print('-----------------------------------')

# Looping Through All Values in a Tuple

dimensions = (100, 200)

for dimension in dimensions:
    print(dimension)
print('---------------------------------')

#Writing Over a Tuple
"""Although you can’t modify a tuple, you can assign a new value to a variable
that represents a tuple."""

dimensions = (200,50)
print('Original dimension:')
for dimension in dimensions:
    print(dimension)

dimensions = (400,100)
print('\nUpdated dimension:')
for dimension in dimensions:
    print(dimension)