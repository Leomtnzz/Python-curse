#Dictionaries

band={
    'vocals':'Plant',
    'guitar':'Page'
}

band2=dict(vocals='Plant', guitar='Page')

#print(band)
#print(band2)
#print(type(band))
#print(len(band))

#access items

#print(band2['guitar'])
#print(band.get('vocals'))

#list all keys
#print(band.keys())

#list all values
#print(band.values())

#list of key/values pairs as tuples

#print(band.items())

#verify a key exists

#print('guitar' in band)
#print('triangle' in band)

#Yo
#band=tuple(band)
#print(type(band))


#change values
band['vocals']='Coverdale' 
band.update({'bass':'JPJ'})

#print(band)


#remove items
#print(band.pop('bass'))
#print(band)


band['Drums']= 'Bonham'
#print(band)

#print(band.popitem())  #tuple
#print(type(band.popitem()))  #Yo
#print(band)

#Delete and clear

band['Drums']= 'Bonham'
#del band['Drums']
#print(band)

band2.clear()
#print(band2)

del band2

#Copy dictionaries

#No quiero que pase eso!

#band2=band #creates a reference
#print('Bad copy!')
#print (band2)
#print (band)

#band2['Drums']= 'Dave'
#print(band)


band2=band.copy()
band2['Drums']= 'Dave'
#print('Good copy!')
#print(band)
#print(band2)

#or use the dict() constructor function

band3=dict(band)
print('Good copy!')
print(band3)