#Closure es una función con acceso al scope de su función madre cuando la función madre devuelve el valor.

def funcion_madre(person,coins):
    #coins=3
    #person=input('What\'s ur name?')
    def play_game():
       
        nonlocal coins
        coins-=1

        if coins >1:
            print('\n'+person+' has '+str(coins)+' coins left')
        elif coins==1:
            print('\n'+person+' has '+str(coins)+' coin left')
        else:
            print('\n'+person+' is out of coins!')
    return play_game

#funcion_madre()

tommy=funcion_madre('tommy',4)
jenny=funcion_madre('jenny',6)

tommy()
tommy()
tommy()
jenny()