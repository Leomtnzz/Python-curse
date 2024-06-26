first='Leo'
last='Martínez'

pizza=str('pepperoni')
#print(type(pizza))
#print(type(pizza)==str)
#print(isinstance(pizza, str))



#concatenación

fullname= first+' '+last
#print(fullname)
fullname+= '?'
#print(fullname)



#casting a number to a string

decade=str(1980)
#print(type(decade))
#print(decade)

afirmación='me gusta la música de los ' + decade+'s.'
#print(afirmación)



#varias líneas

multilínea='''
Hola, cómo estás?                               

Pasaba para saludar.
                        Todo bien?

'''
#print(multilínea)



#escapar caracteres especiales.

frase='i\'m back at work!\t hey!\n\n Where\'s this at\\located?'
#print(frase)



#métodos string

#print(first)
#print(first.lower())
#print(first.upper())
#print(first)

#print(multilínea.title())
#print(multilínea.replace('bien', 'ok'))
#print(multilínea)

#print(len(multilínea))
multilínea+= '                                        '
multilínea='               '+multilínea
#print(len(multilínea))

#print(len(multilínea.strip()))
#print(len(multilínea.lstrip()))
#print(len(multilínea.rstrip()))



#construir un menú

title='menú'.upper()
#print(title.center(20, '='))

#print('café'.ljust(16,'.')+'1$'.rjust(4))
#print('magdalena'.ljust(16,'.')+'1,75$'.rjust(4))
#print('tarta de queso'.ljust(16,'.')+'3$'.rjust(4))


#string index values

#print(first[1])
#print(first[1:-1])
#print(first[0:])


#some methods return boolean data

#print(first.startswith('L'))
#print(first.endswith('o'))


#boolean data type

myvalue=True
x=bool(False)
#print(type(#))
#print(isinstance(#, bool))



#numeric data types
#integer

price=100
best_price=int(80)
#print(type(price))
#print(isinstance(best_price, int))


#float type

gpa=3.28
#y= float(1.14)
#print(type(gpa))

#complex type

comp_value=5+3j
#print(type(comp_value))
#print(comp_value.real)
#print(comp_value.imag)


#built-in functions for numbers

#print(abs(gpa))
#print(abs(gpa* -1))

#print(round(gpa))

#print(round(gpa, 1))

import math

#print(math.pi)
#print(math.sqrt(64))
#print(math.ceil(gpa))
#print(math.floor(gpa))


#casting a string to a number

zipcode='10001'
zip_value=int(zipcode)
#print(type(zip_value))


#error if you attempt to cast incorrect data

#zip_value=int(New York)