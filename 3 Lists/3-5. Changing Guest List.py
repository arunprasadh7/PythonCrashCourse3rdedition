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