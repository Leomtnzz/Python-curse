person='Leo'
coins=3

#print('\n'+person+'has'+str(coins)+'coins left')

#mensaje='\n%s has %s coins left.' % (person,coins)
#print (mensaje)


#mensaje='\n{} has {} coins left.'.format(person,coins)
#print (mensaje)


# mensaje='\n{1} has {0} coins left.'.format(coins,person)
# print(mensaje)


# mensaje='\n{person} has {coins} coins left.'.format(coins=coins,person=person)
# print(mensaje)

player={'person':'Dave','coins':3}

# mensaje='\n{person} has {coins} coins left.\n'.format(**player)
# print(mensaje)



#f -String

# mensaje=f'\n{person} has {coins} coins left.\n'
# print(mensaje)

# mensaje=f'\n{person} has {2**2} coins left.\n'
# print(mensaje)

# mensaje=f'\n{person.lower()} has {2**2} coins left.\n'
# print(mensaje)

# mensaje=f'\n{player['person']} has {player['coins']} coins left.\n'
# print(mensaje)


#You can pass formatting options

num=10
#print(f'\n2.25 times {num} is {2.25*num:.2f}')

#Yo
# num=int(input('pon un número\n'))
# print(f'\n2.25 times {num} is {2.25*num:.2f}')


# for num in range(1,11):
#     print(f'2.25 times {num} is {2.25*num:.2f}')


for num in range(1,11):
    print(f'{num} divided by 4.52 is {num/4.52:.2f}')

for num in range(1,11):
    print(f'{num} divided by 4.52 is {num/4.52:.2%}')


#Muy curioso
txt = "The binary version of {0} is {0:b}"
print(txt.format(7))
