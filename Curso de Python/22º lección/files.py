import os
# r=Read
# a=Append
# w=Write
# x=Create


#Read - error if it doesn't exist

f=open('names.txt', 'r')
# print(f.read())
# print(f.read(4))

# print(f.readline())
# print(f.readline())

# for line in f:
#     print(line)

# f.close()

# try:
#     f=open('rps.py')
#     print(f.read())
# except:
#     print('Hermano, eso no existe')
# finally:
#     f.close()


# try:
#     f=open('context.txt')
#     print(f.read())
# except:
#     print('Eso no existe')
# finally:
#     f.close()


# Append - Creates the file if it doesn't exist

# f=open('names.txt', 'a')
# f.write('\nLeo')
# f.close()

# f=open('names.txt')
# print(f.read())
# f.close()


# Write (overwrite)
f=open('context.txt','w')
f.write('He borrado todo lo que hay en context.txt')
f.close()

f=open('context.txt')
# print(f.read())
f.close()

# Dos maneras de crear un nuevo archivo

# 1º métoodo
# Abre un archivo para escribir y lo crea si no existe
f=open('names_list.txt','w')
f.write('Te acabo de crear primo')
f.close()


# 2º método
# Crea el archivo especificado pero da error si el archivo existe. Hay que importar os.
if not os.path.exists('leo.txt'):
    f=open('leo.txt', 'x')
    f.close()


# Borrar archivos
# Evitar un error si no existe
if os.path.exists('leo.txt'):
    os.remove('leo.txt')
else:
    print('El archivo que quieres borrar no existe')


if os.path.exists('names_list.txt'):
    os.remove('names_list.txt')


with open('more_names.txt') as f:
    content=f.read()

with open('names.txt','w') as f:
    f.write(content)