"""
Make a list that includes at least three people you’d like to
invite to dinner. Then use your list to print a message to each person, inviting
them to dinner.
"""

people = ['Ironman','Hulk','Thor']
message = 'I would like to invite you to dinner.'

print(f'Hello {people[0]}, {message}')
print(f'Hello {people[1]}, {message}')
print(f'Hello {people[2]}, {message}')

print('--------------------------------------------------------')
"""
You just heard that one of your guests can’t make the
dinner, so you need to send out a new set of invitations. You’ll have to think of
someone else to invite.
• Start with your program from Exercise 3-4. Add a print() call at the end of
your program, stating the name of the guest who can’t make it.
• Modify your list, replacing the name of the guest who can’t make it with the
name of the new person you are inviting.
• Print a second set of invitation messages, one for each person who is still in
your list.
"""
people = ['Ironman','Hulk','Thor']

print(f'Sorry!! {people[1]} cannot make it to the dinner.')
people.remove('Hulk')
print(people)

people.append('Captain America')
message = 'You are invited to the dinner.'
print(f'Hello {people[0]},{message}')
print(f'Hello {people[1]},{message}')
print(f'Hello {people[2]},{message}')
print(people)
print('--------------------------------------------------------')
"""
3-6. More Guests: You just found a bigger dinner table, so now more space is
available. Think of three more guests to invite to dinner.
• Start with your program from Exercise 3-4 or 3-5. Add a print() call to the
end of your program, informing people that you found a bigger table.
• Use insert() to add one new guest to the beginning of your list.
• Use insert() to add one new guest to the middle of your list.
• Use append() to add one new guest to the end of your list.
• Print a new set of invitation messages, one for each person in your list.
"""

print('Good news fellas, we have found a bigger table for our dinner party.')
people.insert(0,'Spiderman')
people.insert(2,'Superman')
people.insert(-1,'Batman')
message = 'You are invited to the dinner.'
print(f'Hello {people[0]},{message}')
print(f'Hello {people[1]},{message}')
print(f'Hello {people[2]},{message}')
print(f'Hello {people[3]},{message}')
print(f'Hello {people[4]},{message}')
print(f'Hello {people[5]},{message}')

print('--------------------------------------------------------')

"""
3-7. Shrinking Guest List: You just found out that your new dinner table won’t
arrive in time for the dinner, and now you have space for only two guests.
• Start with your program from Exercise 3-6. Add a new line that prints a
message saying that you can invite only two people for dinner.
• Use pop() to remove guests from your list one at a time until only two
names remain in your list. Each time you pop a name from your list, print a
message to that person letting them know you’re sorry you can’t invite them
to dinner.
• Print a message to each of the two people still on your list, letting them
know they’re still invited.
• Use del to remove the last two names from your list, so you have an empty
list. Print your list to make sure you actually have an empty list at the end of
your program."""

print(people)
print('We can only invite 2 people for dinner.')
sry_msg = '.Sorry, we cant invite you to dinner.'

p1 = people.pop()
print(f'{p1} {sry_msg}')
p2 = people.pop()
print(f'{p2} {sry_msg}')
p3 = people.pop()
print(f'{p3} {sry_msg}')
p4 = people.pop()
print(f'{p4} {sry_msg}')

print(f'Hello {people[0]}. You\'re invited to dinner.')
print(f'Hello {people[1]}. You\'re invited to dinner.')

del people[0]
del people[0]
print(people)