#6-3. Glossary

"""
A Python dictionary can be used to model an actual dictionary.
However, to avoid confusion, let’s call it a glossary.
-Think of five programming words you’ve learned about in the previous
chapters. Use these words as the keys in your glossary, and store their
meanings as values.
-Print each word and its meaning as neatly formatted output. You might
print the word followed by a colon and then its meaning, or print the word
on one line and then print its meaning indented on a second line. Use the
newline character (\n) to insert a blank line between each word-meaning
pair in your output.
"""

glossary = {
    'variable':'used to store data of values which can be altered',
    'data':'piece of information',
    'constants':'values that cannot be altered',
    'OOP':'object oriented programming',
    'lists':'collection of variables',
}

term = "variable"
print(f"{term}:\n{glossary[term]}\n")

term = "data"
print(f"{term}:\n{glossary[term]}\n")

term = "constants"
print(f"{term}:\n{glossary[term]}\n")

term = "OOP"
print(f"{term}:\n{glossary[term]}\n")

term = "lists"
print(f"{term}:\n{glossary[term]}\n")