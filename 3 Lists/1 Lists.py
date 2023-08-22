"""
A list is a collection of items in a particular order.

"""

colors = ['red','green','blue','yellow','black','white']
print(colors)

#accessing elements of list using index
#index starts from 0
print(colors[1])
print(colors[3])
print(colors[-1])
print(colors[2].title())

#Using Individual Values from a List
message = f'My favourite color is {colors[0]}'
print(message)

#Modifying Elements in a List
bikes = ['honda','yamaha','kawasaki','bajaj','tvs']
print(bikes)
bikes[0] = 'ktm'
print(bikes)

#Adding Elements to a List

#append method
bikes.append('keeway')
print(bikes)
cars = []
cars.append('honda')
cars.append('toyota')
cars.append('bmw')
print(cars)

#Inserting Elements into a List
numbers = [1,2,3,4,5]
numbers.insert(0,0)
print(numbers)
numbers.insert(7,6)
print(numbers)

#Removing elements from a list
    #del
colors = ['red','white','pink','orange']
del colors[0]
print(colors)

motorcycles = ['honda', 'yamaha', 'suzuki']
del motorcycles[1]
print(motorcycles)

    #pop() Method
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
pop_mot = motorcycles.pop()
print(pop_mot)
print(f'The last motorcycle I owned was a {pop_mot}.')
pop_mat = motorcycles.pop(0)
print(f'The last motorcycle I owned was a {pop_mat}.')

#Removing an Item by Value
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
motorcycles.remove('ducati')
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
expensive = 'ducati'
motorcycles.remove(expensive)
print(motorcycles)
print(f'\n A {expensive} is too expensive for me.')