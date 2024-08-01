import sys
import random


def play_gn(name='PlayerOne'):
    game_count=0
    player_wins=0

    def gn():
        nonlocal name
        nonlocal player_wins

        yo_elijo=input(f'\n{name}, dime el número en el que estoy pensando entre 1, 2 y 3 \n\n')
        yo=int(yo_elijo)

        if yo_elijo not in ['1','2','3']:
            print(f'\n{name}, porfavor un número que sea 1, 2 o 3\n')
            return gn()
        
        py_elige=random.choice('123')
        py=int(py_elige)

        print(f'\n{name}, elegiste {yo_elijo}.')
        print(f'\npython pensaba en el {py_elige}.\n\n')
        
        def ganador(yo, py):
            nonlocal player_wins
            nonlocal name

            if yo==py:
                player_wins+=1
                return f'🎉¡{name} lo has adivinado!🎉'
            else:
                return f'😢Lo siento {name}, no lo has adivinado.😢\n'

        game_result=ganador(yo,py)
        print(game_result)

        nonlocal game_count
        game_count+=1
        print(f'\nVeces jugadas {game_count}.\n')
        print(f'{name}, has ganado {player_wins} vez/veces.\n')
        print(f'Tu porcentaje de victorias es: {player_wins/game_count*100:.2f}%\n') #another way would be : {player_wins/game count:.2%}


        print(f'\n{name}, quieres jugar otra vez?\n' )

        while True:
            jugar_mas=input('Si quieres jugar otra vez escribe \'Y\'.\nSi no, escribe \'Q\'.\n\n')
            if jugar_mas.lower() not in ['y','q']:
                continue
            else:
                break

        if jugar_mas =='y':
            return gn()
        else:
            print('\n🎉🎉🎉🎉')
            print(f'\nGracias por jugar!')
            if __name__=='__main__':
                sys.exit(f'Adios {name}!👋')
            else:
                return 

    return gn()

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

    Guess_num=play_gn(args.name)
    Guess_num()