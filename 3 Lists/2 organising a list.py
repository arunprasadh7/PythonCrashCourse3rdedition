#Organizing a List

#Sorting a List Permanently with the sort() Method
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print('sorted list :',cars)
#sort in reverse order
cars.sort(reverse=True)
print('reverse sorted list:',cars)
print()

#Sorting a List Temporarily with the sorted() Function

cars = ['bmw', 'audi', 'toyota', 'subaru']
print('original list',cars)
print('sorted list',sorted(cars))
print()

#Printing a List in Reverse Order -reverse() 
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.reverse()
print(cars)
print()

#Finding the Length of a List len()
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(len(cars))