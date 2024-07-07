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
#print('Good copy!')
#print(band3)


#nested dictionaries

member1={
    'name':'Plant',
    'instrument':'vocals'
}
member2={
    'name':'Page',
    'instrument':'guitar'
}
band={
    'member1':member1,
    'member2':member2,
    'member3':'curse'
}
#print(band)
#print(band['member1']['name'])

#Yo

#band.get('name')
#print(band.get('member1'))
#print(band)

#Yo

#print(band.popitem())
#print(band)

#Yo
#Da error

#band=dict(band)
#band+= (dict(['Dave']))

#Yo

#print(band.update({'member3':'Page'}))
#print(band)
#print(band.setdefault('member2'))
#print(band.clear())
#print(band.fromkeys('member2'))
#print(band.pop('member2'))
#print(band.keys())
#print(band)


#Sets

nums={1,2,3,4}

#nums2=set((1,2,3,4))
#print(nums)
#print(nums2)
#print(type(nums))
#print(len(nums))


#No duplicates are allowed

nums={1,2,2,3}
#print(nums)

#True is a dupe of 1 and False is a dupe of 0

nums={1,True,2,False,3,4,0} 
#print(nums)
#print(type(nums))

#Check if a value is in a set

#print(2 in nums)


#but you can't refer to an element in the set with an index position or a key

#No funciona
nums=int(nums)
print(nums.index(2, '4'))