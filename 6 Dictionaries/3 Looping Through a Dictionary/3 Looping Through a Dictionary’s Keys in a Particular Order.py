#Looping Through a Dictionary’s Keys in a Particular Order

favorite_languages = {
  'jen': 'python',
  'sarah': 'c',
  'edward': 'rust',
  'phil': 'python',
}

for name in sorted(favorite_languages.keys()):
    print(f'Hello {name}. Thanks for taking the poll.') 