#Modifying Values in a Dictionary

alien_0 = {'color':'green','points':5}
print(f'Alien color is {alien_0["color"]}')

#modifying color to yellow

alien_0['color'] = 'yellow'
print(f'Now the alien color is {alien_0["color"]}')

#tracking position of the alien

alien_0 = {'x_pos':0,'y_pos':25,'speed':'medium'}
print(f'Original position is {alien_0["x_pos"]}')

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    #this is a fast alien
    x_increment = 3

alien_0['x_pos'] = alien_0['x_pos'] + x_increment

print(f'The new postion of the alien is {alien_0["x_pos"]}')