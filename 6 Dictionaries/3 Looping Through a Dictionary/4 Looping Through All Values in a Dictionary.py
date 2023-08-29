# Looping Through All Values in a Dictionary values()

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}

print('The languages are:')
for language in favorite_languages.values():
    print(language.title())

# to get without any duplicate values, we can use a set

print('Languages without duplicates:')
for lang in set(favorite_languages.values()):
    print(lang.title())
