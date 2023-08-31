'''
Now that you know how to loop through a dictionary, clean
up the code from Exercise 6-3 (page 99) by replacing your series of print()
calls with a loop that runs through the dictionary’s keys and values. When
you’re sure that your loop works, add five more Python terms to your glossary.
When you run your program again, these new words and meanings should
automatically be included in the output.'''

glossary = {
    'variable':'used to store data of values which can be altered',
    'data':'piece of information',
    'constants':'values that cannot be altered',
    'OOP':'object oriented programming',
    'lists':'collection of variables',
    
}

for term, meaning in glossary.items():
    print(f'\n{term}:\n{meaning}.')