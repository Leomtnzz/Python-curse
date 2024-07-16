#value=input('introduzca un valor:\n')
#print(value) 
import random
import sys
from enum import Enum

class RPS(Enum):
    ROCK=1
    PAPER=2
    SCISSORS=3

playagain=str(True)

while playagain:

#print(RPS(2))
#print(RPS.ROCK)
#print(RPS[ 'ROCK'])
#print(RPS.ROCK.value)
#sys.exit()

    playerchoice=input('Enter...\n1 for Rock \n2 for Paper \n3 for Scissors \n\n')

    player=int(playerchoice)

    if player <1 or player>3:
        sys.exit('You must enter 1, 2, or 3') #print
        #playerchoice=input('Enter...\n1 for Rock \n2 for Paper \n3 for Scissors \n\n')


    computerchoice= random.choice('123')
    computer=int(computerchoice)

    print('\nYou chose '+ str(RPS(player)).replace('RPS.' ,'' )+'.')
    print('Python chose '+ str(RPS(computer)).replace('RPS.' ,'' )+'.\n')

    if player== 1 and computer == 3:
        print('🎉¡You win!🎉')
    elif player== 2 and computer == 1:
        print('🎉¡You win!🎉')
    elif player== 3 and computer == 2:
        print('🎉¡You win!🎉')
    elif player==computer:
        print('😊Tie game!😊')
    else:
        print('🐍¡Python wins!🐍')
    playagain=input('\n Play again?\n Y for Yes or\n Q to Quit\n\n')
    if playagain.lower()== 'y':
            continue
    else:
        print('\n🎉🎉🎉🎉')
        print('Thanks for playing!\n')
        #playagain=False
        break

sys.exit('Bye! 👋🏻  ')