import argparse
import sys
from rps import rps
from Guess_number import play_gn


def play_game(name='PlayerOne'):
    hola=False

    while True:
        if hola==True:
            print(f'\n🤖Hola {name}, bienvenido a mi arcade.🤖\n')

        playerchoice=input('Porfavor, elige un juego:\n\n1 = Piedra, Papel o Tijera \n2 = Adivina mi número\n\nO, presiona \'x\' si quieres salir del arcade\n\n')
        

        if playerchoice not in ['1','2','x']:
                print(f'\n{name}, tiene que ser 1, 2 o x\n')
                return play_game(name)
        
        hola=True   
           
        if playerchoice=='1':
            rock_paper_scissors=rps(name)
            rock_paper_scissors()
        elif playerchoice=='2':
            play_gn(name)          
        else:
            print('\n🤖 See you next time 🤖')
            sys.exit(f'Bye, {name}👋\n') 
            



if __name__=='__main__':
    import argparse

    parser=argparse.ArgumentParser(
        description='Provides a personalized game experience.'
    )

    parser.add_argument(
        '-n','--name',metavar='name',
        required=True, help='The name of the person playing the game.'
    )
    
    args=parser.parse_args() 

    print(f'\n🤖{args.name}, bienvenido a mi arcade🤖')
    play_game(args.name)