# cuadrado=lambda num: num*num
# print(cuadrado(4))

# addTwo=lambda num:num+2 
# print(addTwo(12))

#Yo
# a=int(input())
# b=int(input())

# suma_total=lambda a,b: a+b
# print(suma_total)


##################

# def funcbuilder(x):
#     return lambda num:num+x

# addten=funcbuilder(10)
# addtwenty=funcbuilder(20)

# print(addten(8))
# print(addtwenty(4))


#######################

numbers=[3,7,12,18,20,21]

# num_cuadrado=map(lambda num:num*num, numbers)
# print(list(num_cuadrado))

#Lo mismo pero con un loop
# for num in numbers:
#     print(list(num*num))

###########################


lambda num:num % 2 != 0 

odd_nums=filter(lambda num:num % 2 != 0, numbers)
#print(list(odd_nums))
# '!' significa 'Los que no cumplan eso' en este ejemplo, los que no sean iguales a 0.


#Lo mismo pero con un loop

# for num in numbers:
#     if num%2==1:
#         print(str(num))
#     else:
#         print()    


from functools import reduce

numbers=[1,2,3,4,5,4,3,2,1]

total=reduce(lambda acc,curr:acc+curr,numbers,10)
#El ultimo 10 es el 'starting value', y el resto se le suma a ese número. 
# print(total)


#mucho más simple.
print(sum(numbers,10))
#Lo mismo que el 'starting value' de antes.


names=('Jose','Mario','Leo','Caludio','yaguermeinster')
tot_names= reduce(lambda acc,curr:acc+len(curr),names,0)
print(tot_names)