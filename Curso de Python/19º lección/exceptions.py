class loserroresnomolan(Exception):
    pass

x=2
try:
    # raise loserroresnomolan('Esto simplemente no mola.')
    print(x/0)
    if not type(x) is str:
        raise TypeError('Goldito, pon un str, no int.')
    raise Exception('Soy una excepción especial broder. ;)')
except NameError:
    print('NameError es que algo no está definido.')
# except ZeroDivisionError:
#     print('No puedes dividir entre 0 bro.')
except ZeroDivisionError as error:
    print(error)
else:
    print('Sin errores.')
finally:
    print('Voy a aparecer con o sin errores bro :)')