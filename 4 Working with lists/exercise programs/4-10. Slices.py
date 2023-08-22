"""
 Slices: Using one of the programs you wrote in this chapter, add several
lines to the end of the program that do the following:
• Print the message The first three items in the list are:. Then use a slice to
print the first three items from that program’s list.
• Print the message Three items from the middle of the list are:. Then use a
slice to print three items from the middle of the list.
• Print the message The last three items in the list are:. Then use a slice to
print the last three items in the list.
"""

l1 = [1, 2, 3, 4, 5, 6,7]

print('First three items of the list are:')
for i in l1[:3]:
    print(i)

print('\n Three items from middle :')
for i in l1[2:5]:
    print(i)

print('\n Last three items are:')
for i in l1[-3:]:
    print(i)
