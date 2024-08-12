from random import choice

capital='Murcia'

pajaro='Aguila real'

flor='rosa'

cancion='si no es contigo amor'


def randomfunfact():
    funfacts=['Murcia es la 7º ciudad de España.','Murcia tiene medio millón de habitantes en la capital.','Murcia tiene un record.','Murcia tiene su propio dialecto.']

    index=choice('0123')

    print(funfacts[int(index)])

if __name__ == '__main__': 
    randomfunfact()