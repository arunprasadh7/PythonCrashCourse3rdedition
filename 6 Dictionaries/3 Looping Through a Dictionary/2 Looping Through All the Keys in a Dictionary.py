# Looping Through All the Keys in a Dictionary
# keys() method

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}

for name in favorite_languages.keys():
    print(name)

print('-------------------------')
# by default it will loop through the keys so the output will be same even without using .keys()

for name in favorite_languages:
    print(name)

print('---------------------------')

#eg 3
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}
friends = ['sarah','jen']

for name in favorite_languages.keys():
    if name in friends:
        lang =  favorite_languages[name].title()
        print(f'Hi {name}. Looks like you love {lang}.')

if 'erin' not in favorite_languages.keys():
    print(f'Erin, please take the poll!.')

