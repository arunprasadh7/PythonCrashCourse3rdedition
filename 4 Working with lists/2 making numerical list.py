#Using the range() Function

for value in range(1, 5):
  print(value)

#Using range() to Make a List of Numbers

num = list(range(1,6))
print(num)

even_numbers = list(range(2,11,2))
print('even numbers:',even_numbers)

squares = []
for value in range(1,6):
  square = value ** 2
  squares.append(square)
print('squares of the numbers:',squares)


squares = []
for value in range(1,11):
  squares.append(value**2)
print(squares)