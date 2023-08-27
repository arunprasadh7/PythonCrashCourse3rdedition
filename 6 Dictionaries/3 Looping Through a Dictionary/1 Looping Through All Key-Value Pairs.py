#Looping Through All Key-Value Pairs

user_0 = {
    'username':'efermi',
    'first':'enrico',
    'last':'fermi',
}

for key,value in user_0.items():
    print(f'\nkey: {key}')
    print(f'value: {value}')

#eg 2

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}

for name , lang in favorite_languages.items():
    print(f'\n{name}\'s favorite language is {lang}')

