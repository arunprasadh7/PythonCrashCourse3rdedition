#Copying a List

my_foods = ['pizza', 'falafel', 'carrot cake']
friends_food = my_foods[:]

print('My foods are :')
print(my_foods)

print('\n My friends food are:')
print(friends_food)

my_foods.append('canoli')
friends_food.append('ice cream')

print('Updated my food is:',my_foods)
print('Updated friends foods is:',friends_food)
