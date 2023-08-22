#A string is a series of characters. 
#Anything inside quotes is considered a string in Python

name = 'arun prasadh'

print(name.title())
print(name.upper())
print(name.lower())

first_name = 'arun'
last_name = "prasadh"
full_name = f'{first_name} {last_name}'
print('Full name is',full_name)
print(f'Hello, {full_name.title()}')

# \t -adding whitespace to strings with tabs or newlines
print('Python')
print('\tPython')

#\n - newline
print("languages:\nPython\nC\nJava")

#combining tab and new lines
print("languages:\n\tPython\n\tC\n\tJava")

#Stripping whitespaces rstrip() lstrip() strip()
name = 'Arun   '
print(name.rstrip())
name2 = '    Arun'
print(name2.lstrip())
name3 = '       Arun         '
print(name3.strip())

#Removing Prefixes
google = "https://google.com"
print(google.removeprefix('https://'))