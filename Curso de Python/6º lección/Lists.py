users=['Dave', 'John', 'Sara']

data=['Dave', 42, True]

emptylist=[]

#print('Dave'in data)
#print(users[1:2])


#print(users.index('John'))

#print(users[1:2])
#print(users[0:])

#print(len(data))

users.append('Elsa')
#print(users)

users+= ['Jason']
#print(users)

users.extend(['Robert', 'Jimmy'])
#print(users)

#users.extend(data)
#print(users)


users.insert(0,'Bob')
#print(users)

#print(type(users))

users[2:2]= ['Eddie','Alex']
#print(users) 

users[1:3]=['Robert','JPJ']
#print(users)

users.remove('Bob')
#print(users)


#print(users.pop())


del users[0]
#print(users)


#del data
#data.clear()
#print(data)

users[1:2] =['dave']
users.sort()
#print(users) 


users.sort(key=str.lower)
#users+= ['True' , 'zadig']
#users.reverse()
#print(users) 



nums=[4,42,78,1,5]
nums.reverse()
#print(nums)

#nums.sort(reverse= True)
#print(nums)

#print(sorted(nums, reverse=True))

numscopy=nums.copy()
mynums=list(nums)
mycopy=nums[:]

#print(numscopy)
#print(mynums)
#mycopy.sort()
#print(mycopy)
#print(nums)


#print(type(nums))

mylist=list([1,'Neil', True])
#print(mylist)


#tuples/tuplas

mytuple=tuple(('Dave', 43, False))
anothertuple=(1,4,2,8)

#print(mytuple)
#print(type(mytuple))
#print(type(anothertuple))

#anothertuple+= (tuple(['Dave']))
#print(anothertuple)
#print(type(anothertuple))

newlist=list(mytuple)
newlist.append('Neil') 
newtuple=tuple(newlist)
#print(newtuple)
#print(type(newtuple))
#print(type(newlist))

(one, *two, hey)=anothertuple
#print(one)
#print(two)
#print(hey)
#print(type(two))

anothertuple+=(tuple([2]))
print(anothertuple.index(2))
print(anothertuple.count(2))
print(anothertuple)